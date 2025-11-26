from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    
    #create
    def create(self , validated_data):
        return Student.objects.create(**validated_data)

 #update
    def update(self , instance , validated_data):
        print(instance.name)#old name
        instance.name = validated_data.get('name' , instance.name)
        print(instance.name)#new name
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.city = validated_data.get('city' , instance.city)
        instance.save()
        return instance
    #no need of delete method as we are not using ModelViewset or GenericAPIView