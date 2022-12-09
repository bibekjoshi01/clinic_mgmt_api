from django.urls import path
from . import views

urlpatterns = [
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

]
