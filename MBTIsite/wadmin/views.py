from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import WMHeader, WMQuestion, WHEvent, WHResult


def home(request):
    context = {}

    if 'eventid' in request.session:
        eventid = request.session['eventid']
        rsEvt = WHEvent.objects.get(event_id=eventid)
        useranswer = rsEvt.user_answer
        usernote = rsEvt.user_note
    else:
        useranswer = ""
        eventid = None
        usernote = ""

    headerid = "0"
    parentid = "0"
    levelmax = 0
    levelnow = 1
    htitle = '이벤트를 선택하세요'
    ptitle = '질문을 선택하세요'
    rsQuestion = None
    qask = ""
    if 'headerid' in request.GET:
        headerid = request.GET['headerid']

        if headerid != "0":
            rsTmp = WMHeader.objects.get(id=headerid)
            htitle = rsTmp.pname + ". " + rsTmp.pdesc
            levelmax = rsTmp.level_max
            qask = rsTmp.qask

            parentid = "0"
            if 'parentid' in request.GET:
                parentid = request.GET['parentid']

            if parentid != "0":
                rsQuestion = WMQuestion.objects.filter(parent_id=parentid)

                rsTmp2 = WMQuestion.objects.get(id=parentid)
                ptitle = 'Level' + str(rsTmp2.qlevel) + ') ' + rsTmp2.qname + "  " + rsTmp2.qdesc
                levelnow = rsTmp2.qlevel
                qask = rsTmp2.qask
            else:
                rsQuestion = WMQuestion.objects.filter(header_id=headerid, qlevel=1)

    else:
        request.session.flush()

    rsTop = WMHeader.objects.filter()

    if levelmax == levelnow:
        rsResult = WHResult.objects.filter(header_id=headerid,result_code=useranswer).all()
    else:
        rsResult = None

    context["rsResult"] = rsResult

    context["qask"] = qask
    context["useranswer"] = useranswer
    context["eventid"] = eventid
    context["usernote"] = usernote
    context["headerid"] = headerid
    context["levelmax"] = levelmax
    context["levelnow"] = levelnow
    context["htitle"] = htitle
    context["ptitle"] = ptitle
    context["rsTop"] = rsTop
    context["rsQuestion"] = rsQuestion
    return render(request, "home.html", context)


@csrf_exempt
def make_session(request):
    context = {}

    headerid = request.GET['hid']
    rsTmp = WMHeader.objects.get(id=headerid)
    levelmax = rsTmp.level_max

    eventid = str(datetime.now())
    print(eventid)

    request.session['eventid'] = eventid
    WHEvent.objects.create(header_id=headerid,
                           event_id=eventid,
                           user_answer='',
                           event_result='',
                           level_max=levelmax)

    context["result_msg"] = "Sessiom 생성 되었습니다."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def reset_session(request):
    context = {}

    request.session.flush()

    context["result_msg"] = "Sessiom 초기화..."
    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def select_answer(request):
    context = {}

    qid = request.GET['qid']
    rsTmp = WMQuestion.objects.get(id=qid)
    adesc = str(rsTmp.order_no)
    anote = rsTmp.qname + " " + rsTmp.qdesc

    if 'eventid' in request.session:
        eventid = request.session['eventid']

        if WHEvent.objects.filter(event_id=eventid).exists():
            rsEvt = WHEvent.objects.get(event_id=eventid)
            user_answer = rsEvt.user_answer + adesc + '.'
            user_note = rsEvt.user_note + anote + "\r\n"
            rsEvt.user_answer = user_answer
            rsEvt.user_note = user_note
            rsEvt.save()

    context["user_answer"] = user_answer
    context["result_msg"] = "Selected... " + user_answer
    return JsonResponse(context, content_type="application/json")


