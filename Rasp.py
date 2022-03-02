from autoscraper import AutoScraper

url = ("https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/ref=sr_1_4?crid=2TZ2Z1WPKWWZT&keywords=raspberry+pi+4&qid=1646173399&sprefix=ras%2Caps%2C115&sr=8-4")

wanted_list = ['124,90']

scraper = AutoScraper()

scraper.build(url, wanted_list)

scraper.get_result_exact('https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/ref=sr_1_4?crid=2TZ2Z1WPKWWZT&keywords=raspberry+pi+4&qid=1646173399&sprefix=ras%2Caps%2C115&sr=8-4')

scraper.save('rasp_scraper')

print(scraper.get_result_exact('https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TD42S27/ref=sr_1_4?crid=2TZ2Z1WPKWWZT&keywords=raspberry+pi+4&qid=1646173399&sprefix=ras%2Caps%2C115&sr=8-4'))