from django.db import models


class StudentStatus(models.Model):
  name = models.CharField(max_length=100)


class Student(models.Model):
  index_number = models.CharField(max_length=100)
  status = models.OneToOneField(
    StudentStatus,
    on_delete=models.CASCADE,
  )
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)
  year = models.CharField(max_length=100, blank=True)


class Course(models.Model):
  name = models.CharField(max_length=100)
  students = models.ManyToManyField(Student, related_name="courses", blank=True)