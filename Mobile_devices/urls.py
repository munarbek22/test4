from django.urls import path
from .views import DeviceListView, DeviceDetailView

urlpatterns = [
    path('', DeviceListView.as_view(), name='device_list'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
]