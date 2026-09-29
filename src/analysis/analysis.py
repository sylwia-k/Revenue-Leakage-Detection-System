import pandas as pd

def get_delayed_orders(engine):

    query = """
    SELECT
        orderdeliveredcustomerdate order_delivered,
        orderestimateddeliverydate order_estimated
    FROM orders
    WHERE orderdeliveredcustomerdate IS NOT NULL
    AND orderdeliveredcustomerdate > orderestimateddeliverydate
    """

    df = pd.read_sql(query, engine)
    return df
