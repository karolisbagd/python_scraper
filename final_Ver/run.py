from main import SocialMedia
import psutil

with SocialMedia() as bot:



   bot.open_html_file("w")  # Open the HTML file in write mode

   bot.twitter_load_page()
   bot.twitter_input_email()
   bot.twitter_input_password()
   bot.twitter_button_login()
   bot.twitter_click_profile()
   bot.tweet_results()

   bot.end_html_file()  # Close the HTML file after writing all the tweets

   '''bot.facebook_load_page()
   bot.facebook_login_page()
   bot.facebook_click_profile()

   bot.open_html_file("a")  # Open the HTML file in append mode

   bot.scrape_posts()
  
   bot.end_html_file()  # Close the HTML file after writing all the posts'''

    # Get CPU and memory usage
   # cpu_percent = process.cpu_percent()
   # memory_usage = process.memory_info().rss / 1024 / 1024  # in MB        
    
  #  print(f"CPU usage: {cpu_percent}%")
   # print(f"Memory usage: {memory_usage} MB")
