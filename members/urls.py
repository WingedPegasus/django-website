from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('members/', Member, name='members'),
    path('dark_theme/',views.dark_theme,name='dark_theme'),
    path('search/',views.search,name='search'),
    path('light_theme/',views.light_theme,name='light_theme'),
    path('set-cookie/', set_cookie_view, name='set_cookie'),
    path('read-cookie/', read_cookie_view, name='read_cookie'),
    path('delete-cookie/', delete_cookie_view, name='delete_cookie'),
    path('cookie-template/', cookie_template_view, name='cookie_template'),
    path('set-cookie-options/', set_cookie_with_options, name='set_cookie_options'),
]