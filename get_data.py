import time
import pandas as pd
from selenium import webdriver


# Scrape magicbricks.com for data:

driver = webdriver.Chrome()
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Nagpur")
property_list = []
flag = True
time.sleep(20)
div = driver.find_element_by_xpath('.//div[@class="l-srp__results flex__item"]')
a = div.find_elements_by_xpath('.//a')

for element in a:
	try:
		if element.get_attribute("text")[26:].replace("\n", "") != '':
			location = element.get_attribute("text")[26:].replace("\n", "")
			price =  element.find_element_by_xpath('../..//parent::div[@class="flex relative clearfix m-srp-card__container"]').find_element_by_xpath('.//div[@class="m-srp-card__price"]').text
			area = element.find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('.//div[@class="m-srp-card__summary__info"]').text
			print(price + " " + area + " " + location)
			property_list.append({"localilty": location, "area": area, "price": price})
	
		driver.find_element_by_xpath('.//a[@class="toc"]').click()
			
	except:
		break	
driver.close()



# Put into DataFrame for cleaning:

df = pd.DataFrame(property_list)
df.to_csv("properties.csv")

