import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
#from __future__import unicode literals

#class polls(models.Model):
#	title = models.CharField(max_length=100)
#	content=models.TextField()

#def __unicode__(self):
#	return self.title

class Question(models.Model):
	list_filter=['pub_date']
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return timezone.now()-datetime.timedelta(days=1)<=self.pub_date<=now
		
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	
#	return self.pub_date>= timezone.now()
	datetime.timedelta(days=1)

	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')





class Choice(models.Model):
	def __str__(self):
		return self.choice_text
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
