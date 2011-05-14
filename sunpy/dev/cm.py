"""A module for dealing with static and dynamically-generated colormaps

| Author: `Keith Hughitt <keith.hughitt@nasa.gov>`_
| Written: 2011/04/01
| Last Modified: 2011/04/11
"""
__author__ = "Keith Hughitt"
__email__ = "keith.hughitt@nasa.gov"

import matplotlib.colors
import operator
import numpy

#
# Things to try:
#   use sub-sampling to speed up histogram generation
#
def log_adaptive(data, bits=12, vmin=1, vmax=2000):
    """Creates a custom log-scaled color map scaled to the specified image data.
    
    In order increase contrast in those pixel ranges which occur
    frequently a histogram is created for the log of the data and
    those values which occur most often are given unique colors.
    
    The method needs to be tested on other AIA, etc. data. For the sample
    image the color maps generated tend favor detail in the corona.
    
    So far little tweaking has been done though and there are probably
    things that could improved. Feel free to try!
       
    Parameters
    ----------
    data : numpy.ndarray
        Image data
    bits : int
        Number of bits to use per pixel
    vmin : int
        Minimum data clip value
    vmax : int
        Maximum data clip value
    
    Returns
    -------
    out : matplotlib.colors.LinearSegmentedColormap
        A logarithmic grayscale color map normalized to the image data
        
    Examples
    --------
    >>> map = sunpy.Map('doc/sample-data/AIA20110319_105400_0171.fits')
    >>> cmap = sunpy.dev.cm.log_adaptive(map)
    >>> map.plot(cmap=cmap)    
    """
    
    # Number of entries in the color map
    cmap_size = 2 ** bits
    
    # Ignore negative values and outliers
    data = numpy.log(data.clip(vmin, vmax))
    
    # Sort bins by frequency
    sorted_counts = _get_pixel_counts(data, cmap_size)
    indices = sorted([x[0] for x in sorted_counts[0:cmap_size - 1]])
    
    # Map it back to the actual data range
    indices = [numpy.exp(x) for x in indices]
    
    # Scale from 0 to 1
    maximum = numpy.exp(data.max())
    indices =  [x / maximum for x in indices]
    
    # Create a matplotlib-formatted color dictionary
    cdict = _generate_cdict_for_indices(indices, cmap_size)
    
    return matplotlib.colors.LinearSegmentedColormap('automap', cdict, 
                                                     cmap_size)


def _generate_cdict_for_indices(indices, cmap_size):
    """Converts a list of indice values to an RGB color dictionary needed 
       to generate a linear segmented colormap
       
       See: http://matplotlib.sourceforge.net/api/colors_api.html
    """
    step = 1. / cmap_size
    cdict = {'red': [], 'green': [], 'blue': []}
    
    value = 0
    
    for i in indices:
        cmap_value = (i, value, value)
        cdict['red'].append(cmap_value)
        cdict['green'].append(cmap_value)
        cdict['blue'].append(cmap_value)
        value += step
        
    # cmap values must range from 0 to 1
    cdict['red'][0] = cdict['green'][0] = cdict['blue'][0] = (0, 0, 0)
    cdict['red'][-1] = cdict['green'][-1] = cdict['blue'][-1] = (1, 1, 1)
    
    # convert rgb lists to tuples
    cdict['red'] = tuple(cdict['red'])
    cdict['green'] = tuple(cdict['green'])
    cdict['blue'] = tuple(cdict['blue'])

    return cdict

def _get_pixel_counts(data, cmap_size):
    """Returns a list of the pixel values sorted by frequency
    
           ex = [(0.00092784453851832058, 54033),
                 (7.5999746150035641, 3616),
                 (4.6347998824217607, 1186),
                 (5.6273771261136147, 1178),
                 (6.7257286471965561, 1169),
                 ...,
                 (1.7257286471965561, 1)]

    """
    # Bin the data
    hist, bins = numpy.histogram(data, bins=cmap_size)
    
    counts = {}
    i = 0
    
    # Create a dictionary which maps from mean bin values to counts
    for freq in hist:
        counts[(bins[i] + bins[i + 1]) / 2] = freq
        i += 1
    
    # Return as a list of tuples sorted by frequency
    return sorted(iter(counts.items()), key=operator.itemgetter(1), reverse=True)
