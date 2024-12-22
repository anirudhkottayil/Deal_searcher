from Deals.Deal_searcher import Deal_searcher
import time

with Deal_searcher() as bot:
    bot.load_first_page("https://www.ozbargain.com.au/deals")
    time.sleep(4)