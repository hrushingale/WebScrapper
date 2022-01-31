# WebScrapper
1.	The folder ‘webCrawlerAssignment’ is a PyCharm Project. Open it using PyCharm.
2.	In this project, I have created a Web Crawler using Python and Scrapy to scrap data from the webpage ‘https://www.house.gov/representatives’ into a JSON file.
3.	From the Project tab, navigate to the ‘pscrape’ folder and open ‘posts_spider.py’ in PyCharm.
4.	Open the terminal in PyCharm. Enter the ‘pscrape’ folder through the terminal using ‘cd pscrape’. Then type in ‘scrapy crawl –o posts.json’ to export the JSON file. The file will be exported to ‘\pscrape\’ folder.
5.	In case your system doesn’t have scrapy installed, proceed with the following steps before executing Step 3:
      a.	Open the terminal in PyCharm. Install scrapy using command ‘pip install scrapy’. (In case your system doesn’t recognize pip command, please add the pip location (“[Python Installation Directory]\Scripts”) to the Environment Variables PATH)
      b.	Once Scrapy is installed, follow Step 3.
6.	In the end, ‘posts.json’ will be exported to the ‘pscrape’ folder.

