from django.conf.urls import url, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'users', views.UserCreateViewSet)
router.register(r'articles', views.ListUserArticleViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^articles/(?P<pk>\d+)/comments$', views.CommentList.as_view(), name='CommentList'),
    url(r'^users/(?P<pk>\d+)/articles$', views.UserArticleList.as_view(), name='UserArticleList'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]

