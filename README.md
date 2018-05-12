# property-scraping
A Python web scraping project that gets real estate data from Magic Bricks

DESCRIPTION:
This is a web scraping project to gather real estate data of Indian cities from popular property websites. I chose to get data for Nagpur, from magicbricks.com. The scraped data is stored in a CSV file in the current working directory.



REQUIREMENTS:
1.	Python selenium library
2.	The “chromedriver” executable for selenium



HOW TO USE:
1.	In any web browser, open magicbricks.com
2.	Search for properties in the required city.
3.	Copy the URL of the search results page.
4.	Change the "url" parameter in the script "get_data.py".
5.	Run the “get_data.py” script in a python environment to get the property data from     magicbricks.com. This creates a CSV file containing unclean data in the current working directory.
6.	Run the file “clean_data.py” to get two CSV files: one containing cleaned data, the other containing the top five localities where average price per square foot is highest.
7.	To scrape data from any other site, open its HTML source, and make the necessary changes in the argument to the  find_element_by_xpath method, in "get_data.py".

