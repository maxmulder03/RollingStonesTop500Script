import asyncio
from pyppeteer import launch

# Pyppeteer Docs: https://github.com/pyppeteer/pyppeteer
# DOM Selectors: https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors

urls = ["https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/rufus-chaka-khan-ask-rufus-1062734/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/linda-mccartney-and-paul-ram-1062783/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-go-gos-beauty-and-the-beat-1062833/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/stevie-wonder-music-of-my-mind-2-1062883/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/shania-twain-come-on-over-1062933/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/buzzcocks-singles-going-steady-2-1062983/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/sade-diamond-life-1063033/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/bruce-springsteen-nebraska-3-1063083/", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-band-music-from-big-pink-2-1063133", "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/jay-z-the-blueprint-3-1063183/"]

ranking_htmlClassSelector = ".c-gallery-vertical-album__number"

# Result is comma seperate ex: Taylor Swift, "RED"
artist_album_htmlClassSelector = ".c-gallery-vertical-album__title"

async def main():
    f = open("output.txt", "a")
    i = 0
    for url in urls:
        browser = await launch()
        page = await browser.newPage()
        page.setDefaultNavigationTimeout(0)
        await page.goto(url)
        
        # NodeList of Values
        ranking_items = await page.querySelectorAll(ranking_htmlClassSelector)
        # NodeList of Values
        artist_album_items = await page.querySelectorAll(artist_album_htmlClassSelector)
        
        for ranking, artist_album in zip(ranking_items, artist_album_items):
            rank_text = await (await ranking.getProperty('textContent')).jsonValue()
            artist_album_text = await (await artist_album.getProperty('textContent')).jsonValue()    
            # Write as comma seperated string (rank, artist, album)
            f.write(rank_text + ", " + artist_album_text + "\n")
    f.close()
    return 

asyncio.get_event_loop().run_until_complete(main())