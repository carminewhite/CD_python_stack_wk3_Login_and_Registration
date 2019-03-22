from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg_success$', views.reg_success),
    url(r'^log_success$', views.log_success),
    url(r'^process_registration$', views.process_registration),
    url(r'^process_login$', views.process_login),
    url(r'^log_out$', views.destroy_session),
]