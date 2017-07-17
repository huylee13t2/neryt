from django.shortcuts import render
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import *

from app.models import Category, Tag, Post, Static_Page

import requests
import json
import simplejson as json


def index(request):
	try:
		posts = Post.objects.all()

		paginator = Paginator(posts, 24)
		page = request.GET.get('page', 1)

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		array = []
		for obj in contacts:
			array.append({
				'id' : obj.id,
				'image' : obj.default_thumb,
				'title' : obj.title,
				'link' : obj.link,
				'content' : obj.description,
			})

		return render(request, 'home/index.html', {'list' : array, 'contacts' : contacts})

	except:
		return render(request, 'errors/index.html')


def video(request, pk):
	try:
		post = Post.objects.get(id = pk)

		# categories
		categories = []
		for cate in post.category.all():
			categories.append({
				'id' : cate.id,
				'name' : cate.name,
			})

		# tags
		tags = []
		for tag in post.tag.all():
			tags.append({
				'id' : tag.id,
				'name' : tag.name,
			})

		# related
		list_related = Post.objects.filter(Q(category__in = post.category.all()) & ~Q(id = post.id) ).distinct()[:10]

		related = []
		for rel in list_related:
			url_rel = rel.link
			url_name_rel = ''
			output_url_rel = ''

			if url_rel.index("://") > -1:
				url_name_rel = url_rel.split('/')[3]
				http_rel = url_rel.split('/')[2]

			index_rel = url_rel.find(url_name_rel)
			index_http_rel = url_rel.find(http_rel)
			print(http_rel)

			if rel.provider == 'ph':
				print('ph')
				output_url_rel = url_rel.replace('view_video.php?viewkey=', 'embed/')
			elif rel.provider == 'rb':
				print('rb')
				output_url_rel = url_rel[:index_rel] + '?id=' + url_rel[index_rel:]
				output_url_rel = output_url_rel.replace('www', 'embed')

			elif rel.provider == 't8':
				print('t8')
				output_url_rel = url_rel[:index_rel] + 'embed/' + url_rel[index_rel:]

			elif rel.provider == 'yp':
				print('yp')
				output_url_rel = url_rel[:index_rel] + 'embed/' + url_rel[index_rel:]
				output_url_rel = output_url_rel.replace('/watch','')

			elif rel.provider == 'xt':
				print('xt')
				output_url_rel = url_rel[:index] + 'embedded/user/' + url_rel[index:]
				output_url_rel = output_url_rel.replace('watch', 'play')

			elif rel.provider == 'sw':
				print('sw')
				output_url_rel = url_rel

			related.append({
				'id' : rel.id,
				'image' : rel.default_thumb,
				'title' : rel.title,
				'link' : rel.link,
				'url' : output_url_rel,
				'content' : rel.description,
				'categories' : categories,
				'tags' : tags,
			})
			
		# content video
		url = post.link
		url_name = ''
		output_url = ''

		if url.index("://") > -1:
			url_name = url.split('/')[3]
			http = url.split('/')[2]

		index = url.find(url_name)
		index_http = url.find(http)

		if post.provider == 'ph':
			print('ph')
			output_url = url.replace('view_video.php?viewkey=', 'embed/')

		elif post.provider == 'rb':
			print('rb')
			output_url = url[:index] + '?id=' + url[index:]
			output_url = output_url.replace('www', 'embed')

		elif post.provider == 't8':
			print('t8')
			output_url = url[:index] + 'embed/' + url[index:]

		elif post.provider == 'yp':
			print('yp')
			output_url = url[:index] + 'embed/' + url[index:]
			output_url = output_url.replace('/watch','')

		elif post.provider == 'xt':
			print('xt')
			output_url = url[:index] + 'embedded/user/' + url[index:]
			output_url = output_url.replace('watch', 'play')

		elif post.provider == 'sw':
			print('sw')
			output_url = url


		response = {
			'id' : post.id,
			'image' : post.default_thumb,
			'title' : post.title,
			'link' : post.link,
			'url' : output_url,
			'content' : post.description,
			'categories' : categories,
			'provider' : post.get_provider_display(),
			'tags' : tags,
			'related' : related,
		}

		return render(request, 'video/index.html', {'post' : response})

	except:
		return render(request, 'errors/index.html')


def dmca(request):
	try:
		data = Static_Page.objects.get(name_page = 'dmca')

		return render(request, 'about/dmca.html', {'data' : data})
	except:
		return render(request, 'errors/index.html')


def about_2257(request):
	try:
		data = Static_Page.objects.get(name_page = 'dmca')
		
		return render(request, 'about/2257.html', {'data' : data})
	except:
		return render(request, 'errors/index.html')


def view_category(request, pk):
	try:
		posts = Post.objects.filter(category__name = pk).distinct()

		paginator = Paginator(posts, 24)
		page = request.GET.get('page', 1)

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		array = []
		for obj in contacts:
			array.append({
				'id' : obj.id,
				'image' : obj.default_thumb,
				'title' : obj.title,
				'link' : obj.link,
				'content' : obj.description,
			})

		return render(request, 'category/index.html', {'pk' : pk, 'list': array, 'contacts' : contacts})

	except:
		return render(request, 'errors/index.html')

def view_tag(request, pk):
	try:
		posts = Post.objects.filter(tag__name = pk).distinct()

		paginator = Paginator(posts, 24)
		page = request.GET.get('page', 1)

		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)

		array = []
		for obj in contacts:
			array.append({
				'id' : obj.id,
				'image' : obj.default_thumb,
				'title' : obj.title,
				'link' : obj.link,
				'content' : obj.description,
			})

		return render(request, 'tag/index.html', {'pk' : pk, 'list': array, 'contacts' : contacts})

	except:
		return render(request, 'errors/index.html')


def search(request):
	try:
		keywork = request.GET.get('keywork')

		posts = Post.objects.filter(title__icontains = keywork).distinct()
		if(posts.count() > 0):
			paginator = Paginator(posts, 24)
			page = request.GET.get('page', 1)

			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)

			array = []
			for obj in contacts:
				array.append({
					'id' : obj.id,
					'image' : obj.default_thumb,
					'title' : obj.title,
					'link' : obj.link,
					'content' : obj.description,
				})

			return render(request, 'search/index.html', {'keywork' : keywork, 'list': array, 'contacts' : contacts})

		else:
			return render(request, 'search/index.html', {'keywork' : keywork, 'msg' : 'No result!'})

	except:
		return render(request, 'errors/index.html')


# api
def get_data_category(request):
	categories = Category.objects.all().order_by('-count')[:10]
	tags = Tag.objects.all()
	tags_top =  tags.order_by('-count')[:10]

	categories_json = serializers.serialize('json', categories)
	tags_json = serializers.serialize('json', tags)
	tags_top_json = serializers.serialize('json', tags_top)

	response = {
		'result' : 1,
		'data' : {
			'categories' : categories_json,
			'tags' : tags_json,
			'tags_top' : tags_top_json,
		}
	}
	return JsonResponse(response)


def demo(request):
	r = requests.get('https://api.tube8.com/api.php?action=searchVideos&output=json&search=hard&thumbsize=all')
	data = r.json()

	video  = data['videos'][0]['video']
	title  = data['videos'][0]['title']
	tags  = data['videos'][0]['tags']
	thumbs  = data['videos'][0]['thumbs']
	
