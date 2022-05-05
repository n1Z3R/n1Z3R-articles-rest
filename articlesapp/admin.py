from django.contrib import admin

# Register your models here.
from articlesapp.models import *

admin.site.register(ArticlesModel)
admin.site.register(ArticlesLikesModel)
admin.site.register(ArticlesCommentsModel)
