import json

from django.db.models import Q
from django.shortcuts import render
from django.template.defaulttags import register
from django.views.generic import ListView, DetailView

from const.models import Const
from .models import Cake


def contact(request):
    const = Const.get_json_all(Const)
    data = {'CONSTANTS': const}
    return render(request, 'cake/contact.html', data)


class ShowCakesView(ListView):
    model = Cake
    template_name = 'cake/main.html'
    context_object_name = 'Cakes'
    ordering = ['-updated_by']
    # Оптимизация запросов
    # prefetch_related - извлечение связанных объектов, связь многие-ко-многим
    # select_related - извлечение связанных объектов, связь один-ко-многим
    queryset = Cake.objects.prefetch_related('photos')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShowCakesView, self).get_context_data(**kwargs)
        const = Const.get_json_all(Const)
        ctx['CONSTANTS'] = const
        return ctx


class CakeDetailView(DetailView):
    model = Cake
    context_object_name = 'item'
    queryset = Cake.objects.prefetch_related('photos')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CakeDetailView, self).get_context_data(**kwargs)
        const = Const.get_json_all(Const)
        ctx['CONSTANTS'] = const
        return ctx


class SearchCakesView(ListView):
    template_name = 'cake/main.html'
    context_object_name = 'Cakes'
    ordering = ['-updated_by']

    def get_queryset(self):
        value = self.request.GET.get('search')
        return Cake.objects.filter(Q(name__icontains=value) | Q(text__icontains=value))

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(SearchCakesView, self).get_context_data(**kwargs)
        const = Const.get_json_all(Const)
        ctx['CONSTANTS'] = const
        ctx['search_value'] = self.request.GET.get('search')
        return ctx


@register.filter(name='filter__const_by_key')
def filter__const_by_key(dictionary, key):
    return dictionary.get(key)


@register.filter(name='filter__str')
def filter__str(dictionary, key):
    value = dictionary.get(key)
    return json.dumps(value, indent=4)


@register.filter(name='filter__is_active')
def filter__is_active(number):
    if number == 0:
        return 'active'
    return ''
