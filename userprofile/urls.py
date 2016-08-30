from django.conf.urls import url
from . import views

app_name = 'userprofile'

urlpatterns = [
            url(r'^update_profile/$', views.update_profile, name='update'),
            url(r'^your_profile/$', views.your_profile, name='your_profile'),
            # url(r'^profile/(?P<username>[a-zA-Z0-9]+)/$', views.home, name='homage'),
]
