# utils/telegram_utils.py

import csv

def save_scraped_data(channel, data):
    """Save scraped data into a CSV file."""
    
    # Remove the "@" from the channel name for file naming
    file_path = f'data/{channel.replace("@", "")}_messages.csv'
    
    # Save the data into a CSV file
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['message', 'date', 'sender'])
        writer.writeheader()
        writer.writerows(data)
