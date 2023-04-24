drop database retadn2;
create database retadn2;

use retadn2;
DROP TABLE IF EXISTS `admina`;

CREATE TABLE `admina` (
  `Admin_ID` int(11) NOT NULL,
  `Admin_Login` int(11) NOT NULL,
  `Admin_PWD` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Admin_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `admina` (`Admin_ID`, `Admin_Login`, `Admin_PWD`) VALUES (3, 12321, '112233');

###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL,
  `cust_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_phone` bigint(20) NOT NULL,
  `cust_add` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_billadd` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_pwd` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cust_wallet` bigint(20) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE KEY `cust_email` (`cust_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cust_id` int(11) NOT NULL,
  `cart_index` int(11),
  `fin_val` float NOT NULL,
  PRIMARY KEY (`cart_index`),
  KEY `cust_id` (`cust_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################
delimiter //
CREATE TRIGGER `create_cart`
AFTER INSERT ON `customer`
FOR EACH ROW
BEGIN
    INSERT INTO `cart` (`cust_id`, `cart_index`, `fin_val`)
    VALUES (NEW.cust_id, NEW.cust_id, 0.0);
END;
//

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################


INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (11, 'Divyansh Mishra', 'kulasy@example.net', '7514292878', 'New Delhi', 'New Delhi', '1122', 10);
INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (13, 'Dharani', 'cruick@example.net', '7813287422', 'Dubai.', 'Dubai.', '2233', 20000);
INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (14, 'Priyash', 'jaleel@example.org', '9668373125', 'Nepal', 'Nepal', '3344', 12000);
INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (15, 'Aditya', 'ciara@example.com', '8872037842', 'Haryana', 'Haryana', '4455', 9000);
INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (100, 'Mohit', 'carlos@example.com', '8459939909', 'Dwarka', 'Dwarka', '5566', 13200);
INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES (101, 'Hardik', 'jaquelin@example.org', '9782300290', 'Ghaziabad', 'Ghaziabad', '6677', 9999);


###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `emp_login` int(11) NOT NULL,
  `emp_pwd` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `emp_desc` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`emp_id`),
  UNIQUE KEY `emp_login` (`emp_login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_login`, `emp_pwd`, `emp_desc`) VALUES (1025, 'Rajesh', 3995, '813950', 'Good');
INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_login`, `emp_pwd`, `emp_desc`) VALUES (1225, 'Bharat', 8297, '161238', 'Poor');
INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_login`, `emp_pwd`, `emp_desc`) VALUES (1707, 'Dilip', 9936, '731805', 'Excellent');

###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL,
  `cat_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cat_desc` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `category` (`cat_id`, `cat_name`, `cat_desc`) VALUES (10, 'Body Care', 'Soaps, Shampoos, etc.');
INSERT INTO `category` (`cat_id`, `cat_name`, `cat_desc`) VALUES (11, 'Food', 'Pretty Self-Explanatory');
INSERT INTO `category` (`cat_id`, `cat_name`, `cat_desc`) VALUES (12, 'Electronics', 'Iron, kettle etc.');
INSERT INTO `category` (`cat_id`, `cat_name`, `cat_desc`) VALUES (13, 'Clothing', 'Jeans, T-Shirt etc.');

