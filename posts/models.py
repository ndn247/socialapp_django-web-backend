from django.db import models
from mezzanine.core.models import Ownable, Displayable
from mezzanine.generic.fields import RatingField, CommentsField
from django.utils import timezone

# Create your models here.

#subclasses of Message model to represent different types of messages(text, image, poll, etc)
"""class Message(models.Model):

	pass

class Message_Text(Message):

	text = models.TextField()

class Message_Image(Message):

	image = models.ImageField(upload_to='image_posts')

class Message_Poll(Message):

    question = models.CharField(max_length=200)

class Choice(models.Model):

    poll = models.ForeignKey(Message_Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#
"""

class Post(models.Model):

	#message = models.OneToOneField(Message)
	title = models.CharField(max_length=200)
	publish_date = models.DateTimeField(default=timezone.now())
	owner = models.ForeignKey('auth.User', related_name='posts')
	message = models.TextField()
	rating = RatingField()
	allow_comments = models.BooleanField(default=True)
	comments = CommentsField()
	related_posts = models.ManyToManyField("self", blank=True)

class TestModel(models.Model):
	msg = models.TextField()


class Profile(models.Model):

	user = models.OneToOneField("auth.User")
	image = models.ImageField(upload_to='profile_pics')
	description = models.TextField(blank=True)
	karma = models.IntegerField(default=0, editable=False)

	def __unicode__(self):
		return "%s (%s)" % (self.user, self.karma)


