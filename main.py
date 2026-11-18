import os
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, GiftEvent, CommentEvent

TIKTOK_HANDLE = os.getenv("TIKTOK_HANDLE", "roblox_dev_name_dionn001")

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

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    print(f"[CHAT DEBUG] {event.user.nickname}: {event.comment}")
    
    message = event.comment.strip().lower()
    user = event.user.nickname
    
    if message == "/hello":
        print(f"[CHAT CMD] {user} used /hello in TikTok chat!")
    elif message == "/status":
        print(f"[CHAT CMD] {user} checked status. Monitoring: {TIKTOK_HANDLE}")
    elif message == "/help":
        print(f"[CHAT CMD] {user} requested help via TikTok chat.")

if __name__ == "__main__":
    put hear client.run() and stop the weding i mean del del del 
