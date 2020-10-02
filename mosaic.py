import numpy as np
import matplotlib.pyplot as plt

im = plt.imread("me1.jpg")
# im = im[:800,175:775,:]

shape = im.shape

down_shape = np.array([shape[0]/10,shape[1]/10,3]).astype(np.uint8)
print(down_shape,int(int(down_shape[0])*down_shape[1]))
downim = np.zeros(down_shape)


pix_size_x, pix_size_y = int(shape[0]/down_shape[0]), int(shape[1]/down_shape[1])
for i in range(down_shape[0]):
    for j in range(down_shape[1]):
        tmp = im[i*pix_size_x:(i+1)*pix_size_x,j*pix_size_y:(j+1)*pix_size_y,:]


        flattenend = tmp.reshape(tmp.shape[0]*tmp.shape[1],tmp.shape[2])
        avg = flattenend.mean(axis=0)
        downim[i,j,:] = avg

downim = downim.astype(np.uint8)

fig = plt.figure()
plt.imshow(im)
plt.draw()
plt.waitforbuttonpress(0)
plt.close(fig)

fig = plt.figure()
plt.imshow(downim)
plt.draw()
plt.waitforbuttonpress(0)
plt.close(fig)
