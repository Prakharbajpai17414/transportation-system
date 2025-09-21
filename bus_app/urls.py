from django.urls import path
from django.shortcuts import render

from . import views
from .views import get_programs, get_stoppages ,submit_student, success_page, get_routes, register_student, get_schools

urlpatterns = [
    path('', views.home, name='home'),
    path('bus/<str:bus_number>/', views.bus_seating_chart, name='bus_seating_chart'),
    path('seat-details/<int:seat_id>/', views.get_seat_details, name='seat_details'),
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('allot_bus/<int:student_id>/', views.allot_bus, name='allot_bus'),
    path('select_seat/<int:student_id>/<int:bus_id>/', views.select_seat, name='select_seat'),
    path('assign_seat/<int:student_id>/<int:bus_id>/<int:seat_number>/', views.assign_seat, name='assign_seat'),

    # ✅ **Driver Management URLs**
    path('drivers/', views.driver_list, name='driver_list'),
    path('add-driver/', views.add_driver, name='add_driver'),
    path('edit-driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),

    # ✅ **Dynamic Filtering (AJAX Requests)**
    path("admin/get_stoppages/", get_stoppages, name="admin_get_stoppages"),
    path("submit-student/", submit_student, name="submit_student"),
    path("student-form/", submit_student, name="student_form"),
    path("success/", success_page, name="success_page"),
    path("get-programs/", get_programs, name="get_programs"),
    path("get-stoppages/", get_stoppages, name="get_stoppages"),
    path('api/get-schools/', get_schools, name='get_schools'),
    path('api/get-programs/', get_programs, name='get_programs'),
    path('api/get-routes/', get_routes, name='get_routes'),
    path('api/get-stoppages/', get_stoppages, name='get_stoppages'),
    path('api/register-student/', register_student, name='register_student'),
    path('success-page/', lambda request: render(request, 'success.html'), name='success_page'),

    path('buses/', views.bus_list, name='bus_list'),
    path('<str:number>/bus_detail', views.bus_detail, name='bus_detail'),  #BUS DETAILS URL

    path('buses/add/', views.add_bus, name='add_bus'),  #add bus url

    path('allotments/', views.allotment_list, name='allotment_list'), #for allotment list

    path('allotments/add/', views.add_allotment, name='add_allotment'), #add allotment
    path('ajax/get-stoppages/', views.get_stoppages_by_route, name='get_stoppages_by_route'), #ajax url for route-stopage filtering 
    path('drivers/', views.driver_list, name='driver_list'), #driver_list
    path('drivers/<str:license_number>/', views.driver_detail, name='driver_detail'), #driver_details

    path('students/', views.student_list, name='student_list'), #student list
    path('students/add/', views.add_student, name='add_student'),  # to Add Student
    path('students/<int:id>/', views.student_detail, name='student_detail'), #student details
    path('routes/', views.route_list, name='route_list'), #route list
    path('routes/add/', views.add_route, name='add_route'), #add route
    path('stoppages/', views.stoppage_list, name='stoppage_list'), #stoppage list
    path('stoppages/add/', views.add_stoppage, name='add_stoppage'), #add stoppage
    path('notices/', views.notice_list, name='notice_list'),#for notices
    path('notices/add/', views.add_notice, name='add_notice'), #for notices
]
