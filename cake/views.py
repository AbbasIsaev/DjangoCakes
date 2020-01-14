from django.shortcuts import render
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

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShowCakesView, self).get_context_data(**kwargs)
        const = Const.get_json_all(Const)
        ctx['CONSTANTS'] = const
        return ctx


class CakeDetailView(DetailView):
    model = Cake
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CakeDetailView, self).get_context_data(**kwargs)
        const = Const.get_json_all(Const)
        ctx['CONSTANTS'] = const
        return ctx
