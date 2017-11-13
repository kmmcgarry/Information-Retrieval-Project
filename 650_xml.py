import xml.etree.ElementTree as ET

class xmlfile:
	def __init__(self,file):
		tree = ET.parse(file)
		root = tree.getroot()
		for eligi in root.findall('eligibility'):
			self.textblock = eligi.find('criteria').find('textblock').text
			self.gender = eligi.find('gender').text
			self.minimum_age = eligi.find('minimum_age').text
			self.maximum_age = eligi.find('maximum_age').text
			self.healthy_volunteers = eligi.find('healthy_volunteers').text

if __name__ == "__main__":
	xml = xmlfile('../NCT00000102.xml')
	print(xml.textblock)
	print(xml.gender)
	print(xml.minimum_age)











