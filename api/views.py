from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer,StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
"""
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

#all student(queryset)
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


#get data and add it in student database(deserializer)
import io
from rest_framework.parsers import JSONParser
#to bypass csrf token
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serrializer = StudentSerializer(data = parsed_data)
        if serrializer.is_valid():
            serrializer.save()
            #give response
            res = {'msg':'Data Saved!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serrializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')


#to get data and update field by that
@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        serializer = StudentSerializer(stu, data = parsed_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            #give response
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')



#to get data and delete by that
@csrf_exempt
def student_delete(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        stu.delete()
        #give response
        res = {'msg':'Data deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')
"""



"""
Using ModelSerializer

"""

"""
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentModelSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

#all student(queryset)
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentModelSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


#get data and add it in student database(deserializer)
import io
from rest_framework.parsers import JSONParser
#to bypass csrf token
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serrializer = StudentModelSerializer(data = parsed_data)
        if serrializer.is_valid():
            serrializer.save()
            #give response
            res = {'msg':'Data Saved!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serrializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')


#to get data and update field by that
@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        serializer = StudentModelSerializer(stu, data = parsed_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            #give response
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')



#to get data and delete by that
@csrf_exempt
def student_delete(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        stu.delete()
        #give response
        res = {'msg':'Data deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')

"""



"""
using api_view
by data our api can be browserable
easy tu check(don't need to make any 3rd party app)
and it take less code
"""
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def hello(request):
    if request.method == 'GET':
        return Response({'print':'helloworld'})

    if request.method == 'POST':
        print(request.data)
        return Response({'data':request.data, 'print':'helloworld POST'})


@api_view()
def student_detail(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentModelSerializer(stu, many = True)
        return Response(serializer.data)


import io
from rest_framework.parsers import JSONParser
#to bypass csrf token
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serrializer = StudentModelSerializer(data = parsed_data)
        if serrializer.is_valid():
            serrializer.save()
            #give response
            res = {'msg':'Data Saved!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serrializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')


#to get data and update field by that
@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        serializer = StudentModelSerializer(stu, data = parsed_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            #give response
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')



#to get data and delete by that
@csrf_exempt
def student_delete(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        stu = Student.objects.get(name = parsed_data.get('name'))
        stu.delete()
        #give response
        res = {'msg':'Data deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')