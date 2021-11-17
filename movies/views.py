from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Actor, Movie, Actor_Movie
import json

# Create your views here.

class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        actor = Actor.objects.create(
            {
                "first_name" : data["first_name"],
                "last_name" : data["last_name"],
                "date_of_birth" : data["birth"]
        }
        )
        return JsonResponse({"result" : "CREATE"}, status = 201)



    def get(self,request):
        ac = Actor.objects.all()
        results=[]
        for a in ac:
            results.append(
                {
                    "first_name" : a.first_name,
                    "movies" : [i.title for i in a.movie.all()],                    
                }
            )
        return JsonResponse({"result":results}, status = 201)
