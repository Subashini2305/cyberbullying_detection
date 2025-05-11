import asyncio
from twscrape.api import API
from twscrape.logger import set_log_level

# Optional: Suppress debug logs
set_log_level("WARNING")

async def main():
    api = API()  # Initializes with saved session
    await api.init()  # Required before using the API

    print("🔍 Searching tweets with hashtag #AI...\n")
    tweets = await api.search("#AI", limit=5)

    for i, tweet in enumerate(tweets, 1):
        print(f"{i}. 🧠 User: @{tweet.user.username}")
        print(f"🕒 Date: {tweet.date}")
        print(f"💬 Tweet: {tweet.rawContent}")
        print(f"🔗 Link: https://twitter.com/{tweet.user.username}/status/{tweet.id}")
        print("-" * 100)

asyncio.run(main())
