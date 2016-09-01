from django.conf.urls import url
from . import views


app_name = 'posts'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^create/$', views.post_create, name="wiwik"),
    url(r'^(?P<pk>[0-9]+)/$', views.Details.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^(?P<post_id>\d+)/upvote/$', views.upvote, name='upvote'),
    url(r'^(?P<post_id>\d+)/down_vote/$', views.down_vote, name='down_vote'),
    url(r'^categories/$', views.CategoriesIndex.as_view(), name='category'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoriesDetail.as_view(), name='category_detail'),
    url(r'^search/', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
    url(r'^your_posts/(?P<pk>[0-9]+)/$', views.YourPosts.as_view(), name='viewit'),
    url(r'^logging_out/goodbye/$', views.logout_user, name='logout_user'),
    # url(r'^view_posts/(?P<pk>[0-9]+)/$', views.view_user, name='view_user'),



]
