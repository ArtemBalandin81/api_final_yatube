from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register(r'follow', FollowViewSet, basename='follow')
app_name = 'api'
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/jwt/', include('djoser.urls')), # управление пользователями
    path('v1/', include('djoser.urls.jwt')),
]
