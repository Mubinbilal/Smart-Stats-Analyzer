import numpy as np
import pandas as pd

def get_user_input():
    data = input("Enter numbers separated by spaces: ")
    try:
        numbers = list(map(float, data.split()))
        return numbers
    except ValueError:
        print("Invalid input! Please enter only numbers.")
        return get_user_input()

def numpy_operations(numbers):
    arr = np.array(numbers)

    print("\n--- NumPy Operations ---")
    print("Array:", arr)
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    
    
    mode = pd.Series(arr).mode().values
    print("Mode:", mode)

    print("Standard Deviation:", np.std(arr))
    print("Variance:", np.var(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))
    print("Sum:", np.sum(arr))

def pandas_operations(numbers):
    df = pd.DataFrame(numbers, columns=["Numbers"])

    print("\n--- Pandas Operations ---")
    print("\nDataFrame:\n", df)

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nValue Counts (Frequency):")
    print(df["Numbers"].value_counts())

    # Adding a new column
    df["Squared"] = df["Numbers"] ** 2
    print("\nDataFrame with Squared Values:\n", df)

def main():
    print("📊 Data Analysis Tool using NumPy & Pandas")
    numbers = get_user_input()

    numpy_operations(numbers)
    pandas_operations(numbers)

if __name__ == "__main__":
    main()