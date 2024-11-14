import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("data")

# Add sub-elements
item1 = ET.SubElement(root, "item", attrib={"name": "item1"})
item1.text = "This is item 1"

item2 = ET.SubElement(root, "item", attrib={"name": "item2"})
item2.text = "This is item 2"

# Write to an XML file
tree = ET.ElementTree(root)
tree.write("output.xml")

# ------------------------------------------ Modify an XML element
for item in root.findall("item"):
    if item.get("name") == "item1":
        item.text = "Updated item 1 text"
tree.write("modified.xml")

# ------------------------------------------ Reading XML
# import xml.etree.ElementTree as ET

# # Parse an XML file
# tree = ET.parse("output.xml")
# root = tree.getroot()

# # Access elements
# print(root.tag)  # root element tag
# for child in root:
#     print(child.tag, child.attrib)  # child elements and attributes

# ---------------------------------------- Using minidom
from xml.dom import minidom

# # Parse XML file
# doc = minidom.parse("output.xml")

# # Access elements
# items = doc.getElementsByTagName("item")
# for item in items:
#     print(item.getAttribute("name"), item.firstChild.data)

# Pretty print XML from `ElementTree`
xml_str = ET.tostring(root, encoding="utf-8")
parsed_str = minidom.parseString(xml_str)
pretty_xml_str = parsed_str.toprettyxml(indent="  ")

with open("pretty_output.xml", "w") as f:
    f.write(pretty_xml_str)
