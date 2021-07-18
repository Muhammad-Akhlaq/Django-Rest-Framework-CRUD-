from rest_framework import serializers
from .models import Student

#validator
#data is a python dictionary
def start_with(value):
    if value[0].lower() != 'A' or value[0].lower() != 'M':
        raise serializers.ValidationError('name must start with A or M')
    return value

class StudentSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100, validators = [start_with])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    #to add new student detail 
    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    #to update student details
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance

    #Field label validation
    #it will automatic run when we call .is_valid() in views
    #structure "validate_fieldname"
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value

    #object level validation
    #data is a python dictionary
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'Akhlaq' and ct.lower() != 'sialkot':
            raise serializers.ValidationError('city must be sialkot')
        return data
    

#Model-Serializer(auto field generation,default create and update)
class StudentModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [start_with])
    class Meta:
        model = Student
        fields = '__all__'
        #custom fiels
        #fields = ['id','name','roll']
        #read_only_field(lock that field so no one can change it)
        #read_only_fields = ['name','city']


    """
    same as in simple serializer

    """
    #Field label validation
    #it will automatic run when we call .is_valid() in views
    #structure "validate_fieldname"
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value

    #object level validation
    #data is a python dictionary
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'Akhlaq' and ct.lower() != 'sialkot':
            raise serializers.ValidationError('city must be sialkot')
        return data
