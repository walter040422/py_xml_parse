
# coding: utf-8

# In[9]:


import os

from xml.dom import minidom
from PIL import Image
from PIL import ImageDraw
#import matplotlib.pyplot as plt


ImgPath = '/home/walter040422/Downloads/my-projects/xml_parse/JPEG/'
AnnoPath = '/home/walter040422/Downloads/my-projects/xml_parse/Annotations/'

imagelist=os.listdir(ImgPath)

for images in imagelist:
    #print images
    image_pre, ext=os.path.splitext(images)      #分离文件名与扩展名
    #print image_pre
    #print ext
    imgfile=ImgPath+images
    img=Image.open(imgfile)
    img.show()
#    plt.figure(image_pre)
#    plt.imshow(img)
#    plt.show()

#from PIL import Image
#import matplotlib.pyplot as plt
#img=Image.open('d:/dog.png')
#plt.figure("dog")
#plt.imshow(img)
#plt.show()

    drawObject=ImageDraw.Draw(img)   
    #创建一个可用来对image进行操作的对象。对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建。
    
    
#    blank = Image.new("RGB",[1024,768],"white")
#    blank.show()
#    drawObject=ImageDraw.Draw(blank) 
#    drawObject.line([100,100,100,300],fill=128)
    

#    im = Image.open("lena.pgm")
#    draw = ImageDraw.Draw(im)
#    draw.line((0, 0) + im.size, fill=128)
#    draw.line((0, im.size[1], im.size[0], 0), fill=128)
#    del draw
    
    xmlfile=AnnoPath + image_pre + '.xml'
    #print imgfile
    #print xmlfile
    

    Domtree = minidom.parse(xmlfile)

    root = Domtree.documentElement

    filenamelist=root.getElementsByTagName('filename')
    filename=filenamelist[0].childNodes[0].data

    print filename

    objectlist = root.getElementsByTagName('object')

    #print objectlist
    for objects in objectlist:
    #print objects
        namelist = objects.getElementsByTagName('name')
        objectname=namelist[0].childNodes[0].data
        print objectname
    
    
    
        bndboxlist=objects.getElementsByTagName('bndbox')
    
    
        for bndboxes in bndboxlist:
#        print bndboxes        
            Xmin=bndboxes.getElementsByTagName('xmin')
            Xminvalue=float(Xmin[0].childNodes[0].data)
#            print Xminvalue
        
            Ymin=bndboxes.getElementsByTagName('ymin')
            Yminvalue=float(Ymin[0].childNodes[0].data)
#            print Yminvalue
        
            Xmax=bndboxes.getElementsByTagName('xmax')
            Xmaxvalue=float(Xmax[0].childNodes[0].data)
#            print Xmaxvalue
        
            Ymax=bndboxes.getElementsByTagName('ymax')
            Ymaxvalue=float(Ymax[0].childNodes[0].data)
#            print Ymaxvalue
            
            drawObject.line([Xminvalue,Yminvalue,Xminvalue,Ymaxvalue],"yellow")
            drawObject.line([Xminvalue,Yminvalue,Xmaxvalue,Yminvalue],"yellow")
            drawObject.line([Xminvalue,Ymaxvalue,Xmaxvalue,Ymaxvalue],"yellow")
            drawObject.line([Xmaxvalue,Yminvalue,Xmaxvalue,Ymaxvalue],"yellow")
            
            
            
#            drawObject.line([(Xminvalue,Yminvalue),Xmaxvalue,Ymaxvalue] ,"red")

    img.show()
#    plt.figure("dog")
#    plt.imshow(img)
#    plt.show()
    



            
#drawObject.line([(100,100),600,100],fill = 128)  
#drawObject.line([(600,100),(600,600)],"black")  
#drawObject.line((100,600,600,600),fill = "yellow") 


#print '--'*25
#print root.nodeName
#print root.nodeValue
#print root.nodeType
#print root.ELEMENT_NODE
#print '--'*25







