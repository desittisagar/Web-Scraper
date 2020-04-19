# Web-Scraper
#Source from "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv" Tools
How to Build a Web Scraper With Python

1. What Are We Going to Scrape?
For this project, we’ll scrape data from IMDb’s “Top 1,000” movies, specifically the top 50 movies on this page.

    The title
    The year it was released
    How long the movie is
    IMDb’s rating of the movie
    The Metascore of the movie
    How many votes the movie got
    The U.S. gross earnings of the movie
    
2. The URL
https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv

3. Tools that are used
Requests will allow us to send HTTP requests to get HTML files
BeautifulSoup will help us parse the HTML files
pandas will help us assemble the data into a DataFrame to clean and analyze it
NumPy will add support for mathematical functions and tools for working with arrays

4. Steps
Inspected our HTML for the data we need
Wrote code to extract data
Put our code in a loop to grab all the data from each movie
Built a DataFrame with Pandas
Cleaned our Data in pandas
Handled type conversion to make our data consistent
Saved our scraped data to CSV.
