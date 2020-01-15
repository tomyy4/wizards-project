from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('wizards/', views.WizardList.as_view()),
    path('wizard/<int:pk>', views.WizardDetail.as_view()),
    path('houses/', views.HouseList.as_view()),
    path('house/<int:pk>', views.HouseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)