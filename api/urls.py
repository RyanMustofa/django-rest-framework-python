from django.urls import path
from . import views

urlpatterns = [
    path('list-all',views.listAll,name="list-all"),
    path('list-detail/<str:pk>/',views.listDetail,name="list-detail"),
    path('list-create',views.listCreate,name="list-create"),
    path('list-update/<str:pk>/',views.listUpdate,name="list-update"),
    path('list-delete/<str:pk>/',views.listDelete,name="list-delete"),
]
