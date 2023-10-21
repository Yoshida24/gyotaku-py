from modules.reservation import snapshot

import asyncio


async def main():
    await snapshot.post()


if __name__ == "__main__":
    asyncio.run(main())
