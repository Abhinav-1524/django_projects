
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views import generic

def index(request):
    return HttpResponse("hello,world,you're at the cineinfo!...")
    
from cinebot.models import Movie

key='cdb50ba3'

def get_movie_info(request):
    global movies_info
    movies_info = {}
    movies_list=[]
    
    if 'name' in request.GET:
        name = request.GET['name']
        url = f"http://www.omdbapi.com/?apikey={key}&t={name}"
        response = requests.get(url)    
        data = response.json()
        movies_list=data

        for i in movies_list:
                movie_data = Movie(
                Title = data["Title"],
                Director=data["Director"],
                Year=data["Year"],
                Rating = data["imdbRating"],
                poster=data['Poster'],)
                movie_data.save()
                movies_info = Movie.objects.all().order_by('-id')

    return render (request, 'cineinfo/movie.html', { "movies_info": movies_info})


def movie_display(request):
    movie = Movie.objects.get(id=id)
    print(movie)
    return render (
        request,
        'cineinfo/movie_display.html',
        {'movie': movie}
    )


