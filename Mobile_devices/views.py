from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models

class DeviceListView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'device_list'
    model = models.Device

    def get_queryset(self):
        return models.Device.objects.filter(title__iconstains=self.request.GET.get('categories')).order_by('-id')



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.request.GET.get('categories')
        return context


class DeviceDetailView(generic.DetailView):
    template_name = 'show_detail.html'
    context_object_name = 'device_id'

    def get_object(self, **kwargs):
        device_id = self.kwargs.get('id')
        return get_object_or_404(models.Device, id=device_id)

