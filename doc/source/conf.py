# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_sphinx" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

# Load all of the global Astropy configuration
from astropy.sphinx.conf import *

# Load Runnotebook extension
import os, sys
sys.path.insert(0, os.path.abspath('extensions'))
extensions += ['notebook_sphinxext']

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = u'SunPy'
author = u'The SunPy Community'
copyright = u'2013, ' + author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import sunpy
# The short X.Y version.
version = sunpy.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = sunpy.__version__

intersphinx_mapping['astropy'] = ('http://docs.astropy.org/en/stable/', None)
# -- Options for HTML output ---------------------------------------------------

# A NOTE ON HTML THEMES
# The global astropy configuration uses a custom theme, 'bootstrap-astropy',
# which is installed along with astropy. A different theme can be used or
# the options for this theme can be modified by overriding some of the
# variables set in the global configuration. The variables set in the
# global configuration are listed below, commented out.

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
#html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
html_theme = 'default'

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = ''
html_logo = '../logo/sunpy_logo_compact_192x239.png'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0} v{1}'.format(project, release)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


## -- Options for the edit_on_github extension ----------------------------------------
#
extensions += ['astropy.sphinx.ext.edit_on_github']
#
## Don't import the module as "version" or it will override the
## "version" configuration parameter
# TODO: make this smart like astropy
edit_on_github_project = "sunpy/sunpy"
edit_on_github_branch = "master"

edit_on_github_source_root = ""
edit_on_github_doc_root = "docs"


#import sys, os, math
#
#class Mock(object):
#    __all__ = []
#    def __init__(self, *args, **kwargs):
#        for key, value in kwargs.iteritems():
#            setattr(self, key, value)
#
#    def __call__(self, *args, **kwargs):
#        return Mock()
#
#    def __iter__(self):
#        return iter([Mock()])
#
#    __add__  = __mul__  = __getitem__ = __setitem__ = \
#__delitem__ = __sub__ =  __floordiv__ = __mod__ = __divmod__ = \
#__pow__ = __lshift__ = __rshift__ = __and__ = __xor__ = __or__ = \
#__rmul__  = __rsub__  = __rfloordiv__ = __rmod__ = __rdivmod__ = \
#__rpow__ = __rlshift__ = __rrshift__ = __rand__ = __rxor__ = __ror__ = \
#__imul__  = __isub__  = __ifloordiv__ = __imod__ = __idivmod__ = \
#__ipow__ = __ilshift__ = __irshift__ = __iand__ = __ixor__ = __ior__ = \
#__div__ = __rdiv__ = __idiv__ = __truediv__ = __rtruediv__ = __itruediv__ = \
#__neg__ = __pos__ = __abs__ = __invert__ = __call__
#
#    def __getattr__(self, name):
#        if name in ('__file__', '__path__'):
#            return '/dev/null'
#        # This clause is commented out because it makes an assumption with
#        # case convention that is not necessarily true
#        #elif name[0] != '_' and name[0] == name[0].upper():
#        #    return type(name, (), {})
#        else:
#            return Mock(**vars(self))
#
#    def __lt__(self, *args, **kwargs):
#        return True
#
#    __nonzero__ = __le__ = __eq__ = __ne__ = __gt__ = __ge__ = __contains__ = \
#__lt__
#
#
#    def __repr__(self):
#        # Use _mock_repr to fake the __repr__ call
#        res = getattr(self, "_mock_repr")
#        return res if isinstance(res, str) else "Mock"
#
#    def __hash__(self):
#        return 1
#
#    __len__ = __int__ = __long__ = __index__ = __hash__
#
#    def __oct__(self):
#        return '01'
#
#    def __hex__(self):
#        return '0x1'
#
#    def __float__(self):
#        return 0.1
#
#    def __complex__(self):
#        return 1j
#
#
#MOCK_MODULES = [
#    'scipy', 'matplotlib', 'matplotlib.pyplot', 'pyfits',
#    'scipy.constants.constants', 'matplotlib.cm',
#    'matplotlib.image', 'matplotlib.colors',
#    'pandas', 'pandas.io', 'pandas.io.parsers',
#    'suds', 'matplotlib.ticker', 'matplotlib.colorbar',
#    'matplotlib.dates', 'scipy.optimize', 'scipy.ndimage',
#    'matplotlib.figure', 'scipy.ndimage.interpolation', 'bs4',
#    'scipy.interpolate',
#    'matplotlib.cbook','matplotlib.axes','matplotlib.transforms',
#    'matplotlib.gridspec','matplotlib.artist','matplotlib.axis',
#    'matplotlib.collections','matplotlib.contour','matplotlib.path',
#    'matplotlib.patches','matplotlib.animation','matplotlib.widgets',
#    'mpl_toolkits','mpl_toolkits.axes_grid1',
#    'mpl_toolkits.axes_grid1.axes_size',
#
#    # The following lines are for sunpy.gui, which is a mess
#    #'PyQt4','PyQt4.QtCore','PyQt4.QtGui',
#    #'matplotlib.backends.backend_qt4agg',
#    'sunpy.gui.ui.mainwindow.widgets.figure_canvas',
#    'sunpy.gui.ui.mainwindow.widgets.toolbars',
#    'sunpy.gui.ui.mainwindow.resources',
#
#    'scipy.constants',
#
#    'astropy', 'astropy.units', 'astropy.io', 'astropy.constants']
#
#if not tags.has('doctest'):
#    for mod_name in MOCK_MODULES:
#        sys.modules[mod_name] = Mock(pi=math.pi, G=6.67364e-11)
#
#    # We want np.dtype() to return a special Mock class because it shows up as a
#    # default value for arguments (see sunpy.spectra.spectrogram)
#    sys.modules['numpy'] = Mock(pi=math.pi, G=6.67364e-11,
#                                ndarray=type('ndarray', (), {}),
#                                dtype=lambda _: Mock(_mock_repr='np.dtype(\'float32\')'))
#else:
#    import matplotlib
#    matplotlib.interactive(True)
#    exclude_patterns = ["reference/*"]
