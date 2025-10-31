from django.urls import path, include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.auth_view, name="auth_view")


]
