from django.urls import path
from . import views

urlpatterns = [
    path('wizards/', views.wizards_list),
    path('wizard/<int:pk>', views.wizard_detail),
    path('houses/', views.house_list),
    path('house/<int:pk>', views.house_detail),
]