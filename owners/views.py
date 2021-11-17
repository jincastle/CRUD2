from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Owner, Dog
#json file -> python file
import json

# Create your views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name=data["owner"],
            email=data["email"],
            age=data["age"]
        )
        return JsonResponse({"result" : "CREATE"}, status=201)


    def get(self, request):
        owner = Owner.objects.all()
        requests = []
        for owners in owner:
            requests.append(
                {
                    "name" : owners.name,
                    "email" : owners.email,
                    "age" : owners.age,
                    "dog_name" : list(owners.dog_set.values('name'))       
                }
            )

        return JsonResponse({"result" : requests}, status = 201)

        

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data["owner"])
        dog = Dog.objects.create(
            owner = owner,
            name = data["dog"],
            age=data["age"]
        )
        return JsonResponse({"result" : "CREATE"}, status = 201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {   
                    "id" : dog.id,
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }
            )
        return JsonResponse({"result" : results}, status = 201)

# 정참조 없이 구현 
# for dog in dogs:
#     owner = Owner.objects.get(dog__id=dog.id)
#     results.append({
#         "id" : dog.id,
#         "name" : dog.name,
#         "age" : dog.age,
#         "owner" : {
#             "id" : owner.id,
#             "name" : owner.name,
#         }
#     })


# for owner in owners:
#     dogs = Dog.objects.filter(owner_id = owner.id)
#     dog_list = []


# class MoviesView(View):
#     def get(self,request):
#         ac = Actor.objects.all()
#         results=[]
#         for a in ac:
#             results.append(
#                 {
#                     "first_name" : a.first_name,
#                     "movies" : [i.title for i in a.movies.all()]                    
#                 }
#             )
#         return JsonResponse({"result":results}, status = 201)
