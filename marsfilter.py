import matplotlib.image as mpimg
import numpy as np
from skimage import transform, data, io

def marsfilter(imfile):
	img = mpimg.imread(imfile)
	mask = N.ones_like(img)
	mask[:,:,1]*= 0.465
	mask[:,:,2]*= 0.25
	marsimg = img*mask 
	imsavefile = 'mars_'+imfile
	return mpimg.imsave(imsavefile, marsimg, dpi=100)
	
def fisheye(xy):
    center = np.mean(xy, axis=0)
    xc, yc = (xy - center).T

    # Polar coordinates
    r = np.sqrt(xc**2 + yc**2)
    theta = np.arctan2(yc, xc)
    #r[r > 0.5*N.max(r)] = 0.8 * np.exp(r[r > 0.5*N.max(r)]**(1/2.1) / 1.8)
    r = 0.8 * np.exp(r**(1/2.1) / 1.8)
    print r
    P.hist(r)
    return np.column_stack((
       r * np.cos(theta), r * np.sin(theta)
        )) + center
        
#out = transform.warp(image, fisheye)
