from django.urls import path
from .import views

app_name="pms"

urlpatterns=[
    path('', views.welcome, name="welcome"),
    path('add_new', views.add_new, name="add_new"),
    path('home', views.home, name="home"),
    path('revise', views.revise, name="revise"),
    path('update/<int:ppo>', views.update, name="update"),
    path('calculate', views.calculate, name="calculate"),
    path('calculator/<int:ppo>', views.calculator, name="calculator"),
    path('candr', views.candr, name="candr"),
    path('simple_calculator', views.listcontent, name="simple_calculator"),
    path('payment', views.payment, name="payment"),
    path('bankadvice', views.bankadvice, name="bankadvice"),
    path('display_bankaccount', views.display_bankaccount, name="display_bankaccount"),
    path('add_ba', views.add_ba, name="add_ba"),
    path('add_bankaccount/<int:ppo>', views.add_bankaccount, name="add_bankaccount"),
    path('delete_bankaccount/<int:id>', views.delete_bankaccount, name="delete_bankaccount"),
    path('edit_bankaccount/<int:id>', views.edit_bankaccount, name="edit_bankaccount"),
    path('edit_ba/<int:id>', views.edit_ba, name="edit_ba"),
    path('search', views.search, name="search"),
    path('adjustments', views.adjustments, name="adjustments"),
    path('adjustment/<int:ppo>', views.adjustment, name="adjustment"),
    path('recovery', views.recovery, name="recovery"),
    path('rop/<int:ppo>', views.rop, name="rop"),
    path('self', views.self, name="self"),
    path('family-dis', views.family_dis, name="family-dis"),
    path('family-dar', views.family_dar, name="family-dar"),
    
    
    
    

    
]
