from django.urls import path

from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
    path('cvinquiry', views.cvinquiry, name='cvinquiry'),
    path('dealerinquiry', views.dealerinquiry, name='dealerinquiry'),
    path('appraisalinquiry', views.appraisalinquiry, name='appraisalinquiry')
]