from django.shortcuts import render
from rest_framework.views import APIView
from .model_serializers import Products, ProductsSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


# Create your views here.
class ProductsView(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise ValidationError("Invalid Product Id.")

    def get(self, request, pk=None):
        if pk:
            data = self.get_object(pk)
            serializer = ProductsSerializer(data)
        else:
            filter_data = request.data
            product_data = Products.objects.filter()

            if filter_data.get("category"):
                product_data = product_data.filter(sub_category__category=filter_data.get("category"))
            if filter_data.get("sub_category"):
                product_data = product_data.filter(sub_category=filter_data.get("sub_category"))

            serializer = ProductsSerializer(product_data, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ProductsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        product_serializer_instance = serializer.save()
        return Response(
            {
                'message': 'Products Created Successfully',
                'product_id': product_serializer_instance.id
            }
        )

    def put(self, request, pk=None):
        product_data = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(product_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Product Updated Successfully."})

    def delete(self, request, pk):
        product_data = Products.objects.get(pk=pk)
        product_data.delete()

        return Response({
            'message': 'Product Deleted Successfully'
        })
