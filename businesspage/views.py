from .models import Quest, QComment
from .serializers import QuestSerializer, QCommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter

#페이지네이션
class QuestPagination(PageNumberPagination):
    page_size = 3

# Quest - CRUD 모두 가능
class QuestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = QuestPagination

    filter_backends = [SearchFilter]
    search_fields = ['qtitle', 'quest_text']

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#QComment
class QCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = QComment.objects.all()
    serializer_class = QCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user)