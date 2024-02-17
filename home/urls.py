from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homePage, name='home'),
    path('admin/login', login_required(), name='admin'),  # Make sure 'admin_page' is the actual view function
    path('feedBacks', login_required(views.get_feed_backs), name='feedBacks'),  # Make sure 'admin_page' is the actual view function

]
