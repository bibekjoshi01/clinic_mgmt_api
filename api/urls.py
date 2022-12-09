from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('serviceapi', views.ServiceModelViewSet)
router.register('doctorapi', views.DoctorModelViewSet)
router.register('departmentapi', views.DepartmentModelViewSet)
router.register('health_packageapi', views.Health_PackageModelViewSet)
router.register('testapi', views.TestModelViewSet)
router.register('testimonialapi', views.TestimonialModelViewSet)
router.register('accreditationapi', views.AccreditationModelViewSet)
router.register('faqsapi', views.FAQsModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('contactapi', views.ContactView.as_view()),
#     class based urls
#    path('serviceapi/', views.ServiceAPI.as_view()),
#    path('serviceapi/<int:pk>/', views.ServiceAPI.as_view()),

]



