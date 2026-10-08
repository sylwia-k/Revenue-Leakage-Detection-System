from src.database.connections import engine

from src.analysis.analysis import (
    get_delayed_orders,
    get_review_score,
    get_freight_value,
    get_problematic_sellers,
    get_problematic_orders,
    get_canceled_orders,
    get_low_selling_categories,
    get_sales_summary,
    get_monthly_revenue,
    get_category_performance,
    get_seller_performance,
    get_order_status_summary,
    get_delivery_vs_review,
    get_delivery_summary,
)


def main():

    print("=" * 60)
    print("OLIST E-COMMERCE DATA ANALYSIS")
    print("=" * 60)

    print("\n--- SALES SUMMARY ---")

    sales = get_sales_summary(engine)
    print(sales.to_string(index=False))


    print("\n--- MONTHLY REVENUE ---")

    monthly_revenue = get_monthly_revenue(engine)
    print(monthly_revenue.head(10).to_string(index=False))


    print("\n--- CATEGORY PERFORMANCE ---")

    categories = get_category_performance(engine)
    print(categories.head(10).to_string(index=False))

    print("\n--- SELLER PERFORMANCE ---")

    sellers = get_seller_performance(engine)
    print(sellers.head(10).to_string(index=False))


    print("\n--- ORDER STATUS ---")

    order_status = get_order_status_summary(engine)
    print(order_status.to_string(index=False))


    print("\n--- DELIVERY SUMMARY ---")

    delivery = get_delivery_summary(engine)
    print(delivery.to_string(index=False))


    print("\n--- DELIVERY VS REVIEW ---")

    delivery_review = get_delivery_vs_review(engine)
    print(delivery_review.to_string(index=False))


    print("\n--- LOW SELLING CATEGORIES ---")

    low_categories = get_low_selling_categories(engine)
    print(low_categories.to_string(index=False))


    print("\n--- PROBLEMATIC SELLERS ---")

    problematic_sellers = get_problematic_sellers(engine)
    print(problematic_sellers.head(10).to_string(index=False))


    print("\n--- PROBLEMATIC ORDERS ---")

    problematic_orders = get_problematic_orders(engine)
    print(problematic_orders.head(10).to_string(index=False))

   
    print("\n--- CANCELED ORDERS ---")

    canceled_orders = get_canceled_orders(engine)
    print(canceled_orders.head(10).to_string(index=False))


    print("\n--- DELAYED ORDERS ---")

    delayed_orders = get_delayed_orders(engine)
    print(delayed_orders.head(10).to_string(index=False))


    print("\n--- REVIEW SCORES ---")

    review_scores = get_review_score(engine)
    print(review_scores.head(10).to_string(index=False))


    print("\n--- HIGH FREIGHT VALUE ---")

    freight = get_freight_value(engine)
    print(freight.head(10).to_string(index=False))

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()