from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, pk, parent, *args, **kwargs):
        new_comment = Comment(content=request.data['content'])
        if parent == 'article':
            new_comment.level = 1
            new_comment.save()
            article = Article.objects.get(pk=pk)
            article.comments.add(new_comment)
            article.save()
        else:
            parent_comment = Comment.objects.get(pk=pk)
            new_comment.level = parent_comment.level + 1
            new_comment.save()
            parent_comment.comments.add(new_comment)
            parent_comment.save()
        return Response('Comment added.')


class ArticleCommentsListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Article.objects.get(pk=self.kwargs['pk']).comments.filter(level__lte=3)
        return queryset


class CommentRetrieveView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
