from django.urls import re_path
import plant.views as views

app_name = "plant"

urlpatterns = [
    # re_path(r'^login$', views.account_login, name='login'),
    # re_path(r'^logout$', views.account_logout, name='logout'),
    re_path(r'^show$', views.show, name='show'),
]

