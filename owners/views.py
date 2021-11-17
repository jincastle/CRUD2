from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Owner, Dog
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
            request.append(
                {
                    "name" : owners.name,
                    "email" : owners.email,
                    "age" : owners.age,
                    "dog_name" : list(owners.dog_set.values('name'))
                }
            )
        return JsonResponse({"result" : "CREATE"}, status = 201)

        

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
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name,
                }
            )
        return JsonResponse({"result" : results}, status = 201)



