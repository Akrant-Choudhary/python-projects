import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

def head(df,n) :
    return df.head(n)

def tail(df,n):
    return df.tail(n)

def shape(df):
    print(df.shape)

def information(df):
    print(df.dtypes)
    print(df.info())

def description(df):
    print(df.describe(include="all").T)

def remove_outliers(df):
    col_name = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
                "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]

    while True:
        total_outliers = 0

        for col in col_name:
            while True:
                # Calculate Q25 and Q75
                q25, q75 = np.percentile(df[col], [25, 75])
                iqr = q75 - q25
                min_val = q25 - (iqr * 1.5)
                max_val = q75 + (iqr * 1.5)

                # Find outliers for this column
                outliers = df[(df[col] < min_val) | (df[col] > max_val)][col]

                count = len(outliers)
                print(f"Outliers in {col} = {count}")

                if count == 0:
                    break  # column is clean → go to next column

                # Remove outliers inplace
                df.drop(outliers.index, inplace=True)
                total_outliers += count

        # If no outliers left in ANY column, stop
        if total_outliers == 0:
            break

    # Reset index after removing rows
    df.reset_index(drop=True, inplace=True)
    print("Final shape after outliers removed:", df.shape)
    print()


def remove_null(df):
    df.dropna(inplace=True)

def remove_null_values_and_outliers(df):
    print("Before Removal :\n")
    print(df.isna().sum())
    print("\nAfter removal :\n")
    df.dropna(inplace=True)
    print(df.isna().sum())
    remove_outliers(df)

    print("Select:\n 1.Shape\n 2.Information\n 3.Description\n")
    choice=int(input("Enter choice: "))

    if choice==1:
        shape(df)

    elif choice==2:
        information(df)

    elif choice==3:
        description(df)

    else:
        print("Invalid choice")

def plots(df):
    remove_outliers(df)
    col_name = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides","free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]
    print("\nSelect desired plot\n 1.Histogram\n 2.Boxplot\n 3.Lineplot\n 4.Scatter-Plot\n 5.Pairplot\n 6.Heatmap\n")
    choice = int(input("Enter your choice: "))

    if choice==1:
        print("Columns available to be selected as x_axis = [fixed acidity, volatile acidity, citric acid, residual sugar, chlorides,free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality]\n")
        x_axis=input("Enter Column Name on x_axis: ")

        if x_axis in col_name:
            plt.figure(figsize=(10, 5))
            sb.histplot(data=df, x=x_axis, kde= True, color="r")
            plt.title("Histogram")
            plt.xlabel(x_axis)
            plt.ylabel("Frequency")
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==2:
        print("Columns available to be selected as x_axis = [fixed acidity, volatile acidity, citric acid, residual sugar, chlorides,free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality]\n")
        x_axis = input("Enter Column Name on x_axis: ")

        if x_axis in col_name:
            plt.figure(figsize=(10, 5))
            sb.boxplot(data=df, x=x_axis, color="b")
            plt.title("Box-Plot")
            plt.xlabel(x_axis)
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==3:
        print("Columns available to be selected as x_axis = [fixed acidity, volatile acidity, citric acid, residual sugar, chlorides,free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality]\n")
        x_axis = input("Enter Column Name on x_axis: ")
        y_axis = input("Enter Column Name on y_axis: ")

        if x_axis in col_name:
            plt.figure(figsize=(10, 5))
            sb.lineplot(data=df, x=x_axis, y=y_axis, color="g",errorbar=('ci',False))
            plt.title("Line-Plot")
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==4:
        print("Columns available to be selected as x_axis = [fixed acidity, volatile acidity, citric acid, residual sugar, chlorides,free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality]\n")
        x_axis = input("Enter Column Name on x_axis: ")
        y_axis = input("Enter Column Name on y_axis: ")

        if x_axis in col_name and y_axis in col_name:
            plt.figure(figsize=(10, 5))
            sb.scatterplot(data=df, x=x_axis, y=y_axis, color="g")
            plt.title("Scatter-Plot")
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.show()

        else:
            print("INVALID COLUMN NAME")

    elif choice==5:
        g = sb.pairplot(data=df, kind="scatter", diag_kind="hist", corner=True, height=1.5)
        plt.title("Pair-Plot")
        plt.show()

    elif choice==6:
        plt.figure(figsize=(10, 5))
        sb.heatmap(data=df.corr(), annot=True, cmap="coolwarm")
        plt.title("HeatMap")
        plt.show()

    else:
        print("WRONG CHOICE")

def quality(df):
    remove_null(df)
    remove_outliers(df)
    print(df["quality"].value_counts())

df=pd.read_csv("Wine-quality-analysis.csv")
print("\nColumns are = [fixed acidity, volatile acidity, citric acid, residual sugar, chlorides,free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality]\n ")

print("\nCategorise Wine: ")
print(" 1.Poor=4\n 2.Normal=5\n 3.Good=6\n 4.Excellent=7\n")

print("OPTIONS:\n 1.Print first N Rows\n 2.Print last N Rows\n 3.Remove null values & outliers and show further information\n 4.Show Plots (Outliers Removed)\n 5.Wine Quality Analysis ")
choice1=int(input("Enter Your Choice: "))

if choice1==1:
    N=int(input("Enter number of rows to be printed: "))
    print(head(df,N))

elif choice1==2:
    N = int(input("Enter number of rows to be printed: "))
    print(tail(df,N))

elif choice1==3:
    remove_null_values_and_outliers(df)

elif choice1==4:
    print("\nOutlier Removal :\n")
    plots(df)

elif choice1==5:
    quality(df)
    print("\nCategorise Wine: ")
    print(" 1.Poor=4\n 2.Normal=5\n 3.Good=6\n 4.Excellent=7\n")

else:
    print("WRONG CHOICE MADE")
