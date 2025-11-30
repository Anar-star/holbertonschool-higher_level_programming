#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Converts a CSV file to JSON format and saves it as data.json.
    
    Args:
        csv_filename (str): The CSV file to read.
        
    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
