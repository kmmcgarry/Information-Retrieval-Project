import xml.etree.ElementTree as ET


def getFields(inputFile,ct_id):
    tree = ET.parse(inputFile)
    root = tree.getroot()
    for child in root:
        print child.tag, child.attrib


getFields("/Users/kristen/Desktop/test_ct.txt","NCT00202020")
