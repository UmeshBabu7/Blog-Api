from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('blog-list/',views.blogList,name="blogList"),
    path('blog-details/<str:pk>',views.blogDetails,name="blogDetails"),
    path('blog-create/',views.blogCreate,name="blogCreate"),
    path('blog-update/<str:pk>',views.blogUpdate,name="blogUpdate"),
    path('blog-delete/<str:pk>',views.blogDelete,name="blogDelete"),

      
]