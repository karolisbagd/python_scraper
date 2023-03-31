from fold1.booking import Booking
import time


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    time.sleep(3)
    bot.select_place_to_go("Lithuania")
    time.sleep(3)
    bot.click_search()
