import os
from PIL import Image

path = os.getcwd()
path = path+'/Optic Nerve Head Image Sequence'
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        print (os.path.join(root,name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".png"):
                print ("A jpeg file already exists for %s" % name)
                # If a jpeg is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
                try:
                    im = Image.open(os.path.join(root, name))
                    print ("Generating jpeg for %s" % name)
                    im.thumbnail(im.size)
                    im.save(outfile, "PNG", quality=100)
                except Exception, e:
                    print e