from django.conf.urls import url, include
from rest_framework import routers, generics
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import UserViewSet, UserList, UserDetail
from posts import views
from django.contrib import admin
from intern.views import IndexView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'threads', views.ThreadViewSet)
router.register(r'boards', views.BoardViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/threads/$',
        views.ThreadList.as_view(),
        name='thread-list'),
    url(r'^api/threads/(?P<pk>[0-9]+)/$',
        views.ThreadDetail.as_view(),
        name='thread-detail'),
    url(r'^api/users/$',
        UserList.as_view(),
        name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$',
        UserDetail.as_view(),
        name='user-detail'),
    url(r'^api/boards/$',
        views.BoardList.as_view(),
        name='board-list'),
    url(r'^api/boards/(?P<pk>[0-9]+)/$',
        views.BoardDetail.as_view(),
        name='board-detail'),

    url(r'^.*$', IndexView.as_view(), name='index'),
]