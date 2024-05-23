from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt

from nocode.models import Entity, Meta
from nocode.forms import EntityForm
from django.conf import settings

import os
import errno
import pymysql

MYDB = getattr(settings, "DATABASES", None)
MYDB_NAME = MYDB["default"]["NAME"]
MYDB_USER = MYDB["default"]["USER"]
MYDB_PWD = MYDB["default"]["PASSWORD"]
MYDB_HOST = MYDB["default"]["HOST"]
#dbCon = pymysql.connect(MYDB_HOST, MYDB_USER, MYDB_PWD, MYDB_NAME)


def entitylist(request):
    context = {}

    rsEntity = Entity.objects.all()
    context['rsEntity'] = rsEntity

    return render(request, 'entity_list.html', context)


def entity_create(request):
    context = {}

    rsTmp = Entity.objects.aggregate(Max('id'))
    lno = rsTmp['id__max']
    if lno == None:
        lno = 1
    else:
        lno += 1

    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> creating')
    rsEntity = Entity.objects.create(entity_name=f"Entity{lno}",
                                     status="0")

    txtString = f'''
              <tr>
                  <td>{rsEntity.id}</td>
                  <td>{rsEntity.entity_name}</td>
                  <td style="text-align:center;">{rsEntity.status}</td>
                  <td style="width:450px;">
                  </td>
                  <td style="width:150px;">
                  </td>
              </tr>
              '''

    context['txtString'] = txtString
    context['result_msg'] = 'Entity created...'
    return JsonResponse(context, content_type="application/json")


def meta_create(request):
    context = {}

    eid = request.GET['eid']
    ctype = request.GET['ctype']

    rsTmp = Meta.objects.filter(entity_id=eid).aggregate(Max('order_no'))
    mno = rsTmp['order_no__max']
    if mno == None:
        mno = 1
    else:
        mno += 1

    #print(eid)

    if ctype == 'Char':
        clength = 255
    else:
        clength = 0

    rsEntity = Meta.objects.create(entity_id=eid,
                                   column_name=f"Col00{mno}",
                                   column_type=ctype,
                                   column_length=clength,
                                   order_no=mno)

    context['result_msg'] = 'Entity created...'
    return JsonResponse(context, content_type="application/json")


def meta_read(request):
    context = {}

    eid = request.GET['eid']

    rsTmp = Meta.objects.filter(entity_id=eid)

    metastring = ""
    if rsTmp:
        for i in rsTmp:
            metastring += f"<div><span>{i.column_name}</span> <span>{i.column_type}</span></div>"
    else:
        metastring += f"<div>No meta...</div>"

    context['metastring'] = metastring
    context['result_msg'] = 'Entity created...'
    return JsonResponse(context, content_type="application/json")


