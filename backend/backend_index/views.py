from .models import Category, Project, ProjectImage
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, ProjectSerializer, ProjectImageSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

class ProjectImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.AllowAny]

