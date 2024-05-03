from django.urls import path
from .views import PlayerSuccessRecordsView

urlpatterns = [
    path('success-records/<str:nickname>/', PlayerSuccessRecordsView.as_view(), name='player-success-records'),
]
