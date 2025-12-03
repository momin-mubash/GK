from rest_framework import serializers
from .models import Student


#validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("name should starts with R")
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100 , validators=[starts_with_r])
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



    #field level validation
    def validate_roll(self , value):#method is inside the class so self is used
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    

    #object level validation
    def validate(Self , data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'chloe' and ct.lower() != 'colombia':
            raise serializers.ValidationError("city must be colombia")
        return data