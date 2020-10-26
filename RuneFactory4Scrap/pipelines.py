# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import mysql.connector

#CREATE TABLE `playground`.`rf4_equipment` (
#  `Type` VARCHAR(15) NULL,
#  `Name` VARCHAR(50) NULL,
#  `Abilities` VARCHAR(255) NULL,
#  `Buy` INT NULL,
#  `Sell` INT NULL,
#  `Description` VARCHAR(300) NULL);



class Runefactory4ScrapPipeline(object):
	def __init__(self):
		self.create_connection()
		self.create_table()
	
	def create_connection(self):
		self.conn = mysql.connector.connect(
			host = 'localhost',
			user = 'root',
			passwd = '',
			database = 'RuneFactory4Equipments',
		)
		self.curr = self.conn.cursor()
	
	def create_table(self):
		self.curr.execute("""DROP TABLE IF EXISTS rf4_equipment""")
		self.curr.execute(
		"""CREATE TABLE `rf4_equipment` (`Type` VARCHAR(15) NULL,`Name` VARCHAR(50) NULL,`Abilities` VARCHAR(255) NULL,`Buy` VARCHAR(15) NULL,`Sell` VARCHAR(15) NULL,`Description` VARCHAR(300) NULL)"""
		)
	
	def process_item(self, item, spider):
		self.store_item(item)
		return item
	
	def store_item(self, item):
		self.curr.execute("""INSERT INTO rf4_equipment values (%s, %s, %s, %s , %s, %s)""", (
			item["type"],
			item["name"],
			item["abilities"],
			item["buy"],
			item["sell"],
			item["description"]
		))
		self.conn.commit()
