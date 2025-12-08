from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("name should starts with r")
    name = serializers.CharField(validators=[start_with_r])#for validators
    #name = serializers.CharField(read_only = True)#user cant change this field while updating
    #the above line can be used within the class Meta too with read_only_fields attribute
    class Meta:
        model = Student
        fields = ['id' , 'name' , 'roll' , 'city']
#youll get all the fields mentioned ,create and update method automatically by modelserializer
        #read_only_fields = ['name']
#or you can use this below one
        #extra_kwargs = {'name':{'read_only':True}}  


#field level validation
    def validate_roll(self , value):
        if value >= 200 :
            raise serializers.ValidationError("seat full")
        return value
    

#object level validation
    def validate(self , data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'reshma' and ct.lower () != 'bombay':
            raise serializers.ValidationError("Reshma lives in Bombay")
        return data
    




