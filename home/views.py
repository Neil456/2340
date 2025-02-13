from movies.models import Movie

from django.shortcuts import render



def index(request):
    movies = Movie.objects.order_by('-id')[:4] 
    template_data = {
        'title': 'GT Movies Store',
        'movies': movies  # Pass movies to the template
    }

    print(template_data)


    return render(request, 'home/index.html', template_data)


def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request,
                  'home/about.html',
                  {'template_data': template_data})