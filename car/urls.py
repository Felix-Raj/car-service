from rest_framework.routers import DefaultRouter

from car import views

app_name = 'car'
router = DefaultRouter(trailing_slash=False)
router.register('manufacturer', views.ManufacturerViewSet)
router.register('car-model', views.CarModelViewSet)
router.register('car', views.CarViewSet)
urlpatterns = router.urls
