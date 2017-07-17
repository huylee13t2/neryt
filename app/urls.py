from django.conf.urls import url

from app import views

urlpatterns = [
	url(r'^demo$', views.demo, name='demo'),
	url(r'^$', views.index, name='index'),
	url(r'^video/(?P<pk>[0-9]+)$', views.video, name='video'),
	# category
	url(r'^category/(?P<pk>[\w\-]+)$', views.view_category, name='view_category'),
	# tag
	url(r'^tag/(?P<pk>[\w\-]+)$', views.view_tag, name='view_tag'),
	# search
	url(r'^search$', views.search, name='search'),
	# static page
	url(r'^dmca$', views.dmca, name='dmca'),
	url(r'^18-usc-2257$', views.about_2257, name='about_2257'),
	# api
	url(r'^api/get-category-data$', views.get_data_category, name='get_data_category'),
]