CREATE TABLE ProductName 
(
    ProductCategoryName VARCHAR(100) PRIMARY KEY,
    ProductCategoryNameEnglish VARCHAR(100)
);

CREATE TABLE Sellers 
(
    SellerID VARCHAR(100) PRIMARY KEY,
    SellerZipCodePrefix INT,
    SellerCity VARCHAR(100),
    SellerState VARCHAR(3)
);

CREATE TABLE Products 
(
    ProductID VARCHAR(100) PRIMARY KEY,
    ProductCategoryName VARCHAR(100),
    ProductNameLength INT,
    ProductDescLength INT,
    ProductPhotosQty INT,
    ProductWeightG INT,
    ProductLengthCM INT,
    ProductHeightCM INT,
    ProductWidthCM INT
);

CREATE TABLE Customers 
(
    CustomerID VARCHAR(100) PRIMARY KEY,
    CustomerUniqueID VARCHAR(100),
    CustomerZipCodePrefix INT,
    CustomerCity VARCHAR(50),
    CustomerState VARCHAR(3)
);

CREATE TABLE Orders 
(
    OrderID VARCHAR(100) PRIMARY KEY,
    CustomerID VARCHAR(100),
    OrderStatus VARCHAR(30),
    OrderPurchaseTimestamp TIMESTAMP,
    OrderApprovedAt TIMESTAMP,
    OrderDeliveredCarrierDate TIMESTAMP,
    OrderDeliveredCustomerDate TIMESTAMP,
    OrderEstimatedDeliveryDate TIMESTAMP
);

CREATE TABLE OrdersReviews 
(
    ReviewID VARCHAR(100) PRIMARY KEY,
    OrderID VARCHAR(100),
    ReviewScore INT,
    ReviewCommentTitle VARCHAR(100),
    ReviewCommentMessage VARCHAR(1000),
    ReviewCreationDate TIMESTAMP,
    ReviewAnswerDate TIMESTAMP
);

CREATE TABLE OrderPayments (
    OrderID VARCHAR(100),
    PaymentSequential INT,
    PaymentType VARCHAR(100),
    PaymentInstallments INT,
    PaymentValue DECIMAL(10,2),
    PRIMARY KEY (OrderID, PaymentSequential)
);

CREATE TABLE OrderItems 
(
    OrderID VARCHAR(100),
    OrderItemID INT,
    ProductID VARCHAR(100),
    SellerID VARCHAR(100),
    ShippingLimitDate TIMESTAMP,
    Price DECIMAL(10,2),
    FreightValue DECIMAL(10,2),
    PRIMARY KEY (OrderID, OrderItemID)
);

CREATE TABLE Geolocation 
(
    GeolocationZipCodePrefix INT,
    GeolocationLat DECIMAL(10,7),
    GeolocationLng DECIMAL(10,7),
    GeolocationCity VARCHAR(50),
    GeolocationState VARCHAR(3)
);


COPY OrdersReviews (ReviewID, OrderID, ReviewScore, ReviewCommentTitle
, ReviewCommentMessage, ReviewCreationDate, ReviewAnswerDate)
FROM 'C:\archive\olist_order_reviews_dataset.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');


-----
CREATE TEMP TABLE temp_import_reviews AS SELECT * FROM ordersreviews WITH NO DATA;

COPY temp_import_reviews
FROM 'C:\archive\olist_order_reviews_dataset.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');

INSERT INTO ordersreviews
SELECT * FROM temp_import_reviews
ON CONFLICT (reviewid) DO NOTHING;

DROP TABLE temp_import_reviews;

