from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from product.models import ProductSpecifications, Product
from product.serializers import SpecificationsSerializer, ProductSerializer


class APIFormDataView(APIView):
    def get(self, request, *args, **kwargs):
        data = ProductSpecifications.objects.all()
        serializer = SpecificationsSerializer(instance=data, many=True)
        new_dict = {
            'men': [],
            'women': [],
            'children': [],
        }

        for cat in serializer.data:
            new_dict[cat.pop('type')].append(cat)

        return Response(new_dict, status=status.HTTP_200_OK)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class APIProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class APIProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
