from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from articlesapp.views import *

router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'myarticles', MyArticlesViewSet, basename='MyArticles')
router.register(r'comments', ArticlesCommentsViewSet)
router.register(r'likes', ArticlesLikesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/register/', CreateUserView.as_view())
]
