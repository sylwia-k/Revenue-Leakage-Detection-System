from src.database.connections import engine
from src.analysis.analysis import get_delayed_orders


def main():

    print("Starting analysis...")

    df = get_delayed_orders(engine)

    print(df.head())
    print(f"\nDelayed orders: {len(df)}")


if __name__ == "__main__":
    main()