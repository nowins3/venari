from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_pic = models.ImageField()
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    authority_level = models.IntegerField()

    def __str__(self):
        return self.name

class Niche(models.Model):
    niche_name = models.CharField(max_length=200)
    niche_img = models.ImageField()
    niche_description = models.TextField(max_length=300)

    def __str__(self):
        return self.niche_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_pic = models.ImageField()
    category_description = models.TextField(max_length=300)

    def __str__(self):
        return self.category_name

class Type(models.Model):
    type_name = models.CharField(max_length=200)
    type_pic = models.ImageField()
    type_banner = models.ImageField(null=True)
    type_description = models.TextField(max_length=200)

    def __str__(self):
        return self.type_name

class User(AbstractUser):
    bio = models.TextField(max_length=300, null=True)
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(max_length=10, null=True)
    profile_pic = models.ImageField(null=True)

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    quality_stars = models.IntegerField(null=True)
    design_stars = models.IntegerField(null=True)
    general_stars = models.IntegerField(null=True)
    comment = models.TextField(max_length=500, null=True)
    rating_created_date = models.DateTimeField(auto_now_add=True)
    rating_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.quality_stars + self.design_stars + self.general_stars)/3)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)
    brand_url = models.CharField(max_length=200)
    brand_logo = models.ImageField()
    about_brand = models.TextField(null=True)

    def __str__(self):
        return self.brand_name
    
class Specification(models.Model):
    id = models.AutoField(primary_key=True)
    key_features = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    connectivity = models.CharField(max_length=200)
    Summary = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)
    supplier_email = models.EmailField(max_length=200)
    supplier_phone = models.IntegerField()
    supplier_address = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)
    rating = models.ForeignKey(Rating, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(Type, on_delete=CASCADE)
    product_name = models.CharField(max_length=200)
    product_model = models.CharField(max_length=200)
    product_brand = models.ForeignKey(Brand, on_delete=CASCADE)
    product_price = models.DecimalField(decimal_places=2, max_digits=9)
    product_previous = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    product_img = models.ImageField()
    product_population = models.CharField(max_length=200)
    product_niche = models.ForeignKey(Niche, on_delete=SET_NULL, null=True)
    product_size = models.DecimalField(decimal_places=2, max_digits=5)
    product_color = (models.CharField(max_length=200))
    product_material = models.CharField(max_length=200)
    product_availability = models.BooleanField()
    product_description = models.TextField(max_length=300, null=True)
    product_specifications = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    product_added_date = models.DateTimeField(auto_now_add=True) 
    last_bought = models.DateTimeField(auto_now=True)
    units = models.IntegerField()

    def __str__(self):
        return self.product_name
    
    def key_features(self):
        return (self.product_specifications.key_features).split(",")
    
    def style(self):
        return (self.product_specifications.style).split(",")
    
    def connectivity(self):
        return(self.product_specifications.connectivity).split(",")
    
    def summary(self):
        specifications = (self.product_specifications.Summary).split(",")
        specification_new = []
        for specification in specifications:
            specs = specification.split(":")
            specification_new.append(specs)
        return specification_new
