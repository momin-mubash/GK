from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from api.throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,JackRateThrottle]
    
#scopedRateThrottle is used to set different rate for different views
#you just need to define throttle_classes=[ScopedRateThrottle] and then in settings.py file you need to set the rate for that scope like this
# 'list': '5/day' and in that view throttle_scope='list' and for another view you can set throttle_scope='create' and in settings.py file you can set 'create': '10/day' like this you can set different rate for different views
