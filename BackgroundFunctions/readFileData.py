import csv

import pandas as pd

from BackgroundFunctions.loadObjFile import config_parser

config = config_parser()


def read_file(filepath):
    colnames = ["Category", "Product"]
    df = pd.read_csv(filepath, names=colnames, skiprows=[0], on_bad_lines='skip', encoding="utf-8", nrows=1000)
    # mean_usage_b = df.memory_usage(deep=True).mean()
    # mean_usage_mb = mean_usage_b / 1024 ** 2
    pd.options.display.max_colwidth = 100000
    return df


def write_file(filepath):
    colnames = ["Products", "Category Names"]
    df = pd.read_csv(filepath, names=colnames, on_bad_lines='skip', encoding="utf-8", nrows=1000)
    # mean_usage_b = df.memory_usage(deep=True).mean()
    # mean_usage_mb = mean_usage_b / 1024 ** 2
    pd.options.display.max_colwidth = 100000
    return df


def getURL_List():
    try:
        # Read URLs from CSV file
        df = pd.read_csv(config['filePath']['csv_file_path'])
        # Assuming the URL column is named 'URL', adjust if different
        urls = df['URL'].tolist()
        return urls
    except Exception as e:
        print(f"Error reading URLs from CSV: {e}")
        return []
