from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#register StudentViewset with router
router.register('singers',views.SingerViewSet,basename='singers')
router.register('songs',views.SongViewSet,basename='songs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
