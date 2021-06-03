from xml.etree.ElementTree import Element,SubElement,ElementTree,dump
#-*-coding:utf-8 -*-

filename = "sample2"
 
 
root = Element('read')
SubElement(root,'number').text = "번호"
name1 = SubElement(root, 'A')
name1.text = "가장 큰것"
SubElement(name1,'A_t1').text = "1"
SubElement(name1,'A_t2').text = "2"
SubElement(name1,'A_t3').text = "3"
SubElement(name1,'A_t4').text = "4"
SubElement(name1,'A_t5').text = "5"
SubElement(name1,'A_t5').set("prop", "123")
name2 = SubElement(root,'B')
name2.text = "다음으로 큰것"
name3 = SubElement(name2,'B_t1')
name3.text = '11'
 
name4 = SubElement(name3,'C').text = "2222"
 

dump(root)
 
tree = ElementTree(root)
tree.write('./'+filename + '.xml',encoding='utf-8', xml_declaration=True)



# 참고 사이트
#https://vhxpffltm.tistory.com/161
#http://parkjuwan.dothome.co.kr/wordpress/2017/02/14/make-simplexml-py/
#https://ballentain.tistory.com/8
#https://wikidocs.net/21137