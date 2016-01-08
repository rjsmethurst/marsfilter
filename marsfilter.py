import matplotlib.image as mpimg
import numpy as np

def marsfilter(imfile):
	img = mpimg.imread(imfile)
	mask = N.ones_like(img)
	mask[:,:,1]*= 0.465
	mask[:,:,2]*= 0.25
	marsimg = img*mask 
	imsavefile = 'mars_'+imfile
	return mpimg.imsave(imsavefile, marsimg, dpi=100)
