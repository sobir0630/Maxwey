from django.db import models
from food.models import Order, Customer, OrderProduct

# Create your models here.
class OrderSendSignal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)