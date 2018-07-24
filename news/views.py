from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from .models import Users
from .models import Articles
from .models import Comments
from .models import likedAndDislike
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core import serializers
from django.db import IntegrityError
# Create your views here.
def index(request):
	#load template
	articles=Articles.objects.all()
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	#articleCat=Articles.objects.all().distinct('Categories')
	if request.session.has_key('username'):
		context={'userloggedIn':True,'articleTitle':articles,'articleCat':articleCat}
	else:
		context={'userloggedIn':False,'articleTitle':articles,'articleCat':articleCat}
	template = loader.get_template('index.html')
	return render(request,'index.html',context)

def addUserPage(request):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	context={'articleCat':articleCat}
	template = loader.get_template('register.html')
	return render(request,'register.html',context)

def specificArticle(request,articleID):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	article=Articles.objects.filter(pk=articleID).all()
	comments=Comments.objects.filter(articleCommentedOn=articleID).all()#Retrives all the comments 
	liked= likedAndDislike.objects.filter(articleID=article,liked=True).count()#count the amount of likes in the article
	disliked= likedAndDislike.objects.filter(articleID=article,disliked=True).count()#count the amount of dislikes in the article
	
	if request.session.has_key('username'):
		user=Users.objects.get(email=request.session['username'])
		if likedAndDislike.objects.filter(articleID=article,UsersID=user).count() > 0: #if user has liked or disliked an article
			userLiked=likedAndDislike.objects.get(articleID=article,UsersID=user)
			context={'article':article,'comments':comments,'userloggedIn':True,'user':user,'liked':liked,'disliked':disliked,'userLiked':userLiked,'articleCat':articleCat}
		else: #user has not liked or disliked yet
			userLiked="nothing"
			context={'article':article,'comments':comments,'userloggedIn':True,'user':user,'liked':liked,'disliked':disliked,'userLiked':userLiked,'articleCat':articleCat}
	else:
		userLiked="noUser"
		context={'article':article,'comments':comments,'userloggedIn':False,'liked':liked,'disliked':disliked,'userLiked':userLiked,'articleCat':articleCat}
	template = loader.get_template('articleAndcomment.html')
	return render(request,'articleAndcomment.html',context)



def articlePage(request):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	context={'articleCat':articleCat}
	template = loader.get_template('articles.html')
	return render(request,'articles.html',context)


def loginPage(request):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	template = loader.get_template('login.html')
	return render(request,'login.html',{'userloggedIn':False,'articleCat':articleCat})


#check user name and password matches 
def login(request):
	Ausers=request.POST.get("formData[1][value]", '')
	Apassword=request.POST.get("formData[2][value]", '')
	if Users.objects.filter(email=Ausers,password=Apassword):
		request.session['username'] = Ausers
		request.session['password']=Apassword
		template = loader.get_template('index.html')
		print("log")
		return HttpResponse(Users.objects.get(email=Ausers).name)
	else:
		return 

def logout(request):
	print("logging out and flushing session")
	request.session.flush()
	return index(request)

def addUser(request):
	Ausers=request.POST.get("formData[1][value]", '')
	Apassword=request.POST.get("formData[4][value]", '')
	Aemail=request.POST.get("formData[2][value]", '')
	AphoneNumber=request.POST.get("formData[3][value]", '')
	try:
		Users(name=Ausers,email=Aemail,password=Apassword,telephone=AphoneNumber).save()
		request.session['username'] = Aemail
		request.session['password']=Apassword
		template = loader.get_template('index.html')
		return HttpResponse("Correct")
	except IntegrityError :
		print("incorrect")

def getArticles(request,type):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	catergory=""
	if(type=="all"):
		article=Articles.objects.all()
		catergory="All Catergory"
	else:
		article=Articles.objects.filter(Categories=type).all()
		catergory=type
	if request.session.has_key('username'):

		user=Users.objects.get(email=request.session['username'])
		context={'articleTitle':article,'userloggedIn':True,'user':user,'catergory':catergory,'articleCat':articleCat}
	else:
		context={'articleTitle':article,'userloggedIn':False,'catergory':catergory,'articleCat':articleCat}
	template = loader.get_template('articles.html')
	return render(request,'articles.html',context)

