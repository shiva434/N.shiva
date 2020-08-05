#finding radius of the circle
import math
a=float(input("input the  radius of circle:"))
print("the area of the circle with radius",a,"is:",math.pi*a*a)
#finding name of the extension
a=input("input the filename:")
b=a.split('.')
dic={"aif":"AIF audio file","cda":"CD audio track file","mid":"MIDI audio file","7z":"7-zip compressed file","zip":"zip compressed file","c":"c programming","py":"python"}
print("extension file name:",dic[b[-1]])