###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################
###############################################################################################################################################################################

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `prod_id` int(11) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `prod_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prod_desc` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prod_cost` float NOT NULL,
  PRIMARY KEY (`prod_id`),
  KEY `cat_id` (`cat_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `category` (`cat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (1, 10, 'Pantene', '200 ML', '180');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (2, 10, 'Lux', '3 Bars of soap', '225');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (3, 10, 'Nivia Moisturiser', '500 ml', '360');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (4, 10, 'Axe Perfume', '250 ml', '250');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (5, 11, 'Cheese', '12 Slices', '90');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (6, 11, 'Eggs', '12 Eggs', '240');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (7, 11, 'Paneer', '250 gms', '110');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (8, 11, 'Chips', '60 gms', '40');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (9, 12, 'Hair Dryer', '60 Watt', '1200');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (10, 12, 'Iron', '200 Watt', '800');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (11, 12, 'Blender', '40 Watt', '2500');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (12, 12, 'Chimney', '1kW', '12000');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (13, 13, 'T-Shirt', 'Cotton', '800');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (14, 13, 'Jeans', 'Denim', '1600');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (15, 13, 'Jacket', 'Leather', '6000');
INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES (16, 13, 'Shorts', 'Cotton', '600');

###############################################################################################################################################################################
###############################################################################################################################################################################
###################################################################################################################################################################################
###########################################################################################################################################################################

DROP TABLE IF EXISTS `inventory`;

CREATE TABLE `inventory` (
  `prod_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  PRIMARY KEY (`prod_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `products` (`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (1, 22);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (2, 26);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (3, 18);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (4, 22);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (5, 27);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (6, 22);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (7, 31);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (8, 25);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (9, 12);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (10, 13);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (11, 14);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (12, 10);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (13, 23);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (14, 33);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (15, 23);
INSERT INTO `inventory` (`prod_id`, `qty`) VALUES (16, 34);

###############################################################################################################################################################################
###############################################################################################################################################################################
###################################################################################################################################################################################
###########################################################################################################################################################################

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL,
  `fin_val` float NOT NULL,
  `pay_get` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `payment` (`pay_id`, `fin_val`, `pay_get`) VALUES (101966, '4331', '16');
INSERT INTO `payment` (`pay_id`, `fin_val`, `pay_get`) VALUES (110686, '7327', '14');
INSERT INTO `payment` (`pay_id`, `fin_val`, `pay_get`) VALUES (114066, '4127', '16');

###############################################################################################################################################################################
###############################################################################################################################################################################
###################################################################################################################################################################################
###########################################################################################################################################################################

DROP TABLE IF EXISTS `coupons`;

CREATE TABLE `coupons` (
  `coupon_id` int(11) NOT NULL,
  `coupon_val` float NOT NULL,
  `coupon_desc` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`coupon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES (109, '27', 'Get 27 Percent OFF');
INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES (124, '24', 'Get 24 Percent OFF');
INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES (138, '36', 'Get 36 Percent OFF');
INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES (145, '28', 'Get 28 Percent OFF');
INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES (153, '20', 'Get 20 Percent OFF');

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################

DROP TABLE IF EXISTS `ordera`;

CREATE TABLE `ordera` (
  `order_id` int(11) AUTO_INCREMENT NOT NULL,
  `cart_index` int(11) NOT NULL,
  `order_time` datetime NOT NULL,
  `fin_val` float NOT NULL,
  `shipping_address` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `cart_index` (`cart_index`),
  CONSTRAINT `ordera_ibfk_1` FOREIGN KEY (`cart_index`) REFERENCES `cart` (`cart_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
 
###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################
 
DROP TABLE IF EXISTS `order_items`;
 
CREATE TABLE `order_items` (
  `order_item_id` int(11) AUTO_INCREMENT NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `cart_index` int(11) DEFAULT NULL,
  `prod_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_item_id`),
  KEY `cart_index` (`cart_index`),
  KEY `prod_id` (`prod_id`),
  KEY `order_id` (`order_id`),
   FOREIGN KEY (`cart_index`) REFERENCES `cart` (`cart_index`),
   FOREIGN KEY (`prod_id`) REFERENCES `products` (`prod_id`),
   FOREIGN KEY (`order_id`) REFERENCES `ordera` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
 

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################

DROP TABLE IF EXISTS `shipper`;

CREATE TABLE `shipper` (
  `shipment_id` int(11) AUTO_INCREMENT NOT NULL,
  `shipper_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `order_time` datetime NOT NULL,
  `del_date` datetime NOT NULL,
  `shipping_address` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`shipment_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `shipper_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `ordera` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- INSERT INTO `shipper` (`shipment_id`, `shipper_id`, `order_id`, `order_time`, `del_date`, `shipping_address`) VALUES ();

###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################

DROP TABLE IF EXISTS `CartItems`;

CREATE TABLE `CartItems` (
  `cart_item_id` int(11) AUTO_INCREMENT NOT NULL,
  `cart_index` int(11) DEFAULT NULL,
  `prod_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`cart_item_id`),
  KEY `cart_index` (`cart_index`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `CartItems_ibfk_1` FOREIGN KEY (`cart_index`) REFERENCES `cart` (`cart_index`),
  CONSTRAINT `CartItems_ibfk_2` FOREIGN KEY (`prod_id`) REFERENCES `products` (`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DELIMITER //

CREATE TRIGGER update_cart_fin_val
AFTER INSERT ON CartItems
FOR EACH ROW
BEGIN
    UPDATE cart SET fin_val = (
        SELECT SUM(prod_cost * quantity) 
        FROM CartItems
        JOIN products ON CartItems.prod_id = products.prod_id
        WHERE CartItems.cart_index = NEW.cart_index
    ) WHERE cart_index = NEW.cart_index;
END;
//
DELIMITER ;

DELIMITER //

CREATE TRIGGER update_cart_fin_val_upd
AFTER update ON CartItems
FOR EACH ROW
BEGIN
    UPDATE cart SET fin_val = (
        SELECT SUM(prod_cost * quantity) 
        FROM CartItems
        JOIN products ON CartItems.prod_id = products.prod_id
        WHERE CartItems.cart_index = NEW.cart_index
    ) WHERE cart_index = NEW.cart_index;
END;
//
DELIMITER ;


###############################################################################################################################################################################
###################################################################################################################################################################################
##################################################################################################################################################################################
########################################################################################################################################################################

select * from cartitems;
select * from ordera;
select * from shipper;
select * from customer;
INSERT INTO `CartItems` (`cart_index`, `prod_id`, `quantity`) VALUES (13, 1, 2);

-- UPDATE CartItems SET quantity=3 WHERE prod_id=4;


	






