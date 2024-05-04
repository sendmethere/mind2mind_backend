from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import PlayerViewSet
from quizzes.views import QuizViewSet, PlayerSuccessRecordsView, add_success_user, get_random_quizzes, get_player_statistics

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/players/', include(PlayerViewSet.as_view({
        'get': 'list',    # 'GET' 요청
        'post': 'create'  # 'POST' 요청
    }))),
    path('api/players/<int:pk>/', include(PlayerViewSet.as_view({
        'get': 'retrieve',   # 'GET' 요청
        'put': 'update',     # 'PUT' 요청
        'delete': 'destroy'  # 'DELETE' 요청
    }))),
    path('api/quizzes/', include(QuizViewSet.as_view({
        'get': 'list',   # 'GET' 요청
        'post': 'create' # 'POST' 요청
    }))),
    path('api/quizzes/<int:pk>/', include(QuizViewSet.as_view({
        'get': 'retrieve',   # 'GET' 요청
        'put': 'update',     # 'PUT' 요청
        'delete': 'destroy'  # 'DELETE' 요청
    }))),
    path('api/success-records/<str:nickname>/', PlayerSuccessRecordsView.as_view(), name='player-success-records'),
    path('api/success_user', add_success_user, name='add_success_user'),
    path('api/random-quizzes/', get_random_quizzes, name='random-quizzes'),
]
