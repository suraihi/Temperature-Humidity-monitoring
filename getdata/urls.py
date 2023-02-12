from getdata.views import save_data, share_data
from django.urls import path
from getdata import views



urlpatterns = [
    path('save', save_data),
    path('data', share_data),
    path('', views.show_graph, name='show_graph'),
    path('live', views.live_graph, name='live_graph'),

    path('display-data/', views.share_data, name='display_data'),

]