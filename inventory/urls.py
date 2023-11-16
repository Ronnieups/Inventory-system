from django.urls import path
from .views import home, user_login, user_logout, input_data, retrieve_data, add_category, add_supplier

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('input/', input_data, name='input_data'),
    path('retrieve/', retrieve_data, name='retrieve_data'),
    path('add_category/', add_category, name='add_category'),
    path('add_supplier/', add_supplier, name='add_supplier'),
]