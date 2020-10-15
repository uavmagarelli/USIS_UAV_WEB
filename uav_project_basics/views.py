from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UAV_Project_Basics(TemplateView):
    template_name = 'uav_project_basics/uav_project_basics.html'


class UAV_Project_Basic_Docs(TemplateView):
    template_name = 'uav_project_basics/uav_basic_project_docs.html'


class UAV_Project_Starting_Point(TemplateView):
    template_name = 'uav_project_basics/uav_project_starting_point.html'


class UAV_Project_Work_flow(TemplateView):
    template_name = 'uav_project_basics/uav_project_work_flow.html'


class UAV_Note_About_Travel(TemplateView):
    template_name = 'uav_project_basics/uav_note_about_travel.html'
