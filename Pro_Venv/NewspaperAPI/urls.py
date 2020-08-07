
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, NewspaperViewSet, ConsumerViewSet,IntakeViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('newspaper', NewspaperViewSet)
router.register('consumer', ConsumerViewSet)
router.register('intake', IntakeViewSet)

urlpatterns = [
    path('',include(router.urls))
]
