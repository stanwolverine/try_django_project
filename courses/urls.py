from django.urls import path, include
from .views import (
    CourseView,
    course_view,
)

urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', course_view, name='courses-list'),
]
