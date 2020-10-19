import scrapy
from ..items import Runefactory4ScrapItem

class runeSpider(scrapy.Spider):
	name = 'rune'
	start_urls = [
		'https://therunefactory.fandom.com/wiki/Equipment_(RF4)'
	]
	
	def parse(self, response):
		items = Runefactory4ScrapItem()
		
		types = response.css("h3 span::text").extract()
		tables = response.css("table.wikitable")
		
		for index, table in enumerate(tables):
			rows = table.css("tr")[1:]		
			for row in rows:
				if (index == 6):
					continue
				else:
					#could have gone through each td one by one
					column = row.css("td ::text").extract() # get the content in each of those column			
					output = []
				
					#Getting name, abilities, buy price, sell price, and description of each row
					for cell in column:
						if ( (cell != "\n") and (cell != " ") and ("\t" not in cell) ):
							output.append(cell.strip("\n"))
				
					#need to check if the last element end with px
					#cause by the fact that some images arent loading
					if (output[-1].endswith("px")):
						output = output[:-1]
					
					#the equipment Basket is a speical case
					if (output[0] == "Basket"):
						output[1:4] = [" ".join(output[1:4])]
					
					#empty buy cell
					if (len(output) < 5):
						output.insert(2,"0")
					
					output.insert(0,types[index])
					
					
					items["type"] = output[0]
					items["name"] = output[1]
					items["abilities"] = output[2]
					items["buy"] = output[3]
					items["sell"] = output[4]
					items["description"] = output[5]
	
					yield items
				

			
		