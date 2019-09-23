from rest_framework.routers import DefaultRouter

from booking import views

app_name = 'booking'
router = DefaultRouter(trailing_slash=False)
router.register('mechanic', views.MechanicViewSet)
router.register('booking', views.BookingViewSet, basename='booking')
urlpatterns = router.urls
