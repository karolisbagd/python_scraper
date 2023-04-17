from main import SocialMedia

with SocialMedia() as bot:

    '''bot.twitter_load_page()
    bot.twitter_input_email()
    bot.twitter_input_password()
    bot.twitter_button_login()
    bot.twitter_click_profile()
    print(bot.tweet_results())'''

    print("\nChanging to Facebook\n")

    bot.facebook_load_page()
    bot.facebook_login_page()
    bot.facebook_click_profile()
    print(bot.scrape_posts())
    post_data = bot.scrape_posts()
    print(len(post_data))
