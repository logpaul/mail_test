from rest_framework import  generics, viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from main.serializers import UserSerializer, ArticleSerializer, CommentSerializer
from main.models import *

# =============================================================================
# Users
# =============================================================================


class UserCreateViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserArticleList(generics.ListAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super(UserArticleList, self).get_queryset()
        return queryset.filter(user_creator__pk=self.kwargs.get('pk'))

# =============================================================================
# Articles
# =============================================================================


class ArticleFilter(django_filters.FilterSet):
    date_add = django_filters.DateFromToRangeFilter()
    # Вот так можно сделать для user_creator
    user_creator = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    title = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'user_creator', 'date_add', 'tags']


class ListUserArticleViewSet(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = ArticleFilter
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    ordering_fields = ('date_add',)
    ordering = ('date_add',)

    class Meta:
        model = Article
        fields = ('user_creator', 'blocked_users', 'title', 'text', 'date_add', 'tags')


# =============================================================================
# Comments
# =============================================================================


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentList(generics.ListAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('date_add',)
    ordering = ('date_add',)

    def get_queryset(self):
        queryset = super(CommentList, self).get_queryset()
        return queryset.filter(article__pk=self.kwargs.get('pk'))
