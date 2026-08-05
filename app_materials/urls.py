# app_materials/urls.py

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseSubscriptionToggleView
from .views import CourseViewSet
from .views import LessonCreateAPIView
from .views import LessonDestroyAPIView
from .views import LessonListAPIView
from .views import LessonRetrieveAPIView
from .views import LessonUpdateAPIView

app_name = "app_materials"

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
    path(
        "course/<int:course_id>/subscribe/",
        CourseSubscriptionToggleView.as_view(),
        name="course-subscription",
    ),
] + router.urls
