from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from taskApp.students import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  path('api/', include(router.urls)),
  path('admin/', admin.site.urls),
]

