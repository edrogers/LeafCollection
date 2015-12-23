#!/usr/bin/python

import httplib, urllib
from PIL import Image
import xmpp
import os
import re
import math
import config

#Open the target directory and find all PDFs of the map10 area
pattern=re.compile("map10.pdf$")
dirName=os.path.dirname(os.path.realpath(__file__))
targetDir="{}/Leaf".format(dirName)
directoryContents=os.listdir(targetDir)
map10pdfs=[]
for filename in directoryContents:
    if pattern.search(filename) != None:
        map10pdfs.append(filename)
map10pdfs.sort()

#convert the two most recent files to GIF using ImageMagick convert
currFile=map10pdfs[-1]
prevFile=map10pdfs[-2]
currGif=currFile.replace(".pdf",".gif")
prevGif=prevFile.replace(".pdf",".gif")
os.system("convert {}/{} {}/{}".format(targetDir,currFile,targetDir,currGif))
os.system("convert {}/{} {}/{}".format(targetDir,prevFile,targetDir,prevGif))

#convert both GIFs to RGB
prevImg=Image.open("{}/{}".format(targetDir,prevGif))
currImg=Image.open("{}/{}".format(targetDir,currGif))
prev_rgb_im = prevImg.convert('RGB')
curr_rgb_im = currImg.convert('RGB')

#Check legend for pixel definitions for each of the four status
Status = ["Not Done","Done","Current","Next"]
nd_color   = prev_rgb_im.getpixel((27,100))
dn_color   = prev_rgb_im.getpixel((27,120))
cr_color   = prev_rgb_im.getpixel((27,140))
nx_color   = prev_rgb_im.getpixel((27,160))

#Now check the pixel color for Area 10-1 in both GIFs
prev_color = prev_rgb_im.getpixel((486,414))
curr_color = curr_rgb_im.getpixel((486,414))

#Find the smallest RMS distance between 10-1 pixel color and status
# color in RGB space
prev_nd = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nd_color,prev_color)])
prev_dn = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(dn_color,prev_color)])
prev_cr = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(cr_color,prev_color)])
prev_nx = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nx_color,prev_color)])
prevList = [prev_nd, prev_dn, prev_cr, prev_nx]
prevStatus = Status[prevList.index(min(prevList))]
# print prevStatus
curr_nd = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nd_color,curr_color)])
curr_dn = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(dn_color,curr_color)])
curr_cr = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(cr_color,curr_color)])
curr_nx = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nx_color,curr_color)])
currList = [curr_nd, curr_dn, curr_cr, curr_nx]
currStatus = Status[currList.index(min(currList))]
# print currStatus

#Send update of Map10 Status
if prevStatus != currStatus:
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": config.apiKey,
            "user": config.apiUser,
            "message": "10-1 Leaf Update: From \"{}\" to \"{}\"".format(prevStatus,currStatus),
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

#Open the target directory and find all PDFs of the map8 area
pattern=re.compile("map8.pdf$")
map8pdfs=[]
for filename in directoryContents:
    if pattern.search(filename) != None:
        map8pdfs.append(filename)
map8pdfs.sort()

#convert the two most recent files to GIF using ImageMagick convert
currFile=map8pdfs[-1]
prevFile=map8pdfs[-2]
currGif=currFile.replace(".pdf",".gif")
prevGif=prevFile.replace(".pdf",".gif")
os.system("convert {}/{} {}/{}".format(targetDir,currFile,targetDir,currGif))
os.system("convert {}/{} {}/{}".format(targetDir,prevFile,targetDir,prevGif))

#convert both GIFs to RGB
prevImg=Image.open("{}/{}".format(targetDir,prevGif))
currImg=Image.open("{}/{}".format(targetDir,currGif))
prev_rgb_im = prevImg.convert('RGB')
curr_rgb_im = currImg.convert('RGB')

#Check legend for pixel definitions for each of the four status
Status = ["Not Done","Done","Current","Next"]
nd_color   = prev_rgb_im.getpixel((27,100))
dn_color   = prev_rgb_im.getpixel((27,120))
cr_color   = prev_rgb_im.getpixel((27,140))
nx_color   = prev_rgb_im.getpixel((27,160))

#Now check the pixel color for Area 8-99 in both GIFs
prev_color = prev_rgb_im.getpixel((315,365))
curr_color = curr_rgb_im.getpixel((315,365))

#Find the smallest RMS distance between 10-1 pixel color and status
# color in RGB space
prev_nd = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nd_color,prev_color)])
prev_dn = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(dn_color,prev_color)])
prev_cr = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(cr_color,prev_color)])
prev_nx = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nx_color,prev_color)])
prevList = [prev_nd, prev_dn, prev_cr, prev_nx]
prevStatus = Status[prevList.index(min(prevList))]
# print prevStatus
curr_nd = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nd_color,curr_color)])
curr_dn = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(dn_color,curr_color)])
curr_cr = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(cr_color,curr_color)])
curr_nx = sum([math.sqrt((x-y)*(x-y)) for x,y in zip(nx_color,curr_color)])
currList = [curr_nd, curr_dn, curr_cr, curr_nx]
currStatus = Status[currList.index(min(currList))]
# print currStatus

#Send update of Map8 Status
if prevStatus != currStatus:
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": config.apiKey,
            "user": config.apiUser,
            "message": "8-99 Leaf Update: From \"{}\" to \"{}\"".format(prevStatus,currStatus),
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

quit()
