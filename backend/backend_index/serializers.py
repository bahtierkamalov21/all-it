from .models import Category, Project, ProjectImage, Stack
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, validated_data):
        if self.context['request'].method == 'POST':
            if Project.objects.filter(fk_user=validated_data["fk_user"], complete=False).exists():
                raise serializers.ValidationError({"fk_user": "Предыдущий проект пользователя является не завершенным."})
            return validated_data
        return validated_data

    class Meta:
        model = Project
        fields = '__all__'

class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

class ProjectImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'
