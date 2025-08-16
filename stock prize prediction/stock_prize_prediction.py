import pandas as pd
import numpy as np

def load_stock_data():
    df = pd.read_csv("stock.csv")
    if "Close" not in df.columns:
        raise ValueError("CSV file must have a 'Close' column.")
    return df["Close"]

def simple_predict(prices, window=5):
    return np.mean(prices[-window:])

def main():
    prices = load_stock_data()

    actual = prices.iloc[-1]
    prediction = simple_predict(prices)

    direction = "UP 📈" if prediction > actual else "DOWN 📉"
    print(f"Last Price: {actual:.2f} | Predicted: {prediction:.2f} | Trend: {direction}")

if __name__ == "__main__":
    main()
