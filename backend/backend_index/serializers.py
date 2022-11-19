from .models import Category, Project, ProjectImage
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'
