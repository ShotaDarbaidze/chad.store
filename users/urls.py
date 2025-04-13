from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, RegisterViewSet,ProfileViewSet

router=DefaultRouter()
router.register('users',UserViewSet,basename='user')
router.register('register',RegisterViewSet,basename='user-registration')

urlpatterns = [
    path('users/me/',ProfileViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
    path('', include(router.urls))
]