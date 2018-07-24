from django.contrib import admin
from .models import Articles
from .models import Users
from .models import Comments
from .models import likedAndDislike
# Register your models here.
admin.site.register(Articles)
admin.site.register(Users)
admin.site.register(Comments)
admin.site.register(likedAndDislike)