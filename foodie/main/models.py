from django.db import models

class products(models.Model):
    name = models.CharField(max_length= 20)
    dis = models.CharField(max_length= 100)
    price = models.CharField(max_length= 10)
    dis = models.CharField(max_length= 100)
    cat = models.CharField(max_length= 20 ,blank=True, null=True)
    img = models.CharField(max_length= 100)

    class Meta:
        db_table = "products"

class orders(models.Model):
    name = models.CharField(max_length= 20)
    phone = models.CharField(max_length= 10)
    address = models.CharField(max_length= 100)
    food = models.CharField(max_length= 50)
    price = models.CharField(max_length= 20)

    class Meta:
        db_table = "orders"

class feedback(models.Model):
    name = models.CharField(max_length= 20)
    content = models.CharField(max_length= 250)

    class Meta:
        db_table = "feedback"