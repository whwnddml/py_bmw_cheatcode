from xml.etree.ElementTree import Element,SubElement,ElementTree,dump
#-*-coding:utf-8 -*-

import pandas as pd

filename = "bmw-codeskk"

#xlsx = pd.read_excel('./bmw-codes.xlsx',sheet_name="Sheet1")
#xlsx = pd.read_excel('./bmw-codes.xlsx')
xlsx = pd.read_excel('./(BMW) G30 코딩좌표.xlsx')

#print(xlsx)

root = Element('FDL')
cafd_id = "NULL"


for index, row in xlsx.iterrows():
    if row['cafd_id'] != cafd_id:
        name1 = SubElement(root, 'cafd')
        name1.set("id", row['cafd_id'])
        name1.set("name", row['module'])
        # if str(row['series']) != "nan":
        #     name1.set("series", str(row['series']))
        name1.set("author", row['author'])

    name2 = SubElement(name1, 'code')
    name2.set("description", row['description'])
    name3 = SubElement(name2, "group")
    name3.set("id", str(row['group_id']))
    name4 = SubElement(name3, "function")
    name4.set("comment", row['comment'])
    name4.set("mask", str(row['mask']))
    name4.set("start", str(row['start']))
    name4.set("end", str(row['end']))
    name4.text = str(row['function'])

    cafd_id = row['cafd_id']



#
# for index, row in xlsx.iterrows():
#     if cafd_id != "NULL" and row['cafd_id'] == cafd_id:
#         name2 = SubElement(name1, 'code')
#         name2.set("description", row['description'])
#         name3 = SubElement(name2, "group")
#         name3.set("id", str(row['group_id']))
#         name4 = SubElement(name3, "function")
#         name4.set("comment", row['comment'])
#         name4.set("mask", str(row['mask']))
#         name4.set("start", str(row['start']))
#         name4.set("end", str(row['end']))
#         name4.text = str(row['function'])
#         continue
#     name1 = SubElement(root, 'cafd')
#     name1.set("id", row['cafd_id'])
#     name1.set("name", row['module'])
#     #name1.set("series", row['series'])
#     name1.set("author", row['author'])
#
#     name2 = SubElement(name1, 'code')
#     name2.set("description", row['description'])
#     name3 = SubElement(name2, "group")
#     name3.set("id", str(row['group_id']))
#     name4 = SubElement(name3, "function")
#     name4.set("comment", row['comment'])
#     name4.set("mask", str(row['mask']))
#     name4.set("start", str(row['start']))
#     name4.set("end", str(row['end']))
#     name4.text = str(row['function'])
#
#     cafd_id = row['cafd_id']
#

dump(root)

tree = ElementTree(root)
tree.write('./' + filename + '.xml', encoding='utf-8', xml_declaration=True)