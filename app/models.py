from django.db import models
from django.core.validators import URLValidator
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField

class Category(models.Model):
	name = models.CharField(max_length=255, null=True)
	count = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return u'%s'%self.name


class Tag(models.Model):
	name = models.CharField(max_length=255, null=True)
	count = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_by = models.ForeignKey(User, related_name = 'user_tag_updated', editable = False, null=True)
	created_by = models.ForeignKey(User, related_name = 'user_tag_created', editable = False, null=True)

	def __str__(self):
		return u'%s'%self.name

class Post(models.Model):
	list_choice = (
		("ph", "Porn Hub"),
		("rb", "Red Tube"),
		("t8", "Tube8"),
		("yp", "YouPorn"),
		("xt", "XTube"),
		("sw", "Sparn Wire"),
	)

	provider = models.CharField(max_length=255, choices=list_choice, null=True)
	title = models.CharField(max_length=255, null=True)
	default_thumb = models.TextField(validators=[URLValidator()], null=True)
	video_id = models.CharField(max_length=255, null=True)
	link = models.TextField(validators=[URLValidator()])
	description = models.TextField(null=True)
	views= models.IntegerField(default = 0)
	category = models.ManyToManyField(Category, null=True)
	tag = models.ManyToManyField(Tag, null=True)
	# data_json = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_by = models.ForeignKey(User, related_name = 'user_post_updated', editable = False, null=True)
	created_by = models.ForeignKey(User, related_name = 'user_post_created', editable = False, null=True)

	def __str__(self):
		return u'%s'%self.title


# class Post_Tag(models.Model):
# 	post = models.ForeignKey(Post, related_name='name_post_tag', null=True)
# 	tag = models.ForeignKey(Tag, related_name='name_tag', null=True)

# 	def __str__(self):
# 		return u'%s'%self.post


# class Post_Category(models.Model):
# 	post = models.ForeignKey(Post, related_name='name_category_post', null=True)
# 	category = models.ForeignKey(Category, related_name='name_cate', null=True)

# 	def __str__(self):
# 		return u'%s'%self.post



class Static_Page(models.Model):
	list_choice = (
		("dmca", "DMCA"),
		("2257", "2257"),
	)

	name_page = models.CharField(max_length=255, choices=list_choice, default="dmca")
	title = models.CharField(max_length=255)
	content = RichTextField()

	def __str__(self):
		return u'%s'%self.title


class Demo(models.Model):
	name = models.CharField(max_length=45, null=True)
	post = models.ManyToManyField(Post)

	def __str__(self):
		return u'%s'%self.name