from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('entry/', views.entry, name='entry'),
    path('exit/', views.exit, name='exit'),
    path('todayreport/',views.export_users_csv_today,name='todayreport'),
    path('overallreport/',views.export_users_csv_overall,name='overallreport'),
    path('stillinsidereport/',views.export_users_csv_inside,name='stillinsidereport'),
]