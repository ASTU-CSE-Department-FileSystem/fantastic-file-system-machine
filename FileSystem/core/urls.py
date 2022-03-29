from django.urls import path
from .views import DocumentFormView
urlpatterns = [

    path('test/', DocumentFormView.as_view(), name='test'),
]