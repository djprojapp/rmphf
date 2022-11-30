from django.urls import path
from .import views

app_name="loan"

urlpatterns=[
    path('recovery', views.recovery, name="recovery"),
    path('disbursment', views.disbursment, name="disbursment"),
    path('delete/<int:loan_no>', views.delete, name="delete"),
    path('dashboard', views.index, name="dashboard"),


]