import logging
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
from django.db import transaction
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view
from db.models import Orders, OrdersDetails, OrdersDetails
from serializers.serializers import OrdersSerializer, OrdersDetailsSerializer
from uudragon_agency.local.settings import DEFAULT_PAGE_SIZE, STATUS_PAYMENT_COMPLETED, STATUS_PAYMENT_ROLLBACK, \
    STATUS_CHECK_COMPLETED

LOG = logging.getLogger(__name__)


@api_view(['GET'])
def query_agency_orderss(request, agent_id):
    message = request.GET

    LOG.info('Current method is [query_agency_orders], received message is %s' % message)

    pageSize = message.pop('pageSize')
    if pageSize is None or pageSize == 0:
        pageSize = DEFAULT_PAGE_SIZE
    pageNo = message.pop('pageNo')
    if pageNo is None or pageNo == 0:
        pageNo = 1

    LOG.debug('Current message is %s' % message)

    resp_message = dict()

    for key in message.iterkeys():
        key += '__contains'
        LOG.debug('Condition of query is %s' % message)

    try:
        orders_list = Orders.objects.filter(**message).filter(createor=agent_id).order_by('order_time')
        paginator = Paginator(orders_list, pageSize, orphans=0, allow_empty_first_page=True)
        total_page_count = paginator.num_pages
        if pageNo > total_page_count:
            pageNo = total_page_count
        elif pageNo < 1:
            pageNo = 1
        cur_page = paginator.page(pageNo)
        page_records = cur_page.object_list
        resp_array = []
        for item in page_records:
            record_seria = OrdersSerializer(item)
            resp_array.append(record_seria.data)
        resp_message['records'] = resp_array
        resp_message['recordsCount'] = paginator.count
        resp_message['pageSize'] = pageSize
        resp_message['pageNumber'] = total_page_count
        resp_message['pageNo'] = pageNo
    except Exception as e:
        LOG.error('Query orderss information error. [ERROR] %s' % str(e))
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Query orderss information error'},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK, data=resp_message, content_type='application/json;charset=utf-8')


@api_view(['GET'])
def query_agency_orders(request, orders_no):
    LOG.info('Current method is [query_agency_orders], received [orders_no] is %s' % orders_no)

    resp_message = None
    try:
        orders = Orders.object.filter(order_no=orders_no).first()
        orders_seria = OrdersSerializer(orders)
        orders_details = OrdersDetails.objects.filter(order_no=orders_no)
        details_seria = []
        for detail in orders_details:
            detail_seria = OrdersDetailsSerializer(detail)
            details_seria.append(detail_seria.data)
        resp_message = orders_seria.data
        resp_message['details'] = details_seria
    except Exception as e:
        LOG.error('Query orders information error. [ERROR] %s' % str(e))
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Query orders [%s] information error' % orders_no},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK, data=resp_message, content_type='application/json;charset=utf-8')


@api_view(['POST'])
@transaction.commit_manually
def save_orders(request):
    message = request.DATA

    LOG.info('Current method is [save_orders], received message is %s' % message)

    details = message.get('details')

    try:
        for detail in details:
            orders_detail = OrdersDetails(
                id='%s%s' % (message.get('order_no'), detail.get('code')),
                order_no=message.get('order_no'),
                code=detail.get('code'),
                name=detail.get('name'),
                qty=detail.get('qty'),
                amount=detail.get('amount'),
            )
            orders_detail.save()
        now_time = datetime.now()
        orders = Orders(
            id=message.get('id'),
            order_no=message.get('order_no'),
            order_type=message.get('order_type'),
            customer_name=message.get('customer_name'),
            customer_phone=message.get('customer_phone'),
            customer_tel=message.get('customer_tel'),
            customer_addr=message.get('customer_addr'),
            has_invoice=message.get('has_invoice'),
            amount=message.get('amount'),
            payment=message.get('payment'),
            status=0,
            order_time=now_time,
            creator=message.get('creator'),
            create_time=now_time,
            updater=message.get('updater'),
            update_time=now_time,
            yn=1
        )
        orders.save()
        transaction.commit()
    except Exception as e:
        LOG.error('Save orders information error. [ERROR] %s' % str(e))
        transaction.rollback()
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Save orders [%s] information error'},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.commit_manually
def payment_completed(request, orders_no):
    LOG.info('Current method is [payment_completed], received [orders_no] is %s' % orders_no)

    try:
        orders = Orders.objects.filter(order_no=orders_no).select_for_update().first()
        orders.status = STATUS_PAYMENT_COMPLETED
        orders.save()
        transaction.commit()
    except Exception as e:
        LOG.error('Orders payment error. [ERROR] %s' % str(e))
        transaction.rollback()
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Orders payment error. [order_no] is %s' % orders_no},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.commit_manually
def payment_rollback(request, orders_no):
    LOG.info('Current method is [payment_rollback], received [orders_no] is %s' % orders_no)

    try:
        orders = Orders.objects.filter(order_no=orders_no).select_for_update().first()
        orders.status = STATUS_PAYMENT_ROLLBACK
        orders.save()
        transaction.commit()
    except Exception as e:
        LOG.error('Orders payment error. [ERROR] %s' % str(e))
        transaction.rollback()
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Orders payment error. [order_no] is %s' % orders_no},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.commit_manually
def check_completed(request, orders_no):
    LOG.info('Current method is [check_completed], received [orders_no] is %s' % orders_no)

    try:
        orders = Orders.objects.filter(order_no=orders_no).select_for_update().first()
        orders.status = STATUS_CHECK_COMPLETED
        orders.save()
        transaction.commit()
    except Exception as e:
        LOG.error('Orders check error. [ERROR] %s' % str(e))
        transaction.rollback()
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'error': 'Orders checks error. [order_no] is %s' % orders_no},
                        content_type='application/json;charset=utf-8')
    return Response(status=status.HTTP_200_OK)


