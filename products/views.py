from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from rest_framework import status, views
from rest_framework.response import Response
from .models import (
    AttributeValue, 
    AttributeName, 
    Attribute, 
    Product, 
    ProductAttributes, 
    ProductImage, 
    Image, 
    Catalog
)
from .serializers import (
    AttributeValueSerializer,
    AttributeNameSerializer,
    AttributeSerializer,
    ProductSerializer,
    ProductAttributesSerializer,
    ProductImageSerializer,
    ImageSerializer,
    CatalogSerializer
)

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


_parsing_dict = {
    "AttributeValue": (AttributeValue, AttributeValueSerializer),
    "AttributeName": (AttributeName, AttributeNameSerializer),
    "Attribute": (Attribute, AttributeSerializer),
    "Product": (Product, ProductSerializer),
    "ProductAttributes": (ProductAttributes, ProductAttributesSerializer),
    "ProductImage": (ProductImage, ProductImageSerializer),
    "Image": (Image, ImageSerializer),
    "Catalog": (Catalog, CatalogSerializer),
}

    
class ImportView(views.APIView):
    def _parse_item(self, item: dict) -> tuple[str, dict]:
        item_keys: list = list(item.keys())
        if len(item_keys) != 1: 
            raise ValueError("invalid number of keys in one item!")
        
        item_name: str = item_keys[0]
        item_values = item[item_name]
        if not isinstance(item_values, dict):
            raise ValueError("Values are not dict!")
        return item_name, item_values

    def _check_duplicity(self, item_values: dict, model) -> None:
        item_id = item_values.get("id", None) # TODO add support for PK that are not named id
        if item_id is None:
            return
        
        return model.objects.filter(id=item_id).first()

    def post(self, request):
        data = request.data
        try:
            for item in data:
                item_name, item_values = self._parse_item(item)
                print(item_name, item_values)
                model, model_serializer = _parsing_dict[item_name]
                existing_item = self._check_duplicity(item_values, model)
                if existing_item:
                    data_serializer = model_serializer(existing_item, data=item_values, partial=True)
                else:
                    data_serializer = model_serializer(data=item_values)
                if not data_serializer.is_valid():
                    return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                data_serializer.save()
        except ValueError:
            return Response("Invalid item", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e.args[0])
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)


class ModelListView(views.APIView):
    def get(self, request, model_name): 
        model, model_serializer = _parsing_dict[model_name]     
        objects = model.objects.all()
        serializer = model_serializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ModelDetailView(views.APIView):
    def get(self, request, model_name, id): 
        model, model_serializer = _parsing_dict[model_name]     
        obj = get_object_or_404(model, id=id)
        serializer = model_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)