def waadmin(request):
    context = {}

    qask = ""
    if 'headerid' in request.GET:
        headerid = request.GET['headerid']

        rsTmp = WMHeader.objects.get(id=headerid)
        htitle = rsTmp.pname + " - " + rsTmp.pdesc
        qask = rsTmp.qask

        if 'parentid' in request.GET:
            parentid = request.GET['parentid']

            if parentid != "0":
                rsQuestion = WMQuestion.objects.filter(parent_id=parentid)

                rsTmp2 = WMQuestion.objects.get(id=parentid)
                ptitle = 'Level' + str(rsTmp2.qlevel) + ') ' + rsTmp2.qname + "  " + rsTmp2.qdesc
                qask = rsTmp2.qask

            else:
                parentid = "0"
                rsQuestion = WMQuestion.objects.filter(header_id=headerid, qlevel=1)
                ptitle = '질문을 선택하세요'

        else:
            parentid = "0"
            rsQuestion = WMQuestion.objects.filter(header_id=headerid, qlevel=1)
            ptitle = '질문을 선택하세요'

    else:
        headerid = "0"
        parentid = "0"
        rsQuestion = None
        htitle = 'Event 선택하세요'
        ptitle = '질문을 선택하세요'


    rsTop = WMHeader.objects.filter()

    context["qask"] = qask
    context["headerid"] = headerid
    context["parentid"] = parentid
    context["htitle"] = htitle
    context["ptitle"] = ptitle
    context["rsTop"] = rsTop
    context["rsQuestion"] = rsQuestion
    return render(request, "waadmin.html", context)


@csrf_exempt
def create_qheader(request):
    context = {}

    pname = request.GET['pname']
    pdesc = request.GET['pdesc']

    WMHeader.objects.create(pname=pname,
                            pdesc=pdesc,
                            level_max=0)

    context["result_msg"] = "Header 생성 되었습니다."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def change_qheader(request):
    context = {}
    headerid = request.GET['headerid']
    flag = request.GET['flag']
    pvalue = request.GET['pvalue']

    rsTop = WMHeader.objects.get(id=headerid)
    if flag == 'pname':
        rsTop.pname = pvalue
        rsTop.save()
    elif flag == 'pdesc':
        rsTop.pdesc = pvalue
        rsTop.save()
    elif flag == 'plevel':
        rsTop.level_max = pvalue
        rsTop.save()

    context["result_msg"] = "수정 되었습니다."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def create_question(request):
    context = {}

    headerid = request.GET['headerid']
    rsTmp = WMHeader.objects.get(id=headerid)
    lavelmax = rsTmp.level_max

    if 'parentid' in request.GET:
        parentid = request.GET['parentid']

        if parentid != "0":

            rsTmp = WMQuestion.objects.get(id=parentid)
            qlevel = rsTmp.qlevel + 1
            parent_qname = rsTmp.qname

            rsTmp = WMQuestion.objects.filter(parent_id=parentid).all()

            orderno = 0
            for i in rsTmp:
                if i.order_no > orderno:
                    orderno = i.order_no

            orderno += 1

            if qlevel <= lavelmax:
                WMQuestion.objects.create(header_id=headerid,
                                           parent_id=parentid,
                                           order_no=orderno,
                                           qlevel=qlevel,
                                           qname=parent_qname + str(orderno) + '.',
                                           qdesc='Child...'
                                           )
            else:
                print('Max level... can not create')

        else:
            rsTmp = WMQuestion.objects.filter(header_id=headerid, parent_id=0).all()

            orderno = 0
            for i in rsTmp:
                if i.order_no > orderno:
                    orderno = i.order_no

            orderno += 1

            WMQuestion.objects.create(header_id=headerid,
                                       parent_id=parentid,
                                       order_no=orderno,
                                       qlevel=1,
                                       qname=str(orderno) + '.',
                                       qdesc='Child...'
                                       )

    context["result_msg"] = "질문 생성 ..."


    return render(request, "waadmin.html", context)


