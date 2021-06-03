from xml.etree.ElementTree import Element,SubElement,ElementTree,dump
#-*-coding:utf-8 -*-

import pandas as pd
# 출력할 xml 파일명(확장자 제외)
filename = "bmw-codes"

# 읽을 엑셀파일명(확장자 포함)
#xlsx = pd.read_excel('./bmw-codes.xlsx',sheet_name="Sheet1")
#xlsx = pd.read_excel('./bmw-codes.xlsx')
xlsx = pd.read_excel('./(BMW) G30 코딩좌표.xlsx')

#print(xlsx)

root = Element('FDL')
cafd_id = "NULL"

# 로우단위로 반복하여 데이터 만들기
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

# 만들어진 데이터를 xml 생성
dump(root)

tree = ElementTree(root)
tree.write('./' + filename + '.xml', encoding='utf-8', xml_declaration=True)