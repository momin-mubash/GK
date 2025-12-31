from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()#GET is by default
# def hello_world(request): 
#     return Response({"msg":"Hello World!"})



#post request
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#       print(request.data)
#       return Response({'msg':'This is a post request'})
    

#get and post together
@api_view(['GET' , 'POST'])
def hello_world(request):
    if request.method == "GET":
        print(request.query_params)
        return Response({'msg' : 'this is get request'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg' : 'this is post request'})
    