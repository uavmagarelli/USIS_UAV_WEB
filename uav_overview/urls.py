from django.urls import path
from . import views

urlpatterns = [
    path('uav_about_the_company/', views.UAV_About_The_Company.as_view(), name='uav_about_the_company'),
    path('uav_about_this_website/', views.UAV_About_This_Website.as_view(), name='uav_about_this_website'),
    path('uav_basics_team_rolls/', views.UAV_Basics_Team_Rolls.as_view(), name='uav_basics_team_rolls'),
    path('uav_engineering_drive/', views.UAV_Engineering_Drive.as_view(), name='uav_engineering_drive'),
    path('uav_overview/', views.UAV_Overview.as_view(), name='uav_overview'),
    path('uav_procurement/', views.UAV_Procurement.as_view(), name='uav_procurement'),
    path('uav_project_folders/', views.UAV_project_Folder.as_view(), name='uav_project_folders'),
    path('uav_projectengineer_educational_path/', views.UAV_ProjectEngineer_Educational_Path.as_view(), name='uav_projectengineer_educational_path'),
    path('uav_projectengineer_job_description/', views.UAV_ProjectEngineer_Job_Description.as_view(), name='uav_projectengineer_job_description'),
    path('uav_server_drive/', views.UAV_Server_Drive.as_view(), name='uav_server_drive'),
    path('uav_team/', views.UAV_Team.as_view(), name='uav_team'),
    path('uav_wiki_page/', views.UAV_Wiki_Page.as_view(), name='uav_wiki_page'),
]
