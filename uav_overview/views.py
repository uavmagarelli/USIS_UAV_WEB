from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class UAV_About_The_Company(TemplateView):
    template_name = 'uav_overview/uav_about_the_company.html'

class UAV_About_This_Website(TemplateView):
    template_name = 'uav_overview/uav_about_this_website.html'

class UAV_Basics_Team_Rolls(TemplateView):
    template_name = 'uav_overview/uav_basics_team_rolls.html'

class UAV_Engineering_Drive(TemplateView):
    template_name = 'uav_overview/uav_engineering_drive.html'

class UAV_Overview(TemplateView):
    template_name = 'uav_overview/uav_overview.html'

class UAV_Procurement(TemplateView):
    template_name = 'uav_overview/uav_procurement.html'

class UAV_project_Folder(TemplateView):
    template_name = 'uav_overview/uav_project_folders.html'

class UAV_ProjectEngineer_Educational_Path(TemplateView):
    template_name = 'uav_overview/uav_projectengineer_educational_path.html'

class UAV_ProjectEngineer_Job_Description(TemplateView):
    template_name = 'uav_overview/uav_projectengineer_job_description.html'

class UAV_Server_Drive(TemplateView):
    template_name = 'uav_overview/uav_server_drive.html'

class UAV_Team(TemplateView):
    template_name = 'uav_overview/uav_team.html'

class UAV_Wiki_Page(TemplateView):
    template_name = 'uav_overview/uav_wiki_page.html'
