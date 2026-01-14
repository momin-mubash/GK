from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



#READ - pk not required
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
#CREATE - pk not required
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self ,request , *args , **kwargs):
        return self.create(request,*args,**kwargs)
    
#RETRIEVE - pk required
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self ,request , *args , **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
#UPDATE - pk required
class StudentUpdate(GenericAPIView,UpdateModelMixin,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self , request ,*args ,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self ,request , *args , **kwargs):
        return self.update(request,*args,**kwargs)
    
#DELETE - pk required
class StudentDestroy(GenericAPIView,DestroyModelMixin,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self , request ,*args ,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def delete(self ,request , *args , **kwargs):
        return self.destroy(request,*args,**kwargs)