from django.db import models
from datetime import datetime 

# Create your models here.


	

class Articles(models.Model):
	Categories = models.CharField(max_length=30)
	Description = models.CharField(max_length=4096)
	ArticleName = models.CharField(max_length=70);
	pub_date = models.DateTimeField('date published') #When published
	imageUrl=models.TextField(default="")
class Users(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	telephone=models.CharField(max_length=11)
	likes = models.ManyToManyField(Articles, through='likedAndDislike')
class Comments(models.Model):
	CommentInfo = models.CharField(max_length=500)
	articleCommentedOn = models.ForeignKey(Articles)#Article commented on will hae a foreign key linked to the actual article        
	timeOfComment = models.DateTimeField(default=datetime.now)
	UserWhoCommented = models.ForeignKey(Users)#Users who commented on the article
        
class likedAndDislike(models.Model):
 	articleID=models.ForeignKey(Articles)   
 	UsersID=models.ForeignKey(Users)
 	liked=models.BooleanField(default=False)
 	disliked=models.BooleanField(default=False)