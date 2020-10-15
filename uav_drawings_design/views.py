from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UAV_Drawings_Design_Type(TemplateView):
    template_name = 'uav_drawings_design/uav_drawings_design.html'


class UAV_Drawing_Issuance_Type(TemplateView):
    template_name = 'uav_drawings_design/uav_drawing_issuance_type.html'


class UAV_Drawings_Basic_Components(TemplateView):
    template_name = 'uav_drawings_design/uav_drawings_basic_components.html'


class UAV_Drawings_Base_Standardsn(TemplateView):
    template_name = 'uav_drawings_design/uav_drawings_base_standards.html'


class UAV_Drawings_Wiring_Numbers(TemplateView):
    template_name = 'uav_drawings_design/uav_drawings_wiring_numbers.html'


class UAV_Drawings_Wiring_Racks(TemplateView):
    template_name = 'uav_drawings_design/uav_drawings_wiring_racks.html'


class UAV_Schematics_Examples(TemplateView):
    template_name = 'uav_drawings_design/uav_schematics_examples.html'


class UAV_Cad_Base_Standards(TemplateView):
    template_name = 'uav_drawings_design/uav_cad_base_standards.html'


class UAV_Drawing_Package_Checklist(TemplateView):
    template_name = 'uav_drawings_design/uav_drawing_package_checklist.html'


class UAV_Design_Principles_Devices(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_devices.html'


class UAV_Design_Principles_Conduits(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_conduits.html'


class UAV_Design_Principles_Views(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_views.html'


class UAV_Design_Principles_Bgas(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_bgas.html'

class UAV_Design_Principles_Wire_Loss(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_wire_loss.html'

class UAV_Design_Principles_Wire_Loss_Watts(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_wire_loss_watts.html'


class UAV_Design_Principles_Wire_Loss_Ohms(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_wire_loss_ohms.html'

class UAV_Design_Principles_ohms_spkr_load_p(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_ohms_spkr_load_p.html'

class UAV_Design_Principles_ohms_spkr_load_s(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_ohms_spkr_load_s.html'

class UAV_Design_Principles_volts_spkr_load_p(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_volts_spkr_load_p.html'

class UAV_Design_Principles_btu_calc(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_btu_calc.html'

class UAV_Design_Principles_btu_speaker_coverage_c(TemplateView):
    template_name = 'uav_drawings_design/uav_design_principles_speaker_coverage_c.html'