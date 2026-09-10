from looger import get_logger
import csv
import pandas as pd

def read_csv():
    # Step 1: specify the path to your CSV
    file_path = "CSV_file/banking.csv"

    # Step 2: read it into a DataFrame
    df = pd.read_csv(file_path)

    # Step 3: return it so whoever calls this function can use it
    return df

def main():
    data = read_csv()
    print(data.head())
    print(data.shape)


if __name__ == "__main__":
    main()
