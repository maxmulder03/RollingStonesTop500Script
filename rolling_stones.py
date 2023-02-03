import asyncio
from pyppeteer import launch

# Pyppeteer Docs: https://github.com/pyppeteer/pyppeteer
# DOM Selectors: https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors

urls = ["https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/rufus-chaka-khan-ask-rufus-1062734/"]

ranking_htmlClassSelector = ".c-gallery-vertical-album__number"

# Result is comma seperate ex: Taylor Swift, "RED"
artist_album_htmlClassSelector = ".c-gallery-vertical-album__title"

async def main():
    for url in urls:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        # NodeList of Values
        ranking_items = await page.querySelectorAll(ranking_htmlClassSelector)
        # NodeList of Values
        artist_album_items = await page.querySelectorAll(artist_album_htmlClassSelector)
        print(ranking_items)
        
        for ranking, artist_album in zip(ranking_items, artist_album_items):
            rank_text = await (await ranking.getProperty('textContent')).jsonValue()
            artist_album_text = await (await artist_album.getProperty('textContent')).jsonValue()    
            print(rank_text + " -> " + artist_album_text)
        
    return 

asyncio.get_event_loop().run_until_complete(main())