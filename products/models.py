from django.db import models

# Create your models here.
class AttributeValue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hodnota = models.TextField()


class AttributeName(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev = models.TextField(blank=True)
    kod = models.TextField(blank=True, null=True)
    zobrazit = models.BooleanField(blank=True, null=True)


class Attribute(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nazev = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    cena = models.FloatField()
    mena = models.CharField(max_length=10, blank=True)
    published_on = models.TextField(blank=True, null=True) 
    # models.DateField(blank=True, null=True) is in YYYY-MM-DD format.
    is_published = models.BooleanField(blank=True, null=True)


class ProductAttributes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Image(models.Model):
    id = models.BigIntegerField(primary_key=True)
    obrazek = models.TextField()


class ProductImage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)


class Catalog(models.Model):
    id = models.BigIntegerField(primary_key=True)    
    nazev = models.TextField(blank=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    products_ids = models.ManyToManyField(Product)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)
    
    
