import os
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, GiftEvent

TIKTOK_HANDLE = os.getenv("TIKTOK_HANDLE", "roblox_dev_name_dionn001")

client: TikTokLiveClient = TikTokLiveClient(unique_id=TIKTOK_HANDLE)

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to {event.unique_id}'s livestream!")

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    if event.gift.streakable and not event.streaking:
        print(f"{event.user.nickname} sent {event.repeat_count}x {event.gift.name}!")
    elif not event.gift.streakable:
        print(f"{event.user.nickname} sent a {event.gift.name}!")

if __name__ == '__main__':
    client.run()