@csrf_exempt
def change_question(request):
    context = {}
    headerid = request.GET['headerid']
    qid = request.GET['qid']
    flag = request.GET['flag']
    qvalue = request.GET['qvalue']

    print(headerid)

    if qid == "0":
        rsQues = WMHeader.objects.get(id=headerid)
        print(rsQues)
        rsQues.qask = qvalue
        rsQues.save()
    else:
        rsQues = WMQuestion.objects.get(id=qid)
        if flag == 'qname':
            rsQues.qname = qvalue
            rsQues.save()
        elif flag == 'qdesc':
            rsQues.qdesc = qvalue
            rsQues.save()
        elif flag == 'qask':
            rsQues.qask = qvalue
            rsQues.save()

    context["result_msg"] = "수정 되었습니다."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def delete_question(request):
    context = {}
    qid = request.GET['qid']

    if WMQuestion.objects.filter(parent_id=qid).exists():
        context["flag"] = "1"
        context["result_msg"] = "Child가 있으면 삭제 되지 않습니다."
        return JsonResponse(context, content_type="application/json")
    else:
        rsRes = WMQuestion.objects.get(id=qid)
        rsRes.delete()
        context["flag"] = "0"
        context["result_msg"] = "삭제 되었습니다."
        return JsonResponse(context, content_type="application/json")


def waresult(request):
    context = {}

    if 'headerid' in request.GET:
        headerid = request.GET['headerid']

        rsTmp = WMHeader.objects.get(id=headerid)
        htitle = rsTmp.pname + ". " + rsTmp.pdesc
        levelmax = rsTmp.level_max

        rsResult = WHResult.objects.filter(header_id=headerid)
        rsTarget = WMQuestion.objects.filter(header_id=headerid, qlevel=levelmax).all()

    else:
        headerid = "0"
        rsResult = None
        rsTarget = None
        htitle = "Event를 선택하세요."

    rsTop = WMHeader.objects.filter()

    context["htitle"] = htitle
    context["headerid"] = headerid
    context["rsTop"] = rsTop
    context["rsResult"] = rsResult
    context["rsTarget"] = rsTarget
    return render(request, "waresult.html", context)

@csrf_exempt
def waresult_read(request):
    context = {}

    headerid = request.GET['headerid']

    rsTmp = WMHeader.objects.get(id=headerid)
    htitle = rsTmp.pname + ". " + rsTmp.pdesc
    levelmax = rsTmp.level_max

    rsTmp = WMQuestion.objects.filter(header_id=headerid, qlevel=levelmax)
    print(len(rsTmp))
    if rsTmp:

        queslist = ""
        for i in range(levelmax):
            qlevel = levelmax - i
            rs = WMQuestion.objects.filter(header_id=headerid, qlevel=qlevel).all()
            for x in rs:
                print(x)
                print("<div>" + x.qdesc + "<div>")
                queslist += "<div>" + x.qdesc + "<div>"

        context["flag"] = "0"
        context["result_msg"] = "Read for result..."

    else:
        context["flag"] = "1"
        queslist = "Read error..."
        context["result_msg"] = "Read error..."

    context["queslist"] = queslist
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def create_qresult(request):
    context = {}

    headerid = request.GET['headerid']

    WHResult.objects.create(header_id=headerid,
                            result_code='',
                            result_link='',
                            image_link='',
                            result_desc=''
                            )

    context["result_msg"] = "Blank result 생성 되었습니다."
    return JsonResponse(context, content_type="application/json")

@csrf_exempt
def change_qresult(request):
    context = {}
    rid = request.GET['rid']
    flag = request.GET['flag']
    pvalue = request.GET['pvalue']

    rsRes = WHResult.objects.get(id=rid)
    if flag == 'rcode':
        rsRes.result_code = pvalue
        rsRes.save()
    elif flag == 'rlink':
        rsRes.result_link = pvalue
        rsRes.save()
    elif flag == 'rimage':
        rsRes.image_link = pvalue
        rsRes.save()
    elif flag == 'rdesc':
        rsRes.result_desc = pvalue
        rsRes.save()

    context["result_msg"] = "수정 되었습니다."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def delete_qresult(request):
    context = {}
    rid = request.GET['rid']

    rsRes = WHResult.objects.get(id=rid)
    rsRes.delete()

    context["result_msg"] = "삭제 되었습니다."
    return JsonResponse(context, content_type="application/json")

