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
                    "movies" : [i.title for i in a.Actor_Movie.all()]                    
                }
            )
        return JsonResponse({"result":results}, status = 201)
