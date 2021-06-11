from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

#Creating Router object
router = DefaultRouter()
#Register StudentViewSet with router
router.register('student_api', views.StudentModalViewSet, basename='student')
# router.register('student_api', views.StudentReadonlyModalViewSet, basename='student')#ReadOnly API URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),    
    path('', include(router.urls)),    
]