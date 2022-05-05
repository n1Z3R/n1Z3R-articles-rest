from django.contrib.auth import get_user_model
from rest_framework import mixins, filters
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from articlesapp.permissions import IsOwnerOrAuthenticatedOrReadOnly
from articlesapp.serializers import ArticlesSerializer, ArticlesCommentsSerializer, ArticlesLikesSerializer, \
    UserSerializer
from articlesapp.models import ArticlesModel, ArticlesCommentsModel, ArticlesLikesModel
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class CommonArticlesViewSet:
    '''This viewset helps to integrate common properties'''
    search_fields = ['name', 'content']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ArticlesSerializer


class ArticlesViewSet(CommonArticlesViewSet, ModelViewSet):
    '''This viewset works with all articles_django'''
    queryset = ArticlesModel.objects.all()
    permission_classes = [IsOwnerOrAuthenticatedOrReadOnly]


class MyArticlesViewSet(CommonArticlesViewSet, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    '''This viewset works with my articles_django'''
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ArticlesModel.objects.filter(user=self.request.user)


class ArticlesCommentsViewSet(mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              GenericViewSet):
    '''This viewset works with comments of articles_django'''
    queryset = ArticlesCommentsModel.objects.all()
    serializer_class = ArticlesCommentsSerializer
    permission_classes = [IsOwnerOrAuthenticatedOrReadOnly]


class ArticlesLikesViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    '''This viewset works with likes of articles_django'''
    queryset = ArticlesLikesModel.objects.all()
    serializer_class = ArticlesLikesSerializer
    permission_classes = [IsOwnerOrAuthenticatedOrReadOnly]
