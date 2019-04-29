from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

app_name = "mobilityday"

urlpatterns = [
    path('', views.MobilityDayTemplate.as_view()),
    path('results/', views.ResultsTemplate.as_view()),
    path('change/<uuid:model_id>/', views.MobilityDayTemplate.as_view()),
]

router = DefaultRouter()
router.register(r'api/mobilityday', views.MobilityDayViewSet)
router.register(r'api/school', views.SchoolMobilityViewSet)
router.register(r'api/meeting', views.MeetingMobilityViewSet)
urlpatterns += router.urls
