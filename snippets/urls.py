
from django.urls import path
from . import views
urlpatterns = [
   path('', views.Snippet_list, name=''),
   path('detail/<int:id>', views.Snippet_detail, name='detail'),
]
