#!/usr/bin/python
import requests as r

from PIL import Image as i
from io import BytesIO

# pip install requests Pillow

baseurl="http://static.hitta.se/tile/v3/g/1/19/{x}/{y}"

xcenter=286193
ycenter=153459

size=5

out = i.new("RGB",(256*size*2,256*size*2))

for xi,x in enumerate(range(xcenter-size,xcenter+size)):
  for yi,y in enumerate(range(ycenter-size,ycenter+size)):
    pim = r.get(baseurl.format(x=x,y=y))
    pim = i.open(BytesIO(pim.content))
    out.paste(pim,(xi*256,yi*256))
  print(f"row {x}")

out.save("out.png")