def table_create(request):
    context = {}

    eid = request.GET['eid']

    dbCon = pymysql.connect(MYDB_HOST, MYDB_USER, MYDB_PWD, MYDB_NAME)

    cursor = dbCon.cursor()
    cursor.execute(f"SHOW TABLES LIKE 'entity{eid}'")
    rsTmp = cursor.fetchone()
    cursor.close()

    dbCon.close()

    if rsTmp:
        context['error'] = 'Y'
        context['result_msg'] = 'Table exists...'
        return JsonResponse(context, content_type="application/json")

    else:
        rsMeta = Meta.objects.filter(entity_id=eid)

        if rsMeta:
            sqlstring = f"CREATE TABLE `entity{eid}` ( \n"
            sqlstring += "	`id` INT(11) NOT NULL AUTO_INCREMENT, \n"
            for i in rsMeta:
                if i.column_type == "Char":
                    sqlstring += f"	`{i.column_name}` VARCHAR(255) NULL DEFAULT NULL, \n"
                elif i.column_type == "Int":
                    sqlstring += f"	`{i.column_name}` INT(11) NULL DEFAULT NULL, \n"
                else:
                    sqlstring += f"	`{i.column_name}` VARCHAR(255) NULL DEFAULT NULL, \n"

            sqlstring += "	PRIMARY KEY (`id`) \n"
            sqlstring += ") \n"
            sqlstring += "COLLATE='utf8_general_ci' \n"
            sqlstring += "ENGINE=InnoDB \n"
            sqlstring += "; "

            #print(sqlstring)

            dbCon = pymysql.connect(MYDB_HOST, MYDB_USER, MYDB_PWD, MYDB_NAME)

            cursor = dbCon.cursor()
            cursor.execute(sqlstring)
            cursor.close()

            dbCon.close()

            rsTmp = Entity.objects.get(id=eid)
            rsTmp.status = "TABLE"
            rsTmp.save()

        else:
            context['error'] = 'Y'
            context['result_msg'] = 'No meta...'
            return JsonResponse(context, content_type="application/json")

    context['error'] = 'N'
    context['result_msg'] = 'Table created...'
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codecreate_data(request):
    context = {}

    eid = request.GET['eid']

    # Table 있는지 읽어본다
    strsql = f"SHOW TABLES LIKE 'Entity{eid}'"
    print(strsql)

    dbCon = pymysql.connect(MYDB_HOST, MYDB_USER, MYDB_PWD, MYDB_NAME)
    cursor = dbCon.cursor()
    cursor.execute(strsql)
    rsTbl = cursor.fetchone()
    cursor.close()

    if rsTbl:
        fcontents = "from django.db import models \n\n"
        fforms = "from django import forms \n"

        strsql1 = f"SHOW COLUMNS FROM Entity{eid}"\

        cursor = dbCon.cursor()
        cursor.execute(strsql1)
        rsColumns = cursor.fetchall()
        cursor.close()

        if rsColumns:
            fforms += f"from entity{eid}.models import Entity{eid} \n\n"
            fforms += f"class Entity{eid}Form(forms.ModelForm): \n"
            fforms += f"    class Meta: \n"
            fforms += f"        model = Entity{eid} \n"
            ffields = "        fields = ("
            fcontents += f"class Entity{eid}(models.Model): \n"
            for i in rsColumns:
                print(i)
                if i[0] != 'id':
                    fcontents += f"    {i[0]} = models.CharField(max_length=50) \n"
                ffields += f"'{i[0]}',"

            fcontents += '\n    class Meta: \n'
            fcontents += f'        db_table = "entity{eid}" \n\n'
            fforms += ffields + ") "

        else:
            dbCon.close()
            context['error'] = "Y"
            context['result_msg'] = 'No columns...'
            return JsonResponse(context, content_type="application/json")

    else:
        dbCon.close()
        context['error'] = "Y"
        context['result_msg'] = 'No columns...'
        return JsonResponse(context, content_type="application/json")

    dbCon.close()

    filename = f"entity{eid}/models.py"

    print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close

    filename = f"entity{eid}/forms.py"
    f = open(filename, "w", encoding='utf8')
    f.write(fforms)
    f.close

    context['error'] = "N"
    context['result_msg'] = 'Meta data created...'
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codecreate_view(request):
    context = {}

    eid = request.GET['eid']

    fcontents = "from django.shortcuts import render, redirect, get_object_or_404 \n\n"
    fcontents += f"from django.http import JsonResponse \n"
    fcontents += f"from django.template.loader import render_to_string \n\n"
    fcontents += f"from .models import Entity{eid} \n"
    fcontents += f"from .forms import Entity{eid}Form \n\n"
    fcontents += f"def entity{eid}_list(request): \n"
    fcontents += '    context= {} \n\n'
    fcontents += f"    entity{eid} = Entity{eid}.objects.filter().order_by('-id')[:100] \n\n"
    fcontents += f"    context['entity{eid}'] = entity{eid} \n"
    fcontents += f"    return render(request, 'meta/entity{eid}_list.html', context) \n\n\n"

    fcontents += f"def save_entity{eid}_form(request, form, template_name): \n"
    fcontents += "    data = dict() \n"
    fcontents += "    if request.method == 'POST': \n"
    fcontents += "        if form.is_valid(): \n"
    fcontents += "            form.save() \n"
    fcontents += "            data['form_is_valid'] = True \n"
    fcontents += f"            entity{eid} = Entity{eid}.objects.all().order_by('-id') \n"
    fcontents += "            data['html_entity" + str(eid) + "_list'] = render_to_string('meta/includes/partial_entity" + str(eid) + "_list.html', { \n"
    fcontents += f"                'entity{eid}': entity{eid} \n"
    fcontents += "            }) \n"
    fcontents += "        else: \n"
    fcontents += "            data['form_is_valid'] = False \n\n"
    fcontents += "    context = {'form': form} \n"
    fcontents += "    data['html_form'] = render_to_string(template_name, context, request=request) \n"
    fcontents += "    return JsonResponse(data) \n\n\n"

    fcontents += f"def entity{eid}_create(request): \n"
    fcontents += f"    if request.method == 'POST': \n"
    fcontents += f"        form = Entity{eid}Form(request.POST) \n"
    fcontents += f"    else: \n"
    fcontents += f"        form = Entity{eid}Form() \n\n"
    fcontents += f"    return save_entity{eid}_form(request, form, 'meta/includes/partial_entity{eid}_create.html') \n\n\n"

    fcontents += f"def entity{eid}_update(request, pk): \n"
    fcontents += f"    entity{eid} = get_object_or_404(Entity{eid}, pk=pk) \n"
    fcontents += f"    if request.method == 'POST': \n"
    fcontents += f"        form = Entity{eid}Form(request.POST, instance=entity{eid}) \n"
    fcontents += f"    else: \n"
    fcontents += f"        form = Entity{eid}Form(instance=entity{eid}) \n\n"
    fcontents += f"    return save_entity{eid}_form(request, form, 'meta/includes/partial_entity{eid}_update.html') \n\n\n"

    fcontents += f"def entity{eid}_delete(request, pk): \n"
    fcontents += f"    entity{eid} = get_object_or_404(Entity{eid}, pk=pk) \n"
    fcontents += f"    data = dict() \n"
    fcontents += f"    if request.method == 'POST': \n"
    fcontents += f"        entity{eid}.delete() \n"
    fcontents += f"        data['form_is_valid'] = True \n"
    fcontents += f"        entity{eid} = Entity{eid}.objects.all() \n"
    fcontents += "        data['html_entity" + str(eid) + "_list'] = render_to_string('meta/includes/partial_entity" + str(eid) + "_list.html', { \n"
    fcontents += f"            'entity{eid}': entity{eid} \n"
    fcontents += "        }) \n"
    fcontents += f"    else: \n"
    fcontents += "        context = {'entity" + str(eid) + "': entity" + str(eid) + "} \n"
    fcontents += f"        data['html_form'] = render_to_string('meta/includes/partial_entity{eid}_delete.html', context, request=request) \n\n"
    fcontents += f"    return JsonResponse(data) \n\n\n"

    filename = f"entity{eid}/views.py"

    print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close

    context['error'] = 'N'
    context['result_msg'] = 'Meta views created...'
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codecreate_template(request):
    context = {}

    eid = request.GET['eid']

    # Table 있는지 읽어본다
    strsql = f"SHOW TABLES LIKE 'Entity{eid}'"
    # print(strsql)

    dbCon = pymysql.connect(MYDB_HOST, MYDB_USER, MYDB_PWD, MYDB_NAME)
    cursor = dbCon.cursor()
    cursor.execute(strsql)
    rsTbl = cursor.fetchone()
    cursor.close()

    if rsTbl:
        fcontents = "from django.db import models \n\n"
        fforms = "from django import forms \n"

        strsql1 = f"SHOW COLUMNS FROM Entity{eid}"

        cursor = dbCon.cursor()
        cursor.execute(strsql1)
        rsColumns = cursor.fetchall()
        cursor.close()

        if rsColumns:
            thstring = ""
            tdstring = ""
            tdcount = len(rsColumns) + 1
            for i in rsColumns:
                # print(i)
                if i[0] == 'id':
                    thstring += f"        <th>#</th> \n"
                else:
                    thstring += f"        <th>{i[0]} {i[1]}</th> \n"

                tdstring += "   <td>{{ ett." + i[0] + " }}</td>  \n"

        else:
            dbCon.close()
            context['error'] = "Y"
            context['result_msg'] = 'No columns...'
            return JsonResponse(context, content_type="application/json")

    else:
        dbCon.close()
        context['error'] = "Y"
        context['result_msg'] = 'No columns...'
        return JsonResponse(context, content_type="application/json")

    dbCon.close()


    #************************************************************************************************
    # list
    #************************************************************************************************
    fcontents = "{% extends 'base.html' %} \n\n"
    fcontents += "{% load static %} \n\n"
    fcontents += "{% block javascript %} \n"
    fcontents += "    <script src=" + '"' + "{% static 'jsmeta/script_entity" + str(eid) + ".js' %}" + '"' + "></script> \n"
    fcontents += "{% endblock %} \n\n"
    fcontents += "{% block content %} \n\n"
    fcontents += f"<h1 class='page-header'>Entity{eid} 관리</h1> \n"
    fcontents += "<p> \n"
    fcontents += "  <button type='button' class='btn btn-primary js-create-entity" + str(eid) + "' data-url=" + '"' + "{% url 'entity" + str(eid) + "_create' %}" + '"' + "> \n"
    #fcontents += "  <button type='button' class='btn btn-primary js-create-entity" + str(eid) + "' data-url=" + '"' + " " + '"' + "> \n"
    fcontents += f"등록</button> \n"
    fcontents += "</p> \n"
    fcontents += f'<table class="table" id="entity{eid}-table"> \n'
    fcontents += '  <thead> \n'
    fcontents += '    <tr> \n'

    fcontents += thstring

    fcontents += '      <th></th> \n'
    fcontents += '    </tr> \n'
    fcontents += '  </thead> \n'
    fcontents += '  <tbody> \n'
    fcontents += '    {% include "meta/includes/partial_entity' + str(eid) + '_list.html" %} \n'
    fcontents += '  </tbody> \n'
    fcontents += '</table> \n'
    fcontents += f'<div class="modal fade" id="modal-entity{eid}"> \n'
    fcontents += '  <div class="modal-dialog"> \n'
    fcontents += '    <div class="modal-content">  \n'
    fcontents += '    </div> \n'
    fcontents += '  </div> \n'
    fcontents += '</div> \n\n'

    fcontents += "{% endblock %} \n\n"

    filename = f"templates/meta/entity{eid}_list.html"

    # print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close

    #************************************************************************************************
    # partial list
    #************************************************************************************************
    fcontents = "{% for ett in entity" + str(eid) + " %} \n"
    fcontents += ' <tr> \n'

    fcontents += tdstring

    fcontents += '    <td style="width:150px;text-align:right;"> \n'
    fcontents += f'      <button type="button"  class="btn btn-warning btn-sm js-update-entity{eid}' + '" data-url="{% url ' + f"'entity{eid}_update'" + ' ett.id %}"> \n'
    fcontents += '          수정 \n'
    fcontents += '       </button> \n'
    fcontents += f'      <button type="button"  class="btn btn-danger btn-sm js-delete-entity{eid}' + '" data-url="{% url ' + f"'entity{eid}_delete'" + ' ett.id %}"> \n'
    fcontents += '          삭제 \n'
    fcontents += '      </button> \n'
    fcontents += '    </td> \n'
    fcontents += ' </tr> \n'
    fcontents += '{% empty %} \n'
    fcontents += ' <tr> \n'
    fcontents += f'  <td colspan="{tdcount}" class="text-centr bg-warning">No data...</td> \n'
    fcontents += ' </tr> \n'
    fcontents += '{% endfor %} \n'

    filename = f"templates/meta/includes/partial_entity{eid}_list.html"

    # print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close


    #************************************************************************************************
    # partial form
    #************************************************************************************************
    fcontents = '{% load widget_tweaks %} \n\n'
    fcontents += '{% for field in form %} \n'
    fcontents += '  <div class="form-group{% if field.errors %} has-error {% endif %}"> \n'
    fcontents += '    <label for="{{ field.id_for_label }}">{{ field.label }}</label> \n'
    fcontents += '    {% render_field field class="form-control" %} \n'
    fcontents += '    {% for error in field.errors %} \n'
    fcontents += '      <p class="help-block">{{ error }}</p> \n'
    fcontents += '    {% endfor %} \n'
    fcontents += '  </div> \n'
    fcontents += '{% endfor %} \n'

    filename = f"templates/meta/includes/partial_entity{eid}_form.html"

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close


    #************************************************************************************************
    # partial create
    #************************************************************************************************
    fcontents = '<form method="post" action="{% url ' + f"'entity{eid}_create'" + ' %}" class="js-entity' + f'{eid}-create-form"> \n'
    fcontents += '  {% csrf_token %} \n'
    fcontents += '  <div class="modal-header"> \n'
    fcontents += '    <h4 class="modal-title">등록</h4> \n'
    fcontents += '    <button type="button" class="close" data-dismiss="modal" aria-label="Close"> \n'
    fcontents += '      <span aria-hidden="true">×</span> \n'
    fcontents += '    </button> \n'
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-body"> \n'
    fcontents += "    {% include 'meta/includes/partial_entity" + str(eid) +"_form.html' %} \n"
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-footer"> \n'
    fcontents += '    <button type="button" class="btn btn-default" data-dismiss="modal">닫기</button> \n'
    fcontents += '    <button type="submit" class="btn btn-primary">저장</button> \n'
    fcontents += '  </div> \n'
    fcontents += '</form> \n'

    filename = f"templates/meta/includes/partial_entity{eid}_create.html"

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close


    #************************************************************************************************
    # partial update
    #************************************************************************************************
    fcontents = '<form method="post" action="{% url ' + f"'entity{eid}_update'" + ' form.instance.pk %}" class="js-entity' + f'{eid}-update-form"> \n'
    fcontents += '  {% csrf_token %} \n'
    fcontents += '  <div class="modal-header"> \n'
    fcontents += '    <h4 class="modal-title">수정</h4> \n'
    fcontents += '    <button type="button" class="close" data-dismiss="modal" aria-label="Close"> \n'
    fcontents += '      <span aria-hidden="true">×</span> \n'
    fcontents += '    </button> \n'
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-body"> \n'
    fcontents += "    {% include 'meta/includes/partial_entity" + str(eid) +"_form.html' %} \n"
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-footer"> \n'
    fcontents += '    <button type="button" class="btn btn-default" data-dismiss="modal">닫기</button> \n'
    fcontents += '    <button type="submit" class="btn btn-primary">수정</button> \n'
    fcontents += '  </div> \n'
    fcontents += '</form> \n'

    filename = f"templates/meta/includes/partial_entity{eid}_update.html"

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close

    #************************************************************************************************
    # partial delete
    #************************************************************************************************
    fcontents = '<form method="post" action="{% url ' + f"'entity{eid}_delete'" + ' ett.id %}" class="js-entity' + f'{eid}-delete-form"> \n'
    fcontents += '  {% csrf_token %} \n'
    fcontents += '  <div class="modal-header"> \n'
    fcontents += '    <h4 class="modal-title">삭제 확인</h4> \n'
    fcontents += '    <button type="button" class="close" data-dismiss="modal" aria-label="Close"> \n'
    fcontents += '      <span aria-hidden="true">×</span> \n'
    fcontents += '    </button> \n'
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-body"> \n'
    fcontents += '    <p class="lead">삭제 하시겠습니까? <b>{{ ett.entity_name }}</b></p> \n'
    fcontents += '  </div> \n'
    fcontents += '  <div class="modal-footer"> \n'
    fcontents += '    <button type="button" class="btn btn-default" data-dismiss="modal">닫기</button> \n'
    fcontents += '    <button type="submit" class="btn btn-danger">삭제</button> \n'
    fcontents += '  </div> \n'
    fcontents += '</form> \n'

    filename = f"templates/meta/includes/partial_entity{eid}_delete.html"

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close


    #************************************************************************************************
    # script
    #************************************************************************************************
    fcontents = '$(document).ready(function(){ \n'
    fcontents += '    var loadForm = function () { \n'
    fcontents += '        var btn = $(this); \n'
    fcontents += '        $.ajax({ \n'
    fcontents += '          url: btn.attr("data-url"), \n'
    fcontents += '          type: "get", \n'
    fcontents += '          dataType: "json", \n'
    fcontents += '          beforeSend: function () { \n'
    fcontents += f'            $("#modal-entity{eid} .modal-content").html(""); \n'
    fcontents += f'            $("#modal-entity{eid}").modal("show"); \n'
    fcontents += '          }, \n'
    fcontents += '          success: function (data) { \n'
    fcontents += f'            $("#modal-entity{eid} .modal-content").html(data.html_form); \n'
    fcontents += '          } \n'
    fcontents += '        }); \n'
    fcontents += '    }; \n\n'
    fcontents += '    var saveForm = function () { \n'
    fcontents += '        var form = $(this); \n'
    fcontents += '        $.ajax({ \n'
    fcontents += '          url: form.attr("action"), \n'
    fcontents += '          data: form.serialize(), \n'
    fcontents += '          type: form.attr("method"), \n'
    fcontents += '          dataType: "json", \n'
    fcontents += '          success: function (data) { \n'
    fcontents += '            if (data.form_is_valid) { \n'
    fcontents += f'              $("#entity{eid}-table tbody").html(data.html_entity{eid}_list); \n'
    fcontents += f'              $("#modal-entity{eid}").modal("hide"); \n'
    fcontents += '            } \n'
    fcontents += '            else { \n'
    fcontents += f'              $("#modal-entity{eid} .modal-content").html(data.html_form); \n'
    fcontents += '            } \n'
    fcontents += '          } \n'
    fcontents += '        }); \n'
    fcontents += '      return false; \n'
    fcontents += '    }; \n\n'

    fcontents += '    // Binding \n'
    fcontents += f'    $(".js-create-entity{eid}").click(loadForm); \n'
    fcontents += f'    $("#modal-entity{eid}").on("submit", ".js-entity{eid}-create-form", saveForm); \n\n'

    fcontents += '    // Update entity \n'
    fcontents += f'    $("#entity{eid}-table").on("click", ".js-update-entity{eid}", loadForm); \n'
    fcontents += f'    $("#modal-entity{eid}").on("submit", ".js-entity{eid}-update-form", saveForm); \n\n'

    fcontents += '    // Delete entity \n'
    fcontents += f'    $("#entity{eid}-table").on("click", ".js-delete-entity{eid}", loadForm); \n'
    fcontents += f'    $("#modal-entity{eid}").on("submit", ".js-entity{eid}-delete-form", saveForm); \n\n'

    fcontents += '}); \n'

    filename = f"static/jsmeta/script_entity{eid}.js"

    # print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close


    context['error'] = 'N'
    context['result_msg'] = 'Meta templates created...'
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codecreate_config(request):
    context = {}

    eid = request.GET['eid']

    fcontents = "from django.contrib import admin \n"
    fcontents += "from django.urls import path \n"
    fcontents += "from django.conf.urls import url, include \n\n"
    fcontents += "from . import views \n\n"
    fcontents += "urlpatterns = [ \n"
    fcontents += f"    url(r'^entity{eid}/$', views.entity{eid}_list, name='entity{eid}_list'), \n"
    fcontents += f"    url(r'^entity{eid}/create/$', views.entity{eid}_create, name='entity{eid}_create'), \n"
    fcontents += f"    url(r'^entity{eid}/(?P<pk>\d+)/update/$', views.entity{eid}_update, name='entity{eid}_update'), \n"
    fcontents += f"    url(r'^entity{eid}/(?P<pk>\d+)/delete/$', views.entity{eid}_delete, name='entity{eid}_delete'), \n"
    fcontents += "] \n"

    filename = f"entity{eid}/urls.py"

    # print(filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
                context['error'] = "Y"
                context['result_msg'] = "Can not create directory..."
                return JsonResponse(context, content_type="application/json")

    f = open(filename, "w", encoding='utf8')
    f.write(fcontents)
    f.close

    rsTmp = Entity.objects.get(id=eid)
    rsTmp.status = "CONFIG"
    rsTmp.save()

    context['error'] = 'N'
    context['result_msg'] = 'Meta config...'
    return JsonResponse(context, content_type="application/json")


