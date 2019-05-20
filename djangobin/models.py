from django.db import models
from .utils import Preference as Pref
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from .utils import Preference as Pref

class Post:
	title = models.CharField()
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)    

	class Meta:
		ordering = ['-pub_date']

class Author(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	active = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	last_logged_in = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ", " + self.email

	class Meta:
		unique_together = (('name', 'email'),)

class Employee:
	first_name = models.CharField()
	last_name = models.CharField()
	address = models.CharField()

	class Meta:
		indexes = [
		models.Index(fields = ['last_name', 'first_name']),
		models.Index(fields = ['address'], name = 'address_idx')
		]

class Language(models.Model):
	name = models.CharField(max_length=100)
	lang_code = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	mime = models.CharField(max_length=100, help_text='MIME to use when sending snippet as file.')
	file_extension = models.CharField(max_length=10)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def get_lexer(self):
		return lexers.get_lexer_by_name(self.lang_code)

	def __str__(self):
		return (self.title if self.title else "Untitled") + "-" +self.language.name

	def get_absolute_url(self):
		return reverse('djangobin:trending_snippets', args=[self.slug])

class Snippet(models.Model):
	title = models.CharField(max_length=200, blank=True)
	original_code = models.TextField()
	highlighted_code = models.TextField()
	expiration = models.CharField(max_length=10, choices=Pref.expiration_choices)
	exposure = models.CharField(max_length=10, choices=Pref.exposure_choices)
	hits = models.IntegerField(default=0)
	slug = models.SlugField()
	created_on = models.DateTimeField(auto_now_add=True)

	language = models.ForeignKey(Language, on_delete = models.CASCADE)
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	tags = models.ManyToManyField('Tag')

	def highlight(self):
		formatter = HtmlFormatter(linenos=True)
		return highlight(self.original_code, self.language.get_lexer(), formatter)

	def get_absolute_url(self):
		return reverse('djangobin:snippet_detail', args=[self.slug])

	class Meta:
		ordering = ['-created_on']

class Tag(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('djangobin:tag_list', args=[self.slug])

	class Meta:
		ordering = ['name']