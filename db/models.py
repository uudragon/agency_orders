from django.db import models

__author__ = 'pluto'


class Orders(models.Model):
    # The unique number of orders
    id = models.AutoField(db_column='ID', primary_key=True, max_length=20)
    order_no = models.CharField(db_column='ORDER_NO', max_length=36, unique=True, null=False)
    order_type = models.PositiveSmallIntegerField(db_column='ORDER_TYPE', max_length=4, default='0')
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=255, null=False)
    customer_phone = models.CharField(db_column='CUSTOMER_PHONE', max_length=20)
    customer_tel = models.CharField(db_column='CUSTOMER_TEL', max_length=20)
    customer_addr = models.CharField(db_column='CUSTOMER_ADDR', max_length=255, null=False)
    has_invoice = models.BooleanField(db_column='HAS_INVOICE', default=False)
    amount = models.DecimalField(db_column='AMOUNT', max_digits=20, decimal_places=2, default='0.00')
    payment = models.PositiveSmallIntegerField(db_column='PAYMENT', max_length=4, default='2')
    status = models.PositiveSmallIntegerField(db_column='STATUS', max_length=4, default='0')
    order_time = models.DateTimeField(db_column='ORDER_TIME', auto_now_add=True)
    creator = models.CharField(db_column='CREATOR', max_length=100)
    create_time = models.DateTimeField(db_column='CREATE_TIME', auto_now_add=True)
    updater = models.CharField(db_column='UPDATER', max_length=100)
    update_time = models.DateTimeField(db_column='UPDATE_TIME', auto_now=True)
    yn = models.PositiveSmallIntegerField(db_column='YN', max_length=4, default=0)

    class Meta:
        db_table = 'T_ORDERS'


class OrdersDetails(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=73)
    order_no = models.CharField(db_column='ORDER_NO', max_length=36, null=False)
    code = models.CharField(db_column='CODE', max_length=36, null=False)
    name = models.CharField(db_column='NAME', max_length=255, null=False)
    qty = models.IntegerField(db_column='QTY', max_length=11, default='1')
    type = models.IntegerField(db_column='TYPE', max_length=4, default=0)
    amount = models.DecimalField(db_column='AMOUNT', max_digits=20, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'T_ORDERS_DETAILS'