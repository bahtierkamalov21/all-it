from .models import Category, Project, ProjectImage, Stack
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import CategorySerializer, ProjectSerializer, ProjectImageSerializer, StackSerializer

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

class StackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    permission_classes = [permissions.AllowAny]

class ProjectImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.AllowAny]

@api_view(["GET"])
@permission_classes((AllowAny, ))
def getProjectsUser(request):
    user_id = request.GET.get("user_id")
    projects = Project.objects.filter(fk_user=user_id)
    serializer = ProjectSerializer(projects, many=True, context={"request": request})
    return Response(serializer.data, status=200)

@api_view(["GET"])
@permission_classes((AllowAny, ))
def getProjectSlug(request):
    link_path = request.GET.get("link_path")
    project = Project.objects.get(link_path=link_path)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data, status=200)
