from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from taskApp.students.models import Student, Course
from taskApp.students.serializers import StudentSerializer, CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  @action(detail=True, methods=['get'])
  def courses(self, request, pk=None):
    student = self.get_object()
    serializer = CourseSerializer(student.courses, many=True)
    return Response(serializer.data)


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  @action(detail=True, methods=['get'])
  def students(self, request, pk=None):
    course = self.get_object()
    serializer = StudentSerializer(course.students, many=True)
    return Response(serializer.data)

