from django.urls import path
from . import views


urlpatterns = [
    path('uav_project_lifecycle/', views.UAV_Project_LifeCycle.as_view(), name='uav_project_lifecycle'),
    path('uav_plc_assignment/', views.UAV_PLC_Assignment.as_view(), name='uav_plc_assignment'),
    path('uav_plc_bill_of_materials/', views.UAV_PLC_Bill_Of_Materials.as_view(), name='uav_plc_bill_of_materials'),
    path('uav_plc_bom_audio/', views.UAV_PLC_Bom_Audio.as_view(), name='uav_plc_bom_audio'),
    path('uav_plc_bom_facilities/', views.UAV_PLC_Bom_Facilities.as_view(), name='uav_plc_bom_facilities'),
    path('uav_plc_bom_video/', views.UAV_PLC_Bom_Video.as_view(), name='uav_plc_bom_video'),
    path('uav_plc_bom_control/', views.UAV_PLC_Bom_Control.as_view(), name='uav_plc_bom_control'),
    path('uav_plc_bom_network/', views.UAV_PLC_Bom_Network.as_view(), name='uav_plc_bom_network'),
    path('uav_plc_bom_rack/', views.UAV_PLC_Bom_Rack.as_view(), name='uav_plc_bom_rack'),
    path('uav_plc_drawings/', views.UAV_PLC_Drawings.as_view(), name='uav_plc_drawings'),
    path('uav_plc_supporting_docs/', views.UAV_PLC_Supporting_Docs.as_view(), name='uav_plc_supporting_docs'),
    path('uav_plc_build_support', views.UAV_PLC_Build_Support.as_view(), name='uav_plc_build_support'),
    path('uav_plc_close_out', views.UAV_PLC_Close_Out.as_view(), name='uav_plc_close_out'),
    ]