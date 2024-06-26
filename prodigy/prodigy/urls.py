
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from countries.views import CountriesViewSet

router = DefaultRouter()
router.register(r'countries', CountriesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include(router.urls)),
]