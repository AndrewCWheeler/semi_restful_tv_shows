from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.new_show_form),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/edit', views.edit_show_form),
    path('shows/edit', views.edit_show),
    path('shows/<int:show_id>/destroy', views.delete_show),
]