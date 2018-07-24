from django.conf.urls import url

from.import views

urlpatterns= [

url(r'^$' , views.index),
url(r'loginPage',views.loginPage),
url(r'login',views.login),
url(r'checkSess', views.checkUserSesh),
url(r'logOut', views.logout),
url(r'signUp',views.addUserPage),
url(r'completeSignUp',views.addUser),
url(r'updateLogin',views.getUpdatePage),
url(r'sendUpdate',views.updateUser),
url(r'^(?P<type>[a-zA-Z0-9-]+)/getArticles',views.getArticles),
url(r'^(?P<articleID>[0-9-]+)/getSpecificArticle',views.specificArticle),
url(r'^(?P<articleID>[0-9-]+)/comment',views.addComment),
url(r'^(?P<commentID>[0-9-]+)/(?P<articleID>[0-9-]+)/delete?',views.delComment),
url(r'^(?P<articleID>[0-9-]+)/likeDislike',views.likeDislike),
url(r'^(?P<articleID>[0-9-]+)/checkLikeDislike',views.checkLikedDisliked)

]