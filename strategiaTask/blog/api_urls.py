from django.urls import path

from .views import ArticleCreateView, CommentCreateView, ArticleCommentsListView, CommentListView

urlpatterns = [
    path('articles/create/', ArticleCreateView.as_view()),
    path('articles/<int:pk>/add-comment/', CommentCreateView.as_view(), {'parent': 'article'}),
    path('articles/<int:pk>/related-comments/', ArticleCommentsListView.as_view()),
    path('comments/<int:pk>/add-comment/', CommentCreateView.as_view(), {'parent': 'comment'}),
    path('comments/<int:pk>/related-comments/', CommentListView.as_view()),
]
