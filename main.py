import os
import asyncio
import sys
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, GiftEvent, ChatEvent

# Retrieve the TikTok handle from Railway environment variables (or use default)
TIKTOK_HANDLE = os.getenv("TIKTOK_HANDLE", "roblox_dev_name_dionn001")

# Initialize the TikTok Live client
client: TikTokLiveClient = TikTokLiveClient(unique_id=TIKTOK_HANDLE)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"[SYSTEM] Connected to {event.unique_id}'s livestream!")


@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    if event.gift.streakable and not event.streaking:
        print(f"[GIFT] Thank you {event.user.nickname} for sending {event.repeat_count}x {event.gift.name}!")
    elif not event.gift.streakable:
        print(f"[GIFT] Thank you {event.user.nickname} for sending a {event.gift.name}!")


@client.on(ChatEvent)
async def on_chat(event: ChatEvent):
    # Check if a viewer types a command starting with '/' in the TikTok chat
    message = event.comment.strip().lower()
    user = event.user.nickname
    
    if message == "/hello":
        print(f"[CHAT CMD] {user} used /hello in TikTok chat!")
    elif message == "/status":
        print(f"[CHAT CMD] {user} checked status. Monitoring: {TIKTOK_HANDLE}")
    elif message == "/help":
        print(f"[CHAT CMD] {user} requested help via TikTok chat.")


async def main():
    # Run the TikTok client continuously
    await client.start()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[SYSTEM] Bot stopped manually.")
