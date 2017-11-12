import xml.etree.ElementTree as ET

tree = ET.parse('NCT00000102.xml')
root = tree.getroot()
# [child.attr for child in root if 'eligibility' == child.tag]

# c = 0 
# for child in root:
# 	if 'eligibility' == child.tag:
# 		for k in child.tag:
# 			print k
# 	c+=1
for eligi in root.findall('eligibility'):
	textblock = eligi.find('criteria').find('textblock').text
	gender = eligi.find('gender').text
	minimum_age = eligi.find('minimum_age').text
	maximum_age = eligi.find('maximum_age').text
	healthy_volunteers = eligi.find('healthy_volunteers').text
	print textblock


# print(root[0][0].text)