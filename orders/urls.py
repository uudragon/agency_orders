from django.conf.urls import patterns, url

__author__ = 'pluto'

urlpatterns = patterns(
    'orders.views',
    url(r'^query_all/$', 'query_all_orderss'),
    url(r'^check_orders/(.+)/$', 'check_orders'),
    url(r'^query_orderss/(.+)/$', 'query_agency_orderss'),
    url(r'^save/$', 'save_orders'),
    url(r'^payment/completed/$', 'payment_completed'),
    url(r'^payment/(.+)/rollback/$', 'payment_rollback'),
    url(r'^payment/(.+)/check/$', 'payment_check'),
    url(r'^query_orders/(.+)/$', 'query_agency_orders'),
)