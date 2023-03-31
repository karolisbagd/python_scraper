from main import Twitter

with Twitter() as twitter:
    twitter.load_page()
    twitter.input_email()
    twitter.input_password()
    twitter.button_login()
    twitter.click_profile()
    print(twitter.tweet_results())
    twitter.quit()