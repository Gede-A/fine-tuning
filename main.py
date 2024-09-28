# main.py

from telethon import TelegramClient
from config.credentials import api_id, api_hash
from config.settings import CHANNELS_TO_SCRAPE, SCRAPE_LIMIT
from utils.telegram_utils import save_scraped_data
# Initialize Telegram client with session name
client = TelegramClient('session_name', api_id, api_hash)
async def scrape_messages():
    async with client:
        for channel in CHANNELS_TO_SCRAPE:
            try:
                # Fetch messages from the channel
                messages = await client.get_messages(channel, limit=SCRAPE_LIMIT)
                # Extract message text and other relevant info
                data = [{'message': msg.text, 'date': msg.date, 'sender': msg.sender_id} for msg in messages if msg.text]
                # Save the scraped data
                save_scraped_data(channel, data)
                print(f"Successfully scraped {len(data)} messages from {channel}")
            except Exception as e:
                print(f"An error occurred while scraping {channel}: {e}")

if __name__ == "__main__":
    # Run the scrape_messages function
    client.loop.run_until_complete(scrape_messages())
