from django.urls import path
from main import views

urlpatterns = [
    path('college/<int:pk>', views.CollegeDetail.as_view()),
    path('college_create', views.CollegeCreate.as_view()),
    path('college_update/<int:pk>', views.CollegeUpdate.as_view()),
    path('college_delete/<int:pk>', views.CollegeDelete.as_view()),
    path('', views.index)
]