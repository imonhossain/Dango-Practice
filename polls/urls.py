from django.urls import path

from polls.views import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('department/', DepartmentList.as_view()),
    # path('<int:department_id>/', views.detail, name='detail'),
]