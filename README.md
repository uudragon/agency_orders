#####目录
- [代理商订单保存接口](#11-url)
- [代理商订单查询接口](#21-url)
- [单笔代理商订单查询接口](#31-url)
- [支付完成接口](#41-url)
- [退款接口](#51-url)
- [审查完成接口](#61-url)
- [管理端查询代理商订单接口](#71-url)

#####1.代理商订单保存接口
接收客服系统发送的订单信息，按照一定规则将其拆分成发货单并返回将发货单信息返回给客服系统
######1.1 url
	method: POST
	agency/orders/save/
	注意：结尾的’/’不能省略
######1.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######1.3 请求参数
名称|类型|是否必填|说明
---|---|---|---
orders_no|String|Y|订单号
orders_type|INT|Y|订单类型。0：首期订单；1：促销品订单
customer_name|String|Y|客户姓名
customer_phone|String|Y|客户手机
customer_tel|String|Y|客户电话
customer_addr|String|Y|客户地址
has_invoice|int|Y|是否有发票。0：无；1：有
amount|decimal|Y|总金额
payment|INT|Y|支付方式，1银行;2支付宝
creator|String|Y|创建人
updater|String|Y|需改人
details|Array|Y|明细

$$$订单明细

名称|类型|是否必填|说明
---|---|---|---
code|String|Y|套餐/宣传品编号
name|String|Y|套餐/宣传品名称
qty|INT|Y|数量
amount|DECIMAL|Y|单品金额。

样例报文：

	{'orders_no':'001010101',
	'order_type':0,
	'customer_name':'yonghu1',
	'customer_addr':'北京市天安门',
	'customer_tel':'18600000000',
	'has_invoice':0,
	'amount':10.00,
	'payment':2,
	'creator':'admin',
	'updater':'admin'
	'details':[
		{
			'code':'101010',
			'name':'首期1',
			'qty':10,
			'amount':1.00
		}
	]}

######1.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

响应报文说明：
无

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Orders saved error.'}
	
----

#####2. 代理商订单查询接口
此接口用于查询代理商订单列表
######2.1 url
	method: GET
	agency/orders/query_orderss/${agent_no}/
	注意：结尾的’/’不能省略, agent_no为代理商编号
######2.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######2.3 请求参数
名称|类型|是否必填|说明
---|---|---|---
pageSize|Int|Y|每页显示记录数
pageNo|Int|Y|当前页号
creator|String|Y|代理商号
orders_no|String|O|订单号
orders_type|INT|O|订单类型。0：首期订单；1：促销品订单
customer_name|String|O|客户姓名
customer_phone|String|O|客户手机
customer_tel|String|O|客户电话
customer_addr|String|O|客户地址

样例报文：

	{'orders_no':'001010101',
	'order_type':0,
	'customer_name':'yonghu1',
	'customer_addr':'北京市天安门',
	'customer_tel':'18600000000',
	'pageSize':8,
	'pageNo':1,
	'creator':'agent001'
	}

######1.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

响应报文说明：

名称|类型|是否必填|说明
---|---|---|---
pageSize|Int|Y|每页显示记录数
pageNo|Int|Y|当前页号
recordsCount|Int|Y|总记录数
pageNumber|Int|Y|总页数
records|Array|N|当前页记录

$$$$Records

名称|类型|是否必填|说明
---|---|---|---
orders_no|String|Y|订单号
orders_type|INT|Y|订单类型。0：首期订单；1：促销品订单
customer_name|String|Y|客户姓名
customer_phone|String|Y|客户手机
customer_tel|String|Y|客户电话
customer_addr|String|Y|客户地址
has_invoice|int|Y|是否有发票。0：无；1：有
amount|decimal|Y|总金额
payment|INT|Y|支付方式，1银行;2支付宝
status|INT|Y|状态。-1已退款；0未付款；1已付款；3已审核；4已发货货；5.已完成


样例报文：

	{
		'pageSize':8,
		'pageNo':1,
		'recordsCount':1,
		'pageNumber':1,
		'records':[{
			'orders_no':'001010101',
			'order_type':0,
			'customer_name':'yonghu1',
			'customer_addr':'北京市天安门',
			'customer_tel':'18600000000',
			'has_invoice':0,
			'amount':10.00,
			'payment':2,
			'status':4
		}]
	}

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Orders query error.'}
	
----

#####3. 单笔代理商订单查询接口
此接口用于根据订单号查询订单明细
######3.1 url
	method: GET
	agency/orders/query_orders/${order_no}/
	注意：结尾的’/’不能省略，order_no为订单号
######3.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######3.3 请求参数
无

######3.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

响应报文说明：

名称|类型|是否必填|说明
---|---|---|---
orders_no|String|Y|订单号
orders_type|INT|Y|订单类型。0：首期订单；1：促销品订单
customer_name|String|Y|客户姓名
customer_phone|String|Y|客户手机
customer_tel|String|Y|客户电话
customer_addr|String|Y|客户地址
has_invoice|int|Y|是否有发票。0：无；1：有
amount|decimal|Y|总金额
payment|INT|Y|支付方式，1银行;2支付宝
status|INT|Y|状态。-1已退款；0未付款；1已付款；3已审核；4已发货货；5.已完成
details|Array|Y|明细

$$$订单明细

名称|类型|是否必填|说明
---|---|---|---
code|String|Y|套餐/宣传品编号
name|String|Y|套餐/宣传品名称
qty|INT|Y|数量
amount|DECIMAL|Y|单品金额。

样例报文：

	{'orders_no':'001010101',
	'order_type':0,
	'customer_name':'yonghu1',
	'customer_addr':'北京市天安门',
	'customer_tel':'18600000000',
	'has_invoice':0,
	'amount':10.00,
	'payment':2,
	'status':4,
	'details':[
		{
			'code':'101010',
			'name':'首期1',
			'qty':10,
			'amount':1.00
		}
	]}

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Orders query error.'}
	
----

#####4. 支付完成接口
此接口用于在支付完成后，修改订单状态
######4.1 url
	method: GET
	agency/orders/payment/${order_no}/completed
	注意：结尾的’/’不能省略，${order_no}为订单号
######4.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######4.3 请求参数
无

######4.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Payment error.'}
	
----

#####5. 退款接口
此接口用于在发生退款后，修改订单状态
######5.1 url
	method: GET
	agency/orders/payment/${order_no}/rollback
	注意：结尾的’/’不能省略，${order_no}为订单号
######5.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######5.3 请求参数
无

######5.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Payment error.'}
	
----

#####6. 审核完成接口
此接口用于在客服审核订单后，修改订单状态
######6.1 url
	method: POST
	agency/orders/check_orders/${order_no}/
	注意：结尾的’/’不能省略，${order_no}为订单号
######6.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######6.3 请求参数
名称 | 类型 | 说明
------------ | ------------- | ------------
updater| String  | 更新人（当前操作员id）

样例报文：
    {'updater':'admin'}

######6.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Payment error.'}
	
----

#####7. 代理商订单查询接口
此接口用于查询代理商订单列表
######7.1 url
	method: GET
	agency/orders/query_all/
	注意：结尾的’/’不能省略
######7.2 header
	Content_Type:application/json;charset=utf-8
	Accept:application/json
######7.3 请求参数
名称|类型|是否必填|说明
---|---|---|---
pageSize|Int|Y|每页显示记录数
pageNo|Int|Y|当前页号
agent_id|String|O|代理商号
orders_type|INT|O|订单类型。0：首期订单；1：促销品订单
customer_name|String|O|客户姓名
begin_date|String|O|起始时间，格式YYYY-MM-DD
end_date|String|O|结束时间，格式YYYY-MM-DD
status|INT|O|订单状态，-1已退款；0未付款；1已付款；

样例报文：

	{
	'order_type':0,
	'agent_id':'yonghu1',
	'customer_name':'黄强',
	'pageSize':8,
	'pageNo':1
	}

######7.4 响应报文
成功响应：

	HTTP_STATUS_CODE:200

响应报文说明：

名称|类型|是否必填|说明
---|---|---|---
pageSize|Int|Y|每页显示记录数
pageNo|Int|Y|当前页号
recordsCount|Int|Y|总记录数
pageNumber|Int|Y|总页数
records|Array|N|当前页记录

$$$$Records

名称|类型|是否必填|说明
---|---|---|---
orders_no|String|Y|订单号
orders_type|INT|Y|订单类型。0：首期订单；1：促销品订单
customer_name|String|Y|客户姓名
customer_phone|String|Y|客户手机
customer_tel|String|Y|客户电话
customer_addr|String|Y|客户地址
has_invoice|int|Y|是否有发票。0：无；1：有
amount|decimal|Y|总金额
payment|INT|Y|支付方式，1银行;2支付宝
status|INT|Y|状态。-1已退款；0未付款；1已付款；2已审核；3已发货货；4已完成


样例报文：

	{
		'pageSize':8,
		'pageNo':1,
		'recordsCount':1,
		'pageNumber':1,
		'records':[{
			'orders_no':'001010101',
			'order_type':0,
			'customer_name':'yonghu1',
			'customer_addr':'北京市天安门',
			'customer_tel':'18600000000',
			'has_invoice':0,
			'amount':10.00,
			'payment':2,
			'status':4
		}]
	}

异常响应：

	a．	HTTP_STATUS_CODE:400 Bad request；
	b．	HTTP_STATUS_CODE:500 Server Error

异常报文：

名称 | 类型 | 说明
------------ | ------------- | ------------
error| String  | 错误信息

样例报文：

	{'error':'Orders query error.'}

