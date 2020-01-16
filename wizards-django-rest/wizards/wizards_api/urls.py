from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('wizards/', views.WizardList.as_view()),
    path('wizard/<int:pk>', views.WizardDetail.as_view()),
    path('houses/', views.HouseList.as_view()),
    path('house/<int:pk>', views.HouseDetail.as_view()),
    path('founders/', views.FounderList.as_view()),
    path('founder/<int:pk>', views.FounderDetail.as_view()),
    path('subjects/', views.SubjectList.as_view()),
    path('subject/<int:pk>', views.SubjectDetail.as_view()),
    path('spells/', views.SpellList.as_view()),
    path('spell/<int:pk>', views.SpellDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)