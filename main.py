import os
import asyncio
import sys
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, GiftEvent

# Retrieve the TikTok handle from Railway environment variables (or use default)
TIKTOK_HANDLE = os.getenv("TIKTOK_HANDLE", "roblox_dev_name_dionn001")

# Initialize the TikTok Live client
client: TikTokLiveClient = TikTokLiveClient(unique_id=TIKTOK_HANDLE)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"[SYSTEM] Connected to {event.unique_id}'s livestream!")


@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    # Check if the gift streak has ended or if it is a non-streakable gift
    if event.gift.streakable and not event.streaking:
        print(f"[GIFT] Thank you {event.user.nickname} for sending {event.repeat_count}x {event.gift.name}!")
    elif not event.gift.streakable:
        print(f"[GIFT] Thank you {event.user.nickname} for sending a {event.gift.name}!")


async def cmd_listener():
    # Check if a real interactive terminal/keyboard is available
    if not sys.stdin.isatty():
        print("[CMD] Running in headless environment (Railway). Terminal commands are disabled, monitoring gifts only.")
        # Keep this coroutine running safely in the background
        await asyncio.Event().wait()
        return

    print("[CMD] Interactive terminal ready! Type a command starting with '/' (e.g. /help, /stop):")
    loop = asyncio.get_running_loop()
    
    while True:
        try:
            user_input = await loop.run_in_executor(None, input, "> ")
        except (EOFError, RuntimeError):
            break
            
        command = user_input.strip().lower()

        if command == "/stop":
            print("[CMD] Shutting down bot. Goodbye!")
            await client.disconnect()
            break
        elif command == "/hello":
            print("[BOT] Hey! Ready to stream and save up for GTA 6!")
        elif command == "/status":
            print(f"[BOT] Monitoring livestream for: {TIKTOK_HANDLE}")
        elif command == "/help":
            print("[BOT] Available commands: /hello, /status, /stop")
        elif command == "":
            continue
        else:
            print(f"[BOT] Unknown command: '{command}'. Type '/help' for options.")


async def main():
    # Run both the TikTok client and the CMD listener at the same time
    await asyncio.gather(
        client.start(),
        cmd_listener()
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[SYSTEM] Bot stopped manually.")
