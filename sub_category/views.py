from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .model_serializers import SubCategory, SubCategorySerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class SubCategoryViewSet(ViewSet):
    queryset = SubCategory.objects.filter()

    def list(self, request):
        filter_data = request.data
        if filter_data.get("category"):
            self.queryset = self.queryset.filter(category=filter_data.get("category"))
        serializer = SubCategorySerializer(self.queryset, many=True)
        return Response({"sub_cat_list": serializer.data})

    def retrieve(self, request, pk):
        sub_cat_details = SubCategory.objects.filter(pk=pk).values().first()
        if not sub_cat_details:
            raise ValidationError("Invalid sub category ID.")
        return Response({"response": sub_cat_details})

    def create(self, request):
        data = request.data
        serializer_data = SubCategorySerializer(data=data)
        serializer_data.is_valid(raise_exception=True)
        sub_cat_instance = serializer_data.save()
        return Response({"message": "Sub Category created successfully.", "sub_cat_id": sub_cat_instance.id})

    def partial_update(self, request, pk):
        data = request.data
        sub_cat_details = SubCategory.objects.filter(pk=pk).first()
        if not sub_cat_details:
            raise ValidationError("Invalid sub category ID.")
        serializer_data = SubCategorySerializer(sub_cat_details, data=data, partial=True)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        return Response({"message": "Sub Category Updated successfully."})

    def destroy(self, request, pk):
        sub_cat_data = SubCategory.objects.get(pk=pk)
        sub_cat_data.delete()
        return Response({"message": "Sub Category Deleted Successfully."})

