from django.urls import path
from . import views
urlpatterns=[
        path('',views.all_pets),
        path('<int:pet_id>/',views.pet_details),
 ]
