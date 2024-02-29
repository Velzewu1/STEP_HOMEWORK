"""Task1"""
from pathlib import Path
import asyncio
import requests
import aiohttp
import aiofiles

def write_img(url, path):
    """Gets image using requests"""
    parent_dir_path = Path(path)
    try:
        parent_dir_path.mkdir(parents=True)
    except FileExistsError:
        pass
    finally:
        response = requests.get(url , timeout=200).json()
        iter_count = 1
        for to_write in response:
            file_path = parent_dir_path / f"json{iter_count}.txt"
            with open(file_path, mode="w", encoding="utf-8") as file:
                file.write(str(to_write))
            iter_count += 1

async def async_img(url, path):
    """Gets image using requests and aiohttp"""
    parent_dir_path = Path(path)
    try:
        parent_dir_path.mkdir(parents=True)
    except FileExistsError:
        pass
    finally:
        iter_count = 1
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                for response in await resp.json():
                    file_path = parent_dir_path / f"img{iter_count}.txt"
                    async with aiofiles.open(file_path, mode="w+", encoding="utf-8") as file:
                        await file.write(str(response))
                    iter_count += 1
if __name__ == "__main__":
    # write_img('https://jsonplaceholder.typicode.com/todos/', "sync_dir")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_img('https://jsonplaceholder.typicode.com/todos/', "async_dir"))
