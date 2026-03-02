from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
# from api.auth import CustomAuthToken


#cretaing router object
router = DefaultRouter()
#register StudentModelViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/' , include('rest_framework.urls',namespace='rest_framework'))

    # path('getoken/',obtain_auth_token),#user hit the url gettoken/ with username and password to get token(httpie)
    # path('gettoken/',CustomAuthToken.as_view()),#to get custom response here token,id and email

]