from django.urls import path
from .views import AssignmentListCreateAPIView, AssignmentRetrieveUpdateDestroyAPIView, CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-retrieve-update-destroy'),
    path('quizzes/', QuizListCreateAPIView.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroyAPIView.as_view(), name='quiz-retrieve-update-destroy'),
    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentRetrieveUpdateDestroyAPIView.as_view(), name='assignment-retrieve-update-destroy'),
]