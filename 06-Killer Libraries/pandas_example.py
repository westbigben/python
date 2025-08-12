"""Pandas example — read sample_data.csv, compute total revenue and top categories."""
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "sample_data.csv"

def main():
    print("Pandas demo — reading:", DATA)
    df = pd.read_csv(DATA)
    # add revenue column
    df['revenue'] = df['price'] * df['quantity_sold']
    print("\nFull table:")
    print(df.to_string(index=False))
    # aggregate by category
    agg = df.groupby('category', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
    print("\nRevenue by category:")
    print(agg.to_string(index=False))
    # top product by revenue
    top = df.loc[df['revenue'].idxmax()]
    print("\nTop product by revenue:")
    print(top.to_string())

if __name__ == '__main__':
    main()
