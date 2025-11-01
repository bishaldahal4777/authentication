from django.urls import path
from . import views

urlpatterns = [
    path('', views.any_view, name = "any"),
    path('create', views.create_view, name="create"),
    path('read', views.read_view, name="read"),
    path('update/<int:id>', views.update_view, name="update"),


]
