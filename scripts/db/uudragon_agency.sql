CREATE TABLE IF NOT EXISTS `AGENCY`.`T_ORDERS` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `ORDER_NO` varchar(36) NOT NULL COMMENT '订单号，唯一，非空',
  `ORDER_TYPE` tinyint(4) NOT NULL DEFAULT '0' COMMENT '订单类型。0：首期订单；1：宣传品订单',
  `CUSTOMER_NAME` varchar(200) NOT NULL COMMENT '客户名称',
  `CUSTOMER_PHONE` varchar(32) DEFAULT NULL COMMENT '客户手机',
  `CUSTOMER_TEL` varchar(32) DEFAULT NULL COMMENT '客户电话',
  `CUSTOMER_ADDR` varchar(200) DEFAULT NULL COMMENT '客户地址',
  `HAS_INVOICE` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否有发票。0：无；1：有',
  `AMOUNT` decimal(10,0) NOT NULL DEFAULT 0.0 COMMENT '总付款金额',
  `PAYMENT` tinyint(4) NOT NULL DEFAULT '0' COMMENT '付款方式。1银行;2支付宝;3货到付款' DEFAULT 2,
  `STATUS` tinyint(4) NOT NULL DEFAULT '0' COMMENT '订单状态：-1已退款；0未付款；1已付款；2已审核；3已发货；4.已完成',
  `ORDER_TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '下单时间,非空',
  `CREATE_TIME` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间，非空',
  `CREATOR` varchar(32) DEFAULT NULL COMMENT '代理商ID',
  `UPDATE_TIME` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '更新时间',
  `UPDATER` varchar(32) DEFAULT NULL COMMENT '更新人',
  `YN` tinyint(1) NOT NULL DEFAULT '0' COMMENT '失效标识：0：有效；1：无效',

  PRIMARY KEY (`ID`),
  UNIQUE KEY `ORDER_NO_UNIQUE` (`ORDER_NO`)
)
ENGINE=InnoDB
COMMENT='订单信息表';

CREATE TABLE IF NOT EXISTS `AGENCY`.`T_ORDERS_DETAILS` (
  `ID` VARCHAR(73) NOT NULL COMMENT 'ID',
  `ORDER_NO` VARCHAR(36) NOT NULL COMMENT '订单号，非空',
  `CODE`  VARCHAR(36)  NOT NULL COMMENT '产品/商品编号，非空',
  `NAME` VARCHAR(255) NOT NULL COMMENT '名称，非空',
  `QTY` INT COMMENT '应发数量' DEFAULT 1,
  `AMOUNT` DECIMAL(20,2) COMMENT '金额' DEFAULT 0.00,

  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ORDER_DETAILS_UNIQUE` (`ORDER_NO` ASC,`CODE` ASC)
  )
ENGINE = InnoDB
COMMENT = '订单明细表';