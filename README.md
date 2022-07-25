# Leetcode Scraping by Problem Tags

I needed to scrape a few websites for the purpose of my work, and until I had to, I only knew how to scrape using Beautiful Soup (BS). However, I soon ran into problems:
1. Most websites have buttons that we need to click which BS doesn't let you do
2. Most contents these days are loaded with JS, and if the content isn't loaded when a BS scrapper runs, the BS scrapper will not find the html elements you are looking for. 

As a result I came across Selenium which lets you mimic button clicks and also lets you set a timer for JS content to load before you perform action. I created several scrappers using Selenium and decided to make one available for anyone to use the script. 

## How to run the scrapper:

1. Clone the repository using `git clone https://github.com/farhan0167/leetcode-scraping`
2. In the `leetcode-scrapping` directory, download [Chrome Driver](https://chromedriver.chromium.org/downloads). Mark the location of where chromedriver.exec file is located
3. Open `leetcode.py` and in line 11, change the PATH to ` './leetcode-scrapping/chromedriver' ` or wherever your chromedriver.exec file was located. As you can see, mine was located in `"/Users/farhanishraq/Downloads/Summer 2022/chromedriver"`
4. In line 14, change the url if you want to scrape problems from other tags.
5. In your terminal, activate the virtual environment by typing `source env/bin/activate` from the `leetcode-scrapping` directory. 
6. Now you can run `python leetcode.py` and you'll find the scrapper do its magic. 
7. In the event the scrapper fails, you can re-try. If problems still persist, please reach out to me.

