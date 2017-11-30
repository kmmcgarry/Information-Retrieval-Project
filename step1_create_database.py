import os
import xml.etree.ElementTree as ET
# import nltk 
import sqlite3 as sqlite
import datetime

class xmlfile:
	def __init__(self,file):
		tree = ET.parse(file)
		root = tree.getroot()
		self.id = root.find('id_info').find('nct_id').text
		self.check = root.findall('eligibility')
		for eligi in root.findall('eligibility'):
			#self.textblock = eligi.find('criteria').find('textblock').text
			try:
				self.gender = eligi.find('gender').text
			except:
				self.gender = ''
			try:
				self.minimum_age = eligi.find('minimum_age').text
			except:
				self.minimum_age = ''
			try:
				self.maximum_age = eligi.find('maximum_age').text
			except:
				self.maximum_age = ''
			try:
				self.healthy_volunteers = eligi.find('healthy_volunteers').text
			except:
				self.healthy_volunteers = ''

class directories:
	def __init__(self):
		self.current = os.getcwd()
		self.currentlist = os.listdir(os.getcwd())
		self.parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
		self.parentlist = os.listdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


if __name__ == "__main__":
	# xml = xmlfile('../NCT00000102.xml')
	mydir = directories()

	#changing working directory
	# os.chdir()
	with sqlite.connect('../test.db') as con:
	# 2. Create the movie_genre table and load data into it
		cur = con.cursor()    
		cur.execute("DROP TABLE IF EXISTS clinical_trials")
		cur.execute("CREATE TABLE clinical_trials(nct_id text PRIMARY KEY,gender text, minimum_age text, maximum_age text, healthy_volunteers text, file_path text)")
		for i in os.listdir(mydir.parent+'/clinicaltrials_xml_flat'):
				if i != '.DS_Store':
					print(i)
					print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
					for j in os.listdir(mydir.parent+'/clinicaltrials_xml_flat/'+i):
						if j != '.DS_Store':
							xml = xmlfile(mydir.parent+'/clinicaltrials_xml_flat/'+i+'/'+j)
							if xml.check:
								cur.execute("INSERT INTO clinical_trials VALUES(?,?,?,?,?,?)", (xml.id, xml.gender,xml.minimum_age,xml.maximum_age,xml.healthy_volunteers,i))
		con.commit()

	# with sqlite.connect('../test.db') as con:
	# 	cur = con.cursor()
	# 	cur.execute('select * from clinical_trials limit 10')
	# 	print (cur.fetchall())








