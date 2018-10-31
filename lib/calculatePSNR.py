import numpy
import cv2
import math


def cal(target, ref):
    target_data = numpy.array(target, dtype=numpy.float64)
    ref_data = numpy.array(ref, dtype=numpy.float64)

    diff = ref_data - target_data
    print(diff.shape)
    diff = diff.flatten('C')
    rmse = math.sqrt(numpy.mean(diff ** 2.))
    return 20 * math.log10(255 / rmse)


im1 = cv2.imread('../original.png')
im2 = cv2.imread('../SRCNN_output.png')
im3 = cv2.imread('../SRGAN_output.png')


print (cal(im2, im1))


print (cal(im3, im1))
