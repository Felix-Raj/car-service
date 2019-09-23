from rest_framework.routers import DefaultRouter

from customer import views

router = DefaultRouter(trailing_slash=False)
router.register('customer', views.CustomerViewSet)
urlpatterns = router.urls
