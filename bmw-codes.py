from xml.etree.ElementTree import Element,SubElement,ElementTree,dump
#-*-coding:utf-8 -*-

filename = "bmw-codes"
 
 
root = Element('FDL')
name1 = SubElement(root, 'cafd')
name1.set("series","G012,G011,G030")
name1.set("author","98")
name1.set("name","DKOMBI2")
name1.set("id","00002660")


name2 = SubElement(name1, 'code')
name2.set("description","1.후진시 경고음(G30전용)")

name3 = SubElement(name2, "group")
name3.set("id","3000")

name4 = SubElement(name3, "function")
name4.set("comment","R_GANG_AKUSTIK_ENABLE")
name4.set("mask","0001000b")
name4.set("start","1")
name4.set("end","1")
name4.text = "aktiv"



dump(root)
 
tree = ElementTree(root)
tree.write('./'+filename + '.xml',encoding='utf-8', xml_declaration=True)



# 참고 사이트
#https://vhxpffltm.tistory.com/161
#http://parkjuwan.dothome.co.kr/wordpress/2017/02/14/make-simplexml-py/
#https://ballentain.tistory.com/8
#https://wikidocs.net/21137