from django.urls import path
from . import views
urlpatterns = [
     path('', views.data_entry, name='json-entry-point' )
]
