from ast import literal_eval

import requests
from django.contrib import messages
from django.shortcuts import render, redirect

from blog.models import Movie


def home(request):
    return render(request, 'blog/post_movie.html')


def movie_detail(request):
    context = {}
    if request.method == 'POST':
        search = request.POST['search_movie'].title()
        data = Movie.objects.filter(title__icontains=search)
        if data:
            context = {
                'search': data
            }
        else:
            messages.warning(request, 'Movie not found!!')
            return redirect('movie:dd')

    return render(request, 'blog/search_movie.html', context)


def movie_post(request):
    if request.method == 'POST':
        title = request.POST['movie_title'].title()
        genre = request.POST['genre']
        director = request.POST['director']
        cast = request.POST['cast']

        val = requests.get('http://www.omdbapi.com/?s=' + title + '&apikey=514904fe')
        if val:
            movie = val.content.decode("utf-8")
            search = literal_eval(movie)
            search_list = search.get("Search")
            if search_list:
                year = ''
                poster_image = ''
                type_ = ''
                for search in search_list:
                    if search["Title"] == title:
                        poster_image = search.get('Poster')
                        year = search.get('Year')
                        type_ = search.get('Type')
                obj = Movie()
                obj.title = title
                obj.year = year
                obj.type = type_
                obj.image = poster_image
                obj.director = director
                obj.genre = genre
                obj.cast_member = cast
                if Movie.objects.filter(title=title):
                    messages.warning(request, "Movie Already Exist!!")
                    return redirect("movie:home")
                else:
                    obj.save()

                return redirect('movie:dd')
            else:
                messages.warning(request, 'Movie not found!!!')
                return redirect('movie:home')


def detail(request):
    obj = Movie.objects.all().order_by('-id')
    context = {
        'obj': obj
    }

    return render(request, 'blog/movie_detail.html', context)


def edit_view(request, id):
    movie = Movie.objects.get(id=id)
    context = {

        'movie': movie
    }
    return render(request, 'blog/edit.html', context)


def delete_view(request, id):
    movie = Movie.objects.filter(id=id)
    movie.delete()
    return redirect('movie:dd')


def edit_data(request, id):
    if request.method == 'POST':
        obj = Movie.objects.filter(id=id).first()
        if obj:
            title = request.POST['movie_title'].title()
            year = request.POST['year']
            type_ = request.POST['type']
            genre = request.POST['genre']
            director = request.POST['director']
            cast = request.POST['cast']

            val = requests.get('http://www.omdbapi.com/?s=' + title + '&apikey=514904fe')
            movie = val.content.decode("utf-8")
            search = literal_eval(movie)
            search_list = search.get("Search")
            poster_image = ""
            for search in search_list:
                if search["Title"] == title:
                    poster_image = search.get("Poster")
            obj.title = title
            obj.year = year
            obj.type = type_
            obj.image = poster_image
            obj.director = director
            obj.genre = genre
            obj.cast_member = cast
            obj.save()

        return redirect('movie:dd')
