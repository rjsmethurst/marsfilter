## marsfilter

#Like #nofilter but for selfie's to look like they're taken on Mars!

Possible spectrum to RGB colour conversion...

Original FORTRAN code @ (http://www.physics.sfasu.edu/astro/color/spectra.html)

Will return smooth(continuous) spectrum, heavy on the red side.

w - wavelength, R, G and B - color components

Ignoring gamma and intensity simple leaves:

`if w >= 380 and w < 440:
    R = -(w - 440.) / (440. - 380.)
    G = 0.0
    B = 1.0
elif w >= 440 and w < 490:
    R = 0.0
    G = (w - 440.) / (490. - 440.)
    B = 1.0
elif w >= 490 and w < 510:
    R = 0.0
    G = 1.0
    B = -(w - 510.) / (510. - 490.)
elif w >= 510 and w < 580:
    R = (w - 510.) / (580. - 510.)
    G = 1.0
    B = 0.0
elif w >= 580 and w < 645:
    R = 1.0
    G = -(w - 645.) / (645. - 580.)
    B = 0.0
elif w >= 645 and w <= 780:
    R = 1.0
    G = 0.0
    B = 0.0
else:
    R = 0.0
    G = 0.0
    B = 0.0`
