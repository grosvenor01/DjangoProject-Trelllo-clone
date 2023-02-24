from .models import *
from django.http import HttpResponse,JsonResponse
from .serializer import *
from rest_framework.views import APIView 
from rest_framework import status
# Create your views here.
class user_API(APIView):
    def post(self , request ):
        serializer=user_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class empty_table_API(APIView):
    def post(self, request, pk ,format=None): #to create a empty table for a user 
        try:
            User=user.objects.get(id=pk)
            name=request.data['table_name']
            empty_table=table_list(table_name=name, user=User)
            empty_table.save()
            return HttpResponse("empty table created succefully")
        except user.DoesNotExist:
            return HttpResponse("user doesn't exist") 
    def get(self , request , pk ,format=None): #to get all user's tables
        lists=table_list.objects.filter(user=pk)
        serializer = table_serializer(lists,many=True)
        return JsonResponse(serializer.data,safe=False)
    def delete(self , request , pk , format=None):
        try:
            the_table=table_list.objects.get(id=pk)
            the_table.delete()
            serializer = table_serializer(the_table)
            return JsonResponse(data = serializer.data,safe=False , status=202)
        except table_list.DoesNotExist:
            return HttpResponse("query doesn't exist")            
class todolist_managingAPI(APIView):
    def post(self ,request , pk   ,format=None):
        try:
            table=table_list.objects.get(id=pk)
            table.todo.append(request.data['Element'])
            table.save()
            return HttpResponse("todo list added succefully")
        except table_list.DoesNotExist:
            return HttpResponse("table does not exist")
    def get(self , request,pk , format=None ):
        try : 
            table= table_list.objects.get(id=pk)
            return JsonResponse(data=table.todo, safe=False , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")
    def put(self , request, pk , format = None):
        try:
            table=table_list.objects.get(id=pk)
            table.todo = request.data['todo']
            table.save()
            serializer = table_serializer(table)
            return JsonResponse(serializer.data , safe =False  , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")
class InProgressList_managingAPI(APIView):
    def post(self ,request , pk   ,format=None):
        try:
            table=table_list.objects.get(id=pk)
            table.in_progress.append(request.data['Element'])
            table.save()
            return HttpResponse("in progress list Element added succefully")
        except table_list.DoesNotExist:
            return HttpResponse("table does not exist")
    def get(self , request,pk , format=None ):
        try : 
            table= table_list.objects.get(id=pk)
            return JsonResponse(data=table.in_progress, safe=False , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")
    def put(self , request, pk , format = None):
        try:
            table=table_list.objects.get(id=pk)
            table.in_progress = request.data['in_progress']
            table.save()
            serializer = table_serializer(table)
            return JsonResponse(serializer.data , safe =False  , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")
class DoneList_managingAPI(APIView):
    def post(self ,request , pk   ,format=None):
        try:
            table=table_list.objects.get(id=pk)
            table.done.append(request.data['Element'])
            table.save()
            return HttpResponse("done list Element added succefully")
        except table_list.DoesNotExist:
            return HttpResponse("table does not exist")
    def get(self , request,pk , format=None ):
        try : 
            table= table_list.objects.get(id=pk)
            return JsonResponse(data=table.done, safe=False , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")
    def put(self , request, pk , format = None):
        try:
            table=table_list.objects.get(id=pk)
            table.done = request.data['done']
            table.save()
            serializer = table_serializer(table)
            return JsonResponse(serializer.data , safe =False  , status = 200)
        except table_list.DoesNotExist :
            return HttpResponse("table does not exist")