import re
a = """sdhellolsdlfsdfiooe:
yy988989pythonafsf"""

b = re.findall('hello(.*?)python',a)
c = re.findall('hello(.*?)python',a,re.S)
print (b)
print(c)
