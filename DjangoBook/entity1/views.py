from django.shortcuts import render, redirect, get_object_or_404 

from django.http import JsonResponse 
from django.template.loader import render_to_string 

from .models import Entity1 
from .forms import Entity1Form 

def entity1_list(request): 
    context= {} 

    entity1 = Entity1.objects.filter().order_by('-id')[:100] 

    context['entity1'] = entity1 
    return render(request, 'meta/entity1_list.html', context) 


def save_entity1_form(request, form, template_name): 
    data = dict() 
    if request.method == 'POST': 
        if form.is_valid(): 
            form.save() 
            data['form_is_valid'] = True 
            entity1 = Entity1.objects.all().order_by('-id') 
            data['html_entity1_list'] = render_to_string('meta/includes/partial_entity1_list.html', { 
                'entity1': entity1 
            }) 
        else: 
            data['form_is_valid'] = False 

    context = {'form': form} 
    data['html_form'] = render_to_string(template_name, context, request=request) 
    return JsonResponse(data) 


def entity1_create(request): 
    if request.method == 'POST': 
        form = Entity1Form(request.POST) 
    else: 
        form = Entity1Form() 

    return save_entity1_form(request, form, 'meta/includes/partial_entity1_create.html') 


def entity1_update(request, pk): 
    entity1 = get_object_or_404(Entity1, pk=pk) 
    if request.method == 'POST': 
        form = Entity1Form(request.POST, instance=entity1) 
    else: 
        form = Entity1Form(instance=entity1) 

    return save_entity1_form(request, form, 'meta/includes/partial_entity1_update.html') 


def entity1_delete(request, pk): 
    entity1 = get_object_or_404(Entity1, pk=pk) 
    data = dict() 
    if request.method == 'POST': 
        entity1.delete() 
        data['form_is_valid'] = True 
        entity1 = Entity1.objects.all() 
        data['html_entity1_list'] = render_to_string('meta/includes/partial_entity1_list.html', { 
            'entity1': entity1 
        }) 
    else: 
        context = {'entity1': entity1} 
        data['html_form'] = render_to_string('meta/includes/partial_entity1_delete.html', context, request=request) 

    return JsonResponse(data) 


