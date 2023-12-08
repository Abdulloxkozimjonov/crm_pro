from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

""" Get room all """

@api_view(["GET"])
def room_view(request):
    room = models.Room.objects.all()
    ser = serializers.RoomSerializer(room, many=True)
    return Response(ser.data)

""" End room all """

""" Start student all """

@api_view(["GET"])
def student_view(request):
    student = models.Student.objects.all()
    ser = serializers.StudentSerializer(student, many=True)
    return Response(ser.data)

""" End student all """

""" Start teacher all """

@api_view(["GET"])
def teacher_view(request):
    teacher = models.Teacher.objects.all()
    ser = serializers.TeacherSerializer(teacher, many=True)
    return Response(ser.data)

""" End teacher all """

""" Start Info all """

@api_view(["GET"])
def info_view(request):
    info = models.Info.objects.all()
    ser = serializers.InfoSerializer(info, many=True)
    return Response(ser.data)


""" End info all """

""" Start employee all """

@api_view(["GET"])
def employee(request):
    employee = models.Employee.objects.all()
    ser = serializers.EmployeeSerializer(employee, many=True)
    return Response(ser.data)

""" End employee all """

""" Filter """

""" Start student by name """

@api_view(["GET"])
def student_by_name(request):
    name = models.Student.objects.GET.get(name)
    student = models.Student.objects.filter(name = name)
    ser = serializers.StudentSerializer(student)
    return Response(ser.data)

""" End student by name """

""" Start studen by phone_number """

@api_view(["GET"])
def studen_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    student = models.Student.objects.filter(phone_number = phone_number)
    ser = serializers.StudentSerializer(student)
    return Response(ser.data)

""" End studen by phone_number """

""" Start teacher by name """

@api_view(["GET"])
def teacher_by_name(request):
    name = request.GET.get("name")
    teacher = models.Teacher.objects.filter(name = name)
    ser = serializers.TeacherSerializer(teacher)
    return Response(ser.data)

""" End teacher by name """

""" Start teacher_by_subject """

@api_view(["GET"])
def teacher_by_subject(request):
    subject = request.GET.get("subject")
    teacher = models.Teacher.objects.filter()
    ser = serializers.TeacherSerializer(teacher = subject)
    return Response(ser.data)

""" End teacher_by_subject """

""" Start teacher_by_salary """

@api_view(['GET'])
def teacher_by_salary(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    salary = models.Teacher.objects.filter(price__gte = start_price, price__lte = end_price)
    ser = serializers.TeacherSerializer(salary)
    return Response(ser.data)

""" End teacher_by_salary """

""" Start room_by_group """

@api_view(["GET"])
def room_by_group(request):
    group = request.GET.get("group")
    teacher = models.Teacher.objects.filter(group = group)
    ser = serializers.TeacherSerializer(teacher)
    return Response(ser.data)

""" End room_by_group """

""" Start Employ_by_name """

@api_view(["GET"])
def Employ_by_name(request):
    name = request.GET.get("name")
    employee = models.Employee.objects.filter(name = name)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)

""" End Employ_by_name """

""" Start Employ_by_status """

@api_view(["GET"])
def Employ_by_status(request):
    status = request.GET.get("status")
    employee = models.Employee.objects.filter(status = status)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)

""" End Employ_by_status """

