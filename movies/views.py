from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Actor, Movie, Actor_Movie
import json

# Create your views here.

class MoviesView(View):
    def get(self,request):
        ac = Actor.objects.all()
        results=[]
        for a in ac:
            results.append(
                {
                    "first_name" : a.first_name,
                    "movies" : [i.title for i in a.movies.all()],                    
                }
            )
        return JsonResponse({"result":results}, status = 201)


class ActorView(View):
    def get(self,request):
        m = Movie.objects.all()
        results=[]
        for a in m:
            results.append(
                {
                    "title" : a.title,
                    "release_date" : a.release_date,
                    "running_time" : a.running_time,
                    "actor" : [i.last_name for i in a.actor_set.all()],                    
                }
            )
        return JsonResponse({"result":results}, status = 201)