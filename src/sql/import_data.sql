COPY ProductName (
    ProductCategoryName,
    ProductCategoryNameEnglish
)
FROM 'C:\sql\product_category_name_translation.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY Products (
    ProductID,
    ProductCategoryName,
    ProductNameLength,
    ProductDescLength,
    ProductPhotosQty,
    ProductWeightG,
    ProductLengthCM,
    ProductHeightCM,
    ProductWidthCM
)
FROM 'C:\sql\olist_products_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY Sellers (
    SellerID,
    SellerZipCodePrefix,
    SellerCity,
    SellerState
)
FROM 'C:\sql\olist_sellers_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY Customers (
    CustomerID,
    CustomerUniqueID,
    CustomerZipCodePrefix,
    CustomerCity,
    CustomerState
)
FROM 'C:\sql\olist_customers_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY Orders (
    OrderID,
    CustomerID,
    OrderStatus,
    OrderPurchaseTimestamp,
    OrderApprovedAt,
    OrderDeliveredCarrierDate,
    OrderDeliveredCustomerDate,
    OrderEstimatedDeliveryDate
)
FROM 'C:\sql\olist_orders_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY OrderItems (
    OrderID,
    OrderItemID,
    ProductID,
    SellerID,
    ShippingLimitDate,
    Price,
    FreightValue
)
FROM 'C:\sql\olist_order_items_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);


COPY OrderPayments (
    OrderID,
    PaymentSequential,
    PaymentType,
    PaymentInstallments,
    PaymentValue
)
FROM 'C:\sql\olist_order_payments_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);



COPY OrdersReviews (
    ReviewID,
    OrderID,
    ReviewScore,
    ReviewCommentTitle,
    ReviewCommentMessage,
    ReviewCreationDate,
    ReviewAnswerDate
)
FROM 'C:\sql\olist_order_reviews_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);


COPY Geolocation (
    GeolocationZipCodePrefix,
    GeolocationLat,
    GeolocationLng,
    GeolocationCity,
    GeolocationState
)
FROM 'C:\sql\olist_geolocation_dataset.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);