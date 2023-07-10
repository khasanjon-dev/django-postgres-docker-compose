from django.db.models import CharField, ForeignKey, CASCADE, Model, ImageField


class Product(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='images/products')

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(upload_to='images/products')
    product = ForeignKey('Product', CASCADE, 'images')

    def __str__(self):
        return self.product.name
