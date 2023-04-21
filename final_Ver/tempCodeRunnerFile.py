    post_texts = []

        # Scroll down the webpage
        self.execute_script("window.scrollBy(0, 700);")
        self.implicitly_wait(5)

        # Locate all the post elements on the page
        post_elements = self.find_elements(
            By.XPATH, ".//div[@data-pagelet='ProfileTimeline']")

        print("Scraping post from the timeline")
        time.sleep(2)

        print(f"Number of post elements: {len(post_elements)}")

        for post_element in post_elements:
            post_text_element = post_element.find_element(
                By.XPATH, ".//div[@class='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r']").text
            self.implicitly_wait(5)
            time_element = post_element.find_element(
                By.XPATH, ".//a[@role='link']/span").text
            self.implicitly_wait(5)

            post_texts.append(
                {"Text": post_text_element, "Posted": time_element})

        return post_texts  # Return the text of all the posts