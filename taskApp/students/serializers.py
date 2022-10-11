from rest_framework import serializers
from taskApp.students.models import Student, Course, StudentStatus


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    status = serializers.CharField()

    def get_status(self, obj):
        return obj.status.name

    def validate_status(self, value):
        if value not in ['ft', 'pt']:
            raise serializers.ValidationError("Not valid")
        return value

    def create(self, validated_data):
        status = StudentStatus.objects.create(name=validated_data.get('status'))
        validated_data['status'] = status
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.status.name = validated_data.get('status')
        instance.status.save()
        validated_data['status'] = instance.status
        instance = super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['status'] = instance.status.name
        return ret


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'