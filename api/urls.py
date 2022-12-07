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
    path('blogapi', views.ListBlogAPIView.as_view()),
    path('blogcreateapi', views.CreatePostAPIView.as_view()),
    path('blogapi/<str:slug>/', views.DetailBlogAPIView.as_view()),
    path('comment', views.ListBlogAPIView.as_view()),
    path("<str:slug>/comment/", views.ListCommentAPIView.as_view(), name="list_comment"),
    path(
        "<str:slug>/comment/create/",
        views.CreateCommentAPIView.as_view(),
        name="create_comment",
    ),
    path(
        "<str:slug>/comment/<int:id>/",
        views.DetailCommentAPIView.as_view(),
        name="comment_detail",
    ),


#     class based urls
#    path('serviceapi/', views.ServiceAPI.as_view()),
#    path('serviceapi/<int:pk>/', views.ServiceAPI.as_view()),

]
