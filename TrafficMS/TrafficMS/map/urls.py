from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns
    path('home', views.home_view, name='home_view'),
    path('map/', views.map_view, name='map_view'),
    path('api/map-data/', views.get_map_data, name='get_map_data'),
    path('reroute/', views.reroute_view, name='reroute_view'),
    path('api/routes-data/', views.get_routes_data, name='get_routes_data'),
]