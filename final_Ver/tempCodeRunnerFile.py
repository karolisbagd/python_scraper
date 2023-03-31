from main import SocialMedia

with SocialMedia() as bot:
    bot.load_page()
    bot.twitter_input_email()
    bot.input_password()
    bot.twitter_button_login()
    bot.twitter_click_profile()
    print(bot.tweet_results())
    # print(len(bot.tweet_results()))  # Need to check Console?
