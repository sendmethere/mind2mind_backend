from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import PlayerViewSet
from quizzes.views import QuizViewSet, PlayerSuccessRecordsView, add_success_user, get_random_quizzes, get_player_statistics

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/success-records/<str:nickname>/', PlayerSuccessRecordsView.as_view(), name='player-success-records'),
    path('api/success_user', add_success_user, name='add_success_user'),
    path('api/random-quizzes/', get_random_quizzes, name='random-quizzes'),
]
