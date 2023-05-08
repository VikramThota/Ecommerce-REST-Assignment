from rest_framework import serializers
from .models import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'category'),
                message="Sub Category Name Already Exist."
            )
        ]
        fields = "__all__"
