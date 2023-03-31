from main import Twitter

with Twitter() as bot:
    bot.load_page()
    bot.input_email()
    bot.input_password()
    bot.button_login()
    bot.click_profile()
    print(bot.tweet_results())
    #print(len(bot.tweet_results()))  # Need to check Console?
