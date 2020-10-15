from django.urls import path
from . import views


urlpatterns = [
    path('uav_project_basics/', views.UAV_Project_Basics.as_view(), name='uav_project_basics'),
    path('uav_basic_project_docs/', views.UAV_Project_Basic_Docs.as_view(), name='uav_basic_project_docs'),
    path('uav_project_starting_point/', views.UAV_Project_Starting_Point.as_view(), name='uav_project_starting_point'),
    path('uav_project_work_flow/', views.UAV_Project_Work_flow.as_view(), name='uav_project_work_flow'),
    path('uav_note_about_travel/', views.UAV_Note_About_Travel.as_view(), name='uav_note_about_travel'),
    ]