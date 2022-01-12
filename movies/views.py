import datetime

from .models import NewMovie
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    movies = NewMovie.objects.order_by('-Realese_Date').filter(Coming_Soon=False)
    featured_movies = NewMovie.objects.order_by('-Created_date').filter(Featured=True)
    top_rated = NewMovie.objects.order_by('Rating').reverse()
    home_toprated = top_rated.all()[:10]
    Bollywood_movies = NewMovie.objects.filter(Plot_keywords__icontains='Bollywood')
    home_Bollywood = Bollywood_movies.all()[:10]
    Coming_Soon_Movies = NewMovie.objects.filter(Coming_Soon=True).order_by('-Created_date').reverse()
    Movie_search = NewMovie.objects.filter(Movie_Name__contains='Movie_Name')
    if request.GET['Movie_Name']:
        Movie_Name = request.GET['Movie_Name']
        if Movie_Name:
            movies = movies.filter(Movie_Name__contains=Movie_Name)

    list = []
    for i in range(1,11):
        list.append(i)
        i+=1

    data = {
        'movies': movies,
        'featured_movies': featured_movies,
        'top_rated': top_rated,
        'Bollywood_movies': Bollywood_movies,
        'Coming_Soon_Movies': Coming_Soon_Movies,
        'home_toprated' : home_toprated,
        'home_Bollywood' : home_Bollywood,
        'Movie_search' : Movie_search,
    }
    return render(request, 'home.html', data)


def movie_details(request, id):
    movies = NewMovie.objects.order_by('-Created_date')
    movie_single = get_object_or_404(NewMovie, pk=id)
    mov = movie_single.genres.split()

    for m in mov:
        related_movie = NewMovie.objects.filter(genres__icontains=m)

    # paginator movie call
    paginator = Paginator(related_movie, 18)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    movie_num = int((paginator.count / 18) + 1)

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1

    movies_count = related_movie.count()

    data = {
        'movies': movies,
        'movie_single': movie_single,
        'related_movie': related_movie,
        'movie_num': list,
        'page_obj': page_obj,
        'movies_count': movies_count,

    }
    return render(request, 'movies/movie_details.html', data)


def Search(request):
    movies = NewMovie.objects.order_by('-Rating')
    if request.POST:
        if 'Movie_Name' in request.POST:
            Movie_Name = request.POST['Movie_Name']
            if Movie_Name:
                movies = movies.filter(Movie_Name__icontains=Movie_Name)
                m = Movie_Name

    data = {
        'movies': movies,
        'm': m,

    }
    return render(request, 'movies/search.html', data)

def movielist(request):
    movies = NewMovie.objects.order_by('-Rating')
    movies_count = movies.count()
    # paginator movie call
    paginator = Paginator(movies, 12)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # paggination count
    movie_num = int((paginator.count / 12) + 1)
    movie_search = NewMovie.objects.values_list('Movie_Name', flat=True).distinct()

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1

    data = {
        'movies': movies,
        'movie_search': movie_search,
        'movie_num': list,
        'movies_count': movies_count,
        'page_obj': page_obj,
        'paginator': paginator,

    }
    return render(request, 'nav_movie_files/movielist.html', data)


def newmovie(request):
    movies = NewMovie.objects.order_by('Realese_Date').reverse()
    # paginator movie call
    paginator = Paginator(movies, 18)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # paggination count
    movies_count = movies.count()
    movie_num = int((paginator.count / 18) + 1)

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1
    data = {
        'movies': movies,
        'movies_count': movies_count,
        'movie_num': list,
        'page_obj': page_obj,
    }
    return render(request, 'nav_movie_files/newmovie.html', data)


def upcoming(request):
    movies = NewMovie.objects.filter(Coming_Soon=True)
    # paginator movie call
    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # paggination count
    movies_count = movies.count()
    movie_num = int((paginator.count / 6) + 1)

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1
    data = {
        'movies': movies,
        'movies_count': movies_count,
        'movie_num': list,
        'page_obj': page_obj,
    }
    return render(request, 'nav_movie_files/upcoming.html', data)


def Bollywood(request):
    movies = NewMovie.objects.filter(Plot_keywords__icontains='Bollywood')
    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # paggination count
    movies_count = movies.count()
    movie_num = int((paginator.count / 6) + 1)

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1
    data = {
        'movies': movies,
        'movies_count': movies_count,
        'movie_num': list,
        'page_obj': page_obj,
    }
    return render(request, 'nav_movie_files/Bollywood.html', data)

def Hollywood(request):
    movies = NewMovie.objects.filter(Plot_keywords__icontains='Hollywood').order_by('-Realese_Date')

    paginator = Paginator(movies, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    # paggination count
    movies_count = movies.count()
    movie_num = int((paginator.count / 6) + 1)

    list = []
    for i in range(1, movie_num + 1):
        list.append(i)
        i += 1

    data = {
        'movies': movies,
        'movies_count': movies_count,
        'movie_num': list,
        'page_obj': page_obj,
    }
    return render(request, 'nav_movie_files/hollywood.html', data)
