from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispLogin),
    path('dashboard', views.dispDashboard),
    path('guest/<str:name>', views.dispGuest),




    # ACTION ROUTES
    path('login', views.login),
    path('logout', views.logout),

]