def getUpdatePage(request):
	articleCat=Articles.objects.values_list('Categories', flat=True).distinct()
	user=Users.objects.get(email=request.session['username'])
	context={'user':user,'userloggedIn':True,'articleCat':articleCat}
	template = loader.get_template('updateUser.html')
	return render(request,'updateUser.html',context) 

def updateUser(request):
	print("blarg")
	newName=request.POST.get("formData[1][value]", '')
	newPassword=request.POST.get("formData[4][value]", '')
	Aemail=request.POST.get("formData[2][value]", '')
	newPhoneNumber=request.POST.get("formData[3][value]", '')
	user=Users.objects.get(email=request.session['username'])
	if newPassword=="":
		user.name=newName
		user.telephone=newPhoneNumber
	else:
		user.name=newName
		user.telephone=newPhoneNumber
		user.password=newPassword
	user.save()
	return index(request)

def addComment(request,articleID):
	print("adding")
	user=Users.objects.get(email=request.session['username'])
	art=Articles.objects.get(pk=articleID)
	Comments(CommentInfo=request.POST.get('comment'),articleCommentedOn=art,UserWhoCommented=user).save()
	article=Articles.objects.filter(pk=articleID).all()
	comments=Comments.objects.filter(articleCommentedOn=articleID).all()
	if request.session.has_key('username'):
		context={'article':article,'comments':comments,'userloggedIn':True,'user':user}
	else:
		context={'article':article,'comments':comments,'userloggedIn':False}
	template = loader.get_template('articleAndcomment.html')
	return HttpResponse(render_to_string('refreshComments.html',context))


def delComment(request,commentID,articleID):
	print(request.session['username'])
	user=Users.objects.get(email=request.session['username'])
	commmentToDelete=Comments.objects.get(pk=commentID).delete()
	article=Articles.objects.filter(pk=articleID).all()
	comments=Comments.objects.filter(articleCommentedOn=articleID).all()
	if request.session.has_key('username'):
		context={'article':article,'comments':comments,'userloggedIn':True,'user':user}
	else:
		context={'article':article,'comments':comments,'userloggedIn':False}
	template = loader.get_template('articleAndcomment.html')
	return HttpResponse(render_to_string('refreshComments.html',context))

def likeDislike(request,articleID):
	userEmail=request.session['username']
	user=Users.objects.get(email=userEmail)
	article=Articles.objects.get(pk=articleID)
	print(request.POST.get("likedorDislike"))
	answer=request.POST.get("likedorDislike")
	if likedAndDislike.objects.filter(articleID=article,UsersID=user).count() > 0:
		obj=likedAndDislike.objects.get(articleID=article,UsersID=user)
		if answer=="Like":
			obj.liked=True
			obj.disliked=False

		else:
			obj.liked=False
			obj.disliked=True
		obj.save()
	else:
		if answer=="Like":
			likedAndDislike(articleID=article,UsersID=user,liked=True,disliked=False).save()
		else:
			likedAndDislike(articleID=article,UsersID=user,liked=False,disliked=True).save()
	liked= likedAndDislike.objects.filter(articleID=article,liked=True).count()
	disliked= likedAndDislike.objects.filter(articleID=article,disliked=True).count()
	return JsonResponse({"like":liked,"Dislike":disliked})

def checkLikedDisliked(request,articleID):
	if request.session.has_key('username'):
		print("userenabled")
		userEmail=request.session['username']
		user=Users.objects.get(email=userEmail)
		article=Articles.objects.get(pk=articleID)
		answer=request.POST.get("likedorDislike")
		if likedAndDislike.objects.filter(articleID=article,UsersID=user).count() > 0:
			obj=likedAndDislike.objects.get(articleID=article,UsersID=user)
			print("therearelikes")
			if obj.liked==True:
				print("liked")
				liked=True
				dislike=False
			elif obj.disliked==True:
				print("disliked")
				liked=False
				dislike=True
			else:
				print("neither")
				liked=False
				dislike=False
			return JsonResponse({"like":liked,"Dislike":dislike})
	else:
		return HttpResponse("NotLoggedIn")

	

def checkIfloggedIn(request):

	return context

def checkUserSesh(request):
	print("checking")
	if request.session.has_key('username'):
		username = request.session['username']
		password=request.session['password']
		combo=username+"*"+password
		return JsonResponse(combo,safe=False)
	else:
		return HttpResponse("nothing")