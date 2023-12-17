from lxml import etree

def findfile(file):
    try:
        doc = etree.parse(file)
        root = doc.getroot()
        for element in root.iter():
            print(root.tag)
    except Exception as e:
        print(f"Error reading the XML file: {e}")

xml_path = "/mnt/g/My Drive/backup/sms-20231217000653.xml"
findfile(xml_path)

