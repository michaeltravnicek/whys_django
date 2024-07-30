from django.contrib import admin

from .models import AttributeValue, AttributeName, Attribute, Product, ProductAttributes, ProductImage, Image, Catalog

# Register your models here.

admin.site.register(AttributeValue)
admin.site.register(AttributeName)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(ProductImage)
admin.site.register(Image)
admin.site.register(Catalog)