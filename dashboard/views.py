from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,DestroyAPIView
from main.models import *
from main.serializers import *


""" Start Room Crud """

class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

""" End Room Crud """

""" Start Student Crud """

class CreateStudent(ListCreateAPIView):
    queryset = Student.pbjects.all()
    serializer_class = StudentSerializer


class UpdateStudent(UpdateRoom):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

""" End student """

""" Start teacher Crud """

class CreateTeacher(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class UpdateTeacher(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class DeleteTeacher(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

""" End teacher Crud """

""" Start Course """

class CreateInfo(ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class UpdateInfo(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class DeleteInfo(DestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

""" End Info Crud """

""" Start employee Crud """

class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

""" End employee Crud """