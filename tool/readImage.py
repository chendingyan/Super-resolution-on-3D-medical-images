import pydicom
import numpy
import cv2
from matplotlib import pyplot as plt
dcm = pydicom.read_file('/Users/mikechen/Downloads/CT Image/CT_127_1.dcm')

print(dcm.dir("pat"))
print(dcm.pixel_array)

plt.figure()
plt.imshow(dcm.pixel_array)
plt.axis('off')
plt.savefig('demo111.png')
plt.show()


