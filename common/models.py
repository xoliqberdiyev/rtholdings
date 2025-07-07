import uuid

from django.db import models



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class OurActivityNumber(BaseModel):
    title = models.CharField(max_length=100)
    number = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.number}"
    

class ServiceType(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="media/service/images/%Y/%m/")

    def __str__(self):
        return self.title
    
class Service(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return f"{self.type.title} type - {self.title}"
    

class News(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class NewsImage(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images')
    image = models.ImageField(upload_to='media/news_image/image/%Y/%m/')

    def __str__(self):
        return self.image.name
    

class Feedback(BaseModel):
    image = models.ImageField(upload_to="media/feedback/image/%Y/%m/")
    full_name = models.CharField(max_length=75)
    comment = models.TextField()
    rate = models.FloatField()
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class ContactUs(BaseModel):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField()
    is_contacted = models.BooleanField(default=False)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    

class Product(BaseModel):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=75)
    location = models.CharField(max_length=250)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='media/prduct_images/image/%Y/%m/')

    def __str__(self):
        return f"{self.product.name} image"
    