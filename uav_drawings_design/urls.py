from django.urls import path
from . import views


urlpatterns = [
    path('uav_drawings_design/', views.UAV_Drawings_Design_Type.as_view(), name='uav_drawings_design'),
    path('uav_drawing_issuance_type/', views.UAV_Drawing_Issuance_Type.as_view(), name='uav_drawing_issuance_type'),
    path('uav_drawings_basic_components/', views.UAV_Drawings_Basic_Components.as_view(), name='uav_drawings_basic_components'),
    path('uav_drawings_base_standards', views.UAV_Drawings_Base_Standardsn.as_view(), name='uav_drawings_base_standards'),
    path('uav_drawings_wiring_numbers', views.UAV_Drawings_Wiring_Numbers.as_view(), name='uav_drawings_wiring_numbers'),
    path('uav_drawings_wiring_racks', views.UAV_Drawings_Wiring_Racks.as_view(), name='uav_drawings_wiring_racks'),
    path('uav_schematics_examples/', views.UAV_Schematics_Examples.as_view(), name='uav_schematics_examples'),
    path('uav_cad_base_standards/', views.UAV_Cad_Base_Standards.as_view(), name='uav_cad_base_standards'),
    path('uav_drawing_package_checklist/', views.UAV_Drawing_Package_Checklist.as_view(), name='uav_drawing_package_checklist'),
    path('uav_design_principles_devices/', views.UAV_Design_Principles_Devices.as_view(), name='uav_design_principles_devices'),
    path('uav_design_principles_conduits/', views.UAV_Design_Principles_Conduits.as_view(), name='uav_design_principles_conduits'),
    path('uav_design_principles_views/', views.UAV_Design_Principles_Views.as_view(), name='uav_design_principles_views'),
    path('uav_design_principles_bgas/', views.UAV_Design_Principles_Bgas.as_view(), name='uav_design_principles_bgas'),
    path('uav_design_principles_wire_loss/', views.UAV_Design_Principles_Wire_Loss.as_view(), name='uav_design_principles_wire_loss'),
    path('uav_design_principles_wire_loss_watts/', views.UAV_Design_Principles_Wire_Loss_Watts.as_view(), name='uav_design_principles_wire_loss_watts'),
    path('uav_design_principles_wire_loss_ohms/', views.UAV_Design_Principles_Wire_Loss_Ohms.as_view(), name='uav_design_principles_wire_loss_ohms'),
    path('uav_design_principles_ohms_spkr_load_p/', views.UAV_Design_Principles_ohms_spkr_load_p.as_view(), name='uav_design_principles_ohms_spkr_load_p'),
    path('uav_design_principles_ohms_spkr_load_s/', views.UAV_Design_Principles_ohms_spkr_load_s.as_view(), name='uav_design_principles_ohms_spkr_load_s'),
    path('uav_design_principles_volts_spkr_load_p/', views.UAV_Design_Principles_volts_spkr_load_p.as_view(), name='uav_design_principles_volts_spkr_load_p'),
    path('uav_design_principles_btu_calc/', views.UAV_Design_Principles_btu_calc.as_view(), name='uav_design_principles_btu_calc'),
    path('uav_design_principles_speaker_coverage_c/', views.UAV_Design_Principles_btu_speaker_coverage_c.as_view(), name='uav_design_principles_speaker_coverage_c'),
    ]