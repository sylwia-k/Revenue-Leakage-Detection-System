import pandas as pd

def get_delayed_orders(engine):
    query = """
    SELECT
        OrderId,
        OrderDeliveredCustomerDate AS order_delivered,
        OrderEstimatedDeliveryDate AS order_estimated,
        EXTRACT(
            DAY FROM (
                OrderDeliveredCustomerDate - OrderEstimatedDeliveryDate
            )
        ) AS delay_days
    FROM Orders
    WHERE OrderDeliveredCustomerDate IS NOT NULL
      AND OrderEstimatedDeliveryDate IS NOT NULL
      AND OrderDeliveredCustomerDate > OrderEstimatedDeliveryDate
    ORDER BY delay_days DESC
    """

    df = pd.read_sql(query, engine)
    return df

def get_review_score(engine):

    query = """
     SELECT
        ReviewScore
    FROM OrdersReviews
    WHERE ReviewScore IS NOT NULL
    """

    df = pd.read_sql(query, engine)
    return df

def get_freight_value(engine):

    query = """
    SELECT
       FreightValue, Price, SellerId
    FROM OrderItems
    WHERE FreightValue > Price and FreightValue IS NOT NULL
    """

    df = pd.read_sql(query, engine)
    return df

def get_problematic_sellers(engine):
    query = """
     SELECT
       SellerId, COUNT(DISTINCT oi.OrderId) AS problematic_orders,
        AVG(oi.Price) AS avg_price,
        AVG(oi.FreightValue) AS avg_freight
    FROM OrderItems oi
        JOIN OrdersReviews osr ON oi.OrderId = osr.OrderId
    WHERE ReviewScore < 3 OR (FreightValue > Price and FreightValue IS NOT NULL)
    GROUP BY oi.SellerId
    ORDER BY problematic_orders DESC 
    """

    df = pd.read_sql(query, engine)
    return df

def get_problematic_orders(engine):

    query = """
    SELECT
        oi.OrderId,
        osr.ReviewScore,
        oi.FreightValue,
        oi.Price,
        o.OrderStatus
    FROM OrderItems oi
    JOIN OrdersReviews osr
        ON oi.OrderId = osr.OrderId
    JOIN Orders o
        ON oi.OrderId = o.OrderId
    WHERE
        osr.ReviewScore < 3
        OR (
            oi.FreightValue > oi.Price
            AND oi.FreightValue IS NOT NULL
        )
    """

    return pd.read_sql(query, engine)

def get_canceled_orders(engine):
    query = """
     SELECT
       OrderId, OrderStatus
    FROM Orders
    WHERE OrderStatus = 'canceled'
    """

    df = pd.read_sql(query, engine)
    return df

def get_low_selling_categories(engine):
    query = """     
    SELECT    
       ProductCategoryName, Count(orderid) as Suma
    FROM Products
        JOIN OrderItems ON Products.ProductId = OrderItems.ProductId
    GROUP BY ProductCategoryName 
	ORDER BY  Suma ASC
	LIMIT 10
    """

    df = pd.read_sql(query, engine)
    return df

def get_sales_summary(engine):
    query = """
    SELECT
        COUNT(*) AS total_orders,
        SUM(order_value) AS total_revenue,
        AVG(order_value) AS average_order_value
    FROM (
        SELECT
            OrderId,
            SUM(Price) AS order_value
        FROM OrderItems
        GROUP BY OrderId
    ) AS orders_summary
    """

    df = pd.read_sql(query, engine)
    return df

def get_monthly_revenue(engine):
    query = """
    SELECT
        DATE_TRUNC('month', o.OrderPurchaseTimestamp) AS month,
        COUNT(DISTINCT o.OrderId) AS orders,
        SUM(oi.Price) AS revenue
    FROM Orders o
    JOIN OrderItems oi
        ON o.OrderId = oi.OrderId
    WHERE o.OrderPurchaseTimestamp IS NOT NULL
    GROUP BY DATE_TRUNC('month', o.OrderPurchaseTimestamp)
    ORDER BY month
    """

    df = pd.read_sql(query, engine)
    return df

def get_category_performance(engine):
    query = """
    SELECT
        p.ProductCategoryName,
        COUNT(DISTINCT oi.OrderId) AS orders,
        SUM(oi.Price) AS revenue,
        AVG(oi.Price) AS average_price
    FROM Products p
    JOIN OrderItems oi
        ON p.ProductId = oi.ProductId
    WHERE p.ProductCategoryName IS NOT NULL
    GROUP BY p.ProductCategoryName
    ORDER BY revenue DESC
    """

    df = pd.read_sql(query, engine)
    return df

def get_seller_performance(engine):
    query = """
    SELECT
        SellerId,
        COUNT(DISTINCT OrderId) AS orders,
        SUM(Price) AS revenue,
        AVG(Price) AS average_price,
        AVG(FreightValue) AS average_freight
    FROM OrderItems
    GROUP BY SellerId
    ORDER BY revenue DESC
    """

    df = pd.read_sql(query, engine)
    return df

def get_order_status_summary(engine):
    query = """
    SELECT
        OrderStatus,
        COUNT(*) AS orders,
        ROUND(
            100.0 * COUNT(*) /
            SUM(COUNT(*)) OVER (),
            2
        ) AS percentage
    FROM Orders
    GROUP BY OrderStatus
    ORDER BY orders DESC
    """

    df = pd.read_sql(query, engine)
    return df

def get_delivery_vs_review(engine):
    query = """
    SELECT
        CASE
            WHEN o.OrderDeliveredCustomerDate >
                 o.OrderEstimatedDeliveryDate
            THEN 'Delayed'
            ELSE 'On time'
        END AS delivery_status,

        COUNT(DISTINCT o.OrderId) AS orders,

        ROUND(
            AVG(r.ReviewScore)::numeric,
            2
        ) AS average_review_score

    FROM Orders o

    JOIN OrdersReviews r
        ON o.OrderId = r.OrderId

    WHERE o.OrderDeliveredCustomerDate IS NOT NULL
      AND o.OrderEstimatedDeliveryDate IS NOT NULL
      AND r.ReviewScore IS NOT NULL

    GROUP BY
        CASE
            WHEN o.OrderDeliveredCustomerDate >
                 o.OrderEstimatedDeliveryDate
            THEN 'Delayed'
            ELSE 'On time'
        END

    ORDER BY delivery_status
    """

    df = pd.read_sql(query, engine)
    return df

def get_delivery_summary(engine):
    query = """
    SELECT
        COUNT(*) AS delivered_orders,

        COUNT(
            CASE
                WHEN OrderDeliveredCustomerDate >
                     OrderEstimatedDeliveryDate
                THEN 1
            END
        ) AS delayed_orders,

        ROUND(
            100.0 *
            COUNT(
                CASE
                    WHEN OrderDeliveredCustomerDate >
                         OrderEstimatedDeliveryDate
                    THEN 1
                END
            ) / NULLIF(COUNT(*), 0),
            2
        ) AS delayed_percentage

    FROM Orders

    WHERE OrderDeliveredCustomerDate IS NOT NULL
      AND OrderEstimatedDeliveryDate IS NOT NULL
    """

    df = pd.read_sql(query, engine)
    return df