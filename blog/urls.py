from django.urls import path

from blog.views import (
    home, movie_detail,
    movie_post, detail,
    delete_view, edit_view,
    edit_data
    # link_movie
)

app_name = 'movie'

urlpatterns = [
    path('', detail, name='dd'),
    path('detail/', movie_detail, name='movie_detail'),
    path('post_movie/', movie_post, name='post_movie'),
    path('post/', home, name='home'),
    path('add/movies/', movie_post, name='movie_post'),
    path('delete/<int:id>/', delete_view, name='delete'),
    path('edit/<int:id>/', edit_view, name='edit'),
    path('edit/data/<int:id>/', edit_data, name='edit_data'),

    # path('link/<str:title>/', link_movie, name='link'),

]
