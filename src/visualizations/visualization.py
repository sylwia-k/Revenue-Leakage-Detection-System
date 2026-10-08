import matplotlib.pyplot as plt
from pathlib import Path

from src.database.connections import engine
from src.analysis.analysis import (
    get_monthly_revenue,
    get_category_performance,
    get_seller_performance,
    get_order_status_summary,
    get_delivery_vs_review,
    get_review_score,
)


OUTPUT_DIR = Path("reports/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_monthly_revenue():
    df = get_monthly_revenue(engine)

    df["month"] = df["month"].astype(str).str[:7]

    plt.figure(figsize=(12, 6))
    plt.plot(df["month"], df["revenue"])
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close()


def save_top_categories():
    df = get_category_performance(engine).head(10)

    df = df.sort_values("revenue")

    plt.figure(figsize=(10, 6))
    plt.barh(df["productcategoryname"], df["revenue"])
    plt.title("Top 10 Product Categories by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Product Category")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_categories.png", dpi=150)
    plt.close()


def save_top_sellers():
    df = get_seller_performance(engine).head(10)

    df = df.sort_values("revenue")

    plt.figure(figsize=(10, 6))
    plt.barh(df["sellerid"].astype(str), df["revenue"])
    plt.title("Top 10 Sellers by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Seller")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_sellers.png", dpi=150)
    plt.close()


def save_order_status():
    df = get_order_status_summary(engine)

    plt.figure(figsize=(9, 6))
    plt.bar(df["orderstatus"], df["percentage"])
    plt.title("Order Status Distribution")
    plt.xlabel("Order Status")
    plt.ylabel("Percentage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "order_status.png", dpi=150)
    plt.close()


def save_delivery_vs_review():
    df = get_delivery_vs_review(engine)

    plt.figure(figsize=(8, 6))
    plt.bar(
        df["delivery_status"],
        df["average_review_score"],
    )
    plt.title("Delivery Status vs Average Review Score")
    plt.xlabel("Delivery Status")
    plt.ylabel("Average Review Score")
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "delivery_vs_review.png", dpi=150)
    plt.close()


def save_review_distribution():
    df = get_review_score(engine)

    counts = df["reviewscore"].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("Review Score Distribution")
    plt.xlabel("Review Score")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "review_distribution.png", dpi=150)
    plt.close()


def main():
    print("Generating visualizations...")

    save_monthly_revenue()
    save_top_categories()
    save_top_sellers()
    save_order_status()
    save_delivery_vs_review()
    save_review_distribution()

    print(f"Charts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
