from django.urls import path
from .views import home_view,about_view,warmup_view,workout_list
app_name = 'core'



urlpatterns = [
    path('',home_view.as_view(),name='home'),
    path('about/',about_view.as_view(),name='about'),
    path('workouts/warmup',warmup_view.as_view(),name='warmup'),
    path('workouts/',workout_list.as_view(),name='workouts'),
]