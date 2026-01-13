from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderSendSignal
from .bot import telegram_send_mesage

        

@receiver(post_save, sender=OrderSendSignal)
def send_signall(sender, instance, created, order_product=None, **kwargs):
    """
    sender        -> qaysi model signal yubordi (Order)
    instance      -> asosiy obyekt (Order)
    created       -> yangi buyurtma flag
    order_product -> qo‘shimcha argument, kerak bo‘lsa
    kwargs        -> boshqa qo‘shimchalar
    """
    if created:
        text = f"""
Sizga yangi buyurtma keldi!
--------------------------------------------
Buyurtma ID: {instance.id}
Mijoz: {instance.customer.first_name} {instance.customer.last_name}
Telefon: {instance.customer.phone_number}
Manzil: {instance.address}
--------------------------------------------
Mahsulot: {order_product.product.title if order_product else 'Nomaʼlum'}
Kategoriya: {order_product.product.category.title if order_product else 'Nomaʼlum'}
Buyurtma soni: {order_product.count if order_product else 'Nomaʼlum'}
Umumiy summa: {order_product.price if order_product else 'Nomaʼlum'}
Toʻlov turi: {'Naqd' if instance.payment_type == 1 else 'Karta'}
Buyurtma vaqti: {instance.created_at.strftime('%d-%m-%Y %H:%M')} 
({'Kunduzi' if 6 <= instance.created_at.hour < 18 else 'Kechasi'})
----------------------------------------------

        
Yana buyirtma qiling 👇    
http://127.0.0.1:8080/
"""
        telegram_send_mesage(text)