from django.urls import path
from hospital.views import(
    hospital_list_view,
    hospital_detail_view
)


urlpatterns = [
    path('', hospital_list_view, name='hospital_list_url'),
    path('<int:id>/', hospital_detail_view, name='hospital_detail_url'),
]