def entity_config2(request):
    context = {}

    import django.conf as conf
    conf.settings.MYAPP2 = ["11111"]
    conf.settings.INSTALLED_APPS = ['sdsdsds']
    # https://www.programcreek.com/python/example/100168/django.conf.settings.configure

    from django.conf import settings
    if not settings.configured:
        settings.configure(myapp_defaults, DEBUG=True)
        settings.configure(MYAPP2='dsdsds7d6s7d6s7ds')

    # myset = getattr(settings, "INSTALLED_APPS", None)
    # settings.configure(MYAPP2="tessst4")

    # MYDB = getattr(settings, "DATABASES", None)
    # MYDB_NAME = MYDB["default"]["NAME"]

    myapp = getattr(settings, "MYAPP1", None)
    print(myapp)

    context['result_msg'] = 'Config test...'
    return JsonResponse(context, content_type="application/json")


def entity_config3(request):
    context = {}

    from django.conf import settings

    settings.configure(
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'rest_framework',
            'tests',
        ),
    )
    # https://stackoverflow.com/questions/19855160/django-where-do-i-call-settings-configure
    import django
    django.setup()

    context['result_msg'] = 'Config test...'
    return JsonResponse(context, content_type="application/json")


def entity_config(request):
    context = {}

    # from nocode.default_settings import *
    INSTALLED_APPS += ('nocode2',)



    context['result_msg'] = 'Config test...'
    return JsonResponse(context, content_type="application/json")

