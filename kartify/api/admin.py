from django.contrib import admin
from .models import Customer, Item, Orders, Seller, Delivery_Agent, Order_contains_item, Customer_makes_order

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','address','pincode','c_email','age','phone_num']
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','item_name','category','description','item_price','quantity', 'Seller_Email']
    def Seller_Email(self, obj):
        return obj.s_email.s_email 

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','total_price','time','customer_email','item_list']

    def customer_email(self, obj):
        customer = Customer_makes_order.objects.filter(order_id=obj).first()
        return customer.c_email.c_email

    def item_list(self, obj):
        items = Order_contains_item.objects.filter(order_id=obj)
        item_list = []
        for item in items:
            item_dict = {'item_id': item.item_id.item_id, 'quantity': item.quantity}
            item_list.append(item_dict)
        return item_list

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['s_email','name','address','phone_num']
@admin.register(Delivery_Agent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ['name','order_id','phone_num','d_email']