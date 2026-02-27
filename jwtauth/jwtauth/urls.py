from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

#cretaing router object;
router = DefaultRouter()
#register StudentModelViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),#access + refresg tokens
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),#refresh access token
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'), #verify access token


]

#in terminal with httpie api calls test
#create token
#http POST http://127.0.0.1:8000/studentapi/ \
# name="Ali" roll=101 city="Mumbai" \
# Authorization:"Bearer your_access_token"


#read get token all
# http GET http://127.0.0.1:8000/studentapi/ \
# Authorization:"Bearer your_access_token"

#read get token single
# http GET http://127.0.0.1:8000/studentapi/ \
# Authorization:"Bearer your_access_token"

#update (put) token
# http PUT http://127.0.0.1:8000/studentapi/1/ \
# name="Ahmed" roll=102 city="Delhi" \
# Authorization:"Bearer your_access_token"

#delete token
# http DELETE http://127.0.0.1:8000/studentapi/1/ \
# Authorization:"Bearer your_access_token"
