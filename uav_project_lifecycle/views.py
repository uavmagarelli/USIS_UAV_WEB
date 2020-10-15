from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UAV_Project_LifeCycle(TemplateView):
    template_name = 'uav_project_lifecycle/uav_project_lifecycle.html'


class UAV_PLC_Assignment(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_assignment.html'


class UAV_PLC_Bill_Of_Materials(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bill_of_materials.html'

class UAV_PLC_Bom_Audio(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_audio.html'

class UAV_PLC_Bom_Facilities(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_facilities.html'

class UAV_PLC_Bom_Video(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_video.html'

class UAV_PLC_Bom_Control(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_control.html'

class UAV_PLC_Bom_Network(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_network.html'

class UAV_PLC_Bom_Rack(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_bom_rack.html'


class UAV_PLC_Drawings(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_drawings.html'


class UAV_PLC_Supporting_Docs(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_supporting_docs.html'


class UAV_PLC_Build_Support(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_build_support.html'


class UAV_PLC_Close_Out(TemplateView):
    template_name = 'uav_project_lifecycle/uav_plc_close_out.html'
