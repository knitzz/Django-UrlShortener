from django.db import models
import string,random

# Create your models here.
 
# Create your models here.
class Urls(models.Model):
	short_id = models.SlugField(max_length=6,primary_key=True)
	httpurl = models.URLField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)

	def makeshort():
		length = 6
		char = string.ascii_uppercase + string.digits + string.ascii_lowercase
		# if the randomly generated short_id is used then generate next
		while True:
			short_id = ''.join(random.choice(char) for x in range(length))
			try:
				temp = Urls.objects.get(pk=short_id)
			except:
				return short_id

	def __str__(self):
		return self.httpurl
