from django.urls import path, include

from .views import ArticleCreateView, CommentCreateView, CommentListView, CommentRetrieveView

urlpatterns = [
    path('articles/create/', ArticleCreateView.as_view()),
    path('articles/<int:pk>/add-comment/', CommentCreateView.as_view(), {'parent': 'article'}),
    path('comments/<int:pk>/add-comment/', CommentCreateView.as_view(), {'parent': 'comment'}),
    path('comments/list/', CommentListView.as_view()),
    path('comments/<int:pk>/related-comments', CommentRetrieveView.as_view()),
]
