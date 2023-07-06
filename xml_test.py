from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x23ecb8804b0>]
print(cNodes[0])  # <DOM Element: znajomi at 0x1d0999504b0>
print(cNodes[0].getElementsByTagName('osoba'))
# [<DOM Element: osoba at 0x15242e602d0>, <DOM Element: osoba at 0x15242e97c50>]
print(cNodes[0].getElementsByTagName('osoba')[0])  # <DOM Element: osoba at 0x1f1791c02d0>
print(cNodes[0].getElementsByTagName('osoba')[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(cNodes[0].getElementsByTagName('osoba')[1].toxml())
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie'))  # [<DOM Element: imie at 0x17376c97cf0>]
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].toxml())
# <imie foo="aaaa">Janina</imie>
name = cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].firstChild.data
print(name)  # Janina
