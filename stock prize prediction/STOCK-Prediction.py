import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

def head(df,n) :
    return df.head(n)

def tail(df,n):
    return df.tail(n)

def information(df):
    print(df.shape)
    print(df.dtypes)
    print(df.info())

def description(df):
    return df.describe(include="all").T

def plots_with_outliers_removed(df):
    col_name = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]  # exclude Date
    df_no_outliers = df.copy(deep=True)

    while True:
        total_outliers = 0

        for col in col_name:
            while True:
                # Calculate Q25 and Q75
                q25, q75 = np.percentile(df_no_outliers[col], [25, 75])
                iqr = q75 - q25
                min_val = q25 - (iqr * 1.5)
                max_val = q75 + (iqr * 1.5)

                # Find outliers for this column
                outliers = df_no_outliers[(df_no_outliers[col] < min_val) |
                                          (df_no_outliers[col] > max_val)][col]

                count = len(outliers)
                print(f"Outliers in {col} = {count}")

                if count == 0:
                    break  # column is clean → go to next column

                # Remove outliers and continue until 0
                df_no_outliers = df_no_outliers[~df_no_outliers[col].isin(outliers)]
                total_outliers += count

        # If no outliers left in ANY column, stop
        if total_outliers == 0:
            break

    df = df_no_outliers.reset_index(drop=True)
    print("Final shape after outliers removed:", df.shape)

    print("\nSelect desired plot\n 1.Histogram\n 2.Boxplot\n 3.Lineplot\n")
    choice=int(input("Enter your choice: "))

    plt.figure(figsize=(10, 5))

    if choice==1:
        print("Columns available to be selected as x_axis = [Open, High, Low, Close, Adj Close, Volume]\n")
        x_axis=input("Enter Column Name on x_axis: ")

        if x_axis in col_name:
            sb.histplot(data=df, x=x_axis, kde= True, color="r")
            plt.title("Histogram")
            plt.xlabel(x_axis)
            plt.ylabel("Frequency")
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==2:
        print("Columns available to be selected as x_axis = [Open, High, Low, Close, Adj Close, Volume]\n")
        x_axis = input("Enter Column Name on x_axis: ")

        if x_axis in col_name:
            sb.boxplot(data=df, x=x_axis, color="b")
            plt.title("Box-Plot")
            plt.xlabel(x_axis)
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==3:
        print("Columns available to be selected as x_axis = [Open, High, Low, Close, Adj Close, Volume]\n")
        x_axis = input("Enter Column Name on x_axis: ")

        if x_axis in col_name:
            sb.lineplot(data=df, x="Date", y=x_axis, color="g",errorbar=('ci',False))
            plt.title("Line-Plot")
            plt.xlabel("Date")
            plt.ylabel(x_axis)
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    else:
        print("WRONG CHOICE")

df=pd.read_csv("stock-prediction.csv")
print("\nColumns are = [Date, Open, High, Low, Close, Adj Close, Volume]\n ")

print("OPTIONS:\n 1.Print first N Rows\n 2.Print last N Rows\n 3.Show Plots (Outliers Removed)\n 4.Future Stock Prediction\n")
choice1=int(input("Enter Your Choice: "))

if choice1==1:
    N=int(input("Enter number of rows to be printed: "))
    print(head(df,N))

elif choice1==2:
    N = int(input("Enter number of rows to be printed: "))
    print(tail(df, N))

elif choice1==3:
    print("\nOutlier Removal :\n")
    plots_with_outliers_removed(df)

elif choice1==4:
    def check_Close_column():
        if "Close" not in df.columns:
            raise ValueError("CSV file must have a 'Close' column.")
        return df["Close"]


    def simple_predict(prices, window=5):
        return np.mean(prices[-window:])


    def main():
        prices = check_Close_column()

        actual = prices.iloc[-1]
        prediction = simple_predict(prices)

        direction = "UP 📈" if prediction > actual else "DOWN 📉"
        print(f"Last Price: {actual:.2f} | Predicted: {prediction:.2f} | Trend: {direction}")


    if __name__ == "__main__":
        main()

else:
    print("WRONG CHOICE")