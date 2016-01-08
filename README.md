## marsfilter

#Like #nofilter but for selfies to look like they're taken on Mars!

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

To get the color scaling, we are taking the disk average reflectance spectra of Earth and Mars and comparing the relative scaling between values at R (650 nm), G (532 nm), and B (473 nm). The reflectance spectrum of Mars and Earth are from:

Giovanna Tinetti, Victoria S. Meadows, David Crisp, William Fong, Thangasamy Velusamy, and Heather Snively. Astrobiology. August 2005, 5(4): 461-482. doi:10.1089/ast.2005.5.461.

Giovanna Tinetti, Victoria S. Meadows, David Crisp, William Fong, Evan Fishbein, Margaret Turnbull, and Jean-Pierre Bibring. Astrobiology. March 2006, 6(1): 34-47. doi:10.1089/ast.2006.6.34.
