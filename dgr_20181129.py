Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/derivative.py'}

Warning (from warnings module):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/font_manager.py", line 281
    'Matplotlib is building the font cache using fc-list. '
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/derivative.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f1976beee18>, 'plt': <module 'matplotlib.pyplot' from '/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py'>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])}
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> y
array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
Traceback (most recent call last):
  File "/home/user/RTR105/derivative.py", line 22, in <module>
    plt.plot(x,y, 'ŗo')
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 356, in _plot_args
    linestyle, marker, color = _process_plot_format(tup[-1])
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 129, in _process_plot_format
    'Unrecognized character %c in format string' % c)
ValueError: Unrecognized character ŗ in format string
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
Traceback (most recent call last):
  File "/home/user/RTR105/derivative.py", line 22, in <module>
    plt.plot(x,y, 'ŗo')
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 356, in _plot_args
    linestyle, marker, color = _process_plot_format(tup[-1])
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 129, in _process_plot_format
    'Unrecognized character %c in format string' % c)
ValueError: Unrecognized character ŗ in format string
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
Traceback (most recent call last):
  File "/home/user/RTR105/derivative.py", line 22, in <module>
    plt.plot(x,y,'ŗo')
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 356, in _plot_args
    linestyle, marker, color = _process_plot_format(tup[-1])
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 129, in _process_plot_format
    'Unrecognized character %c in format string' % c)
ValueError: Unrecognized character ŗ in format string
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================

================== RESTART: /home/user/RTR105/derivative.py ==================

================== RESTART: /home/user/RTR105/derivative.py ==================

================== RESTART: /home/user/RTR105/derivative.py ==================

================== RESTART: /home/user/RTR105/derivative.py ==================
[]
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]
Traceback (most recent call last):
  File "/home/user/RTR105/derivative.py", line 40, in <module>
    legend.appened('funkcija ar starpvertibam')
AttributeError: 'list' object has no attribute 'appened'
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]

================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]

================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]
>>> print(plt.legend._doc_)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(plt.legend._doc_)
AttributeError: 'function' object has no attribute '_doc_'
>>> print(plt.legend.__doc__)
Places a legend on the axes.

To make a legend for lines which already exist on the axes
(via plot for instance), simply call this function with an iterable
of strings, one for each legend item. For example::

    ax.plot([1, 2, 3])
    ax.legend(['A simple line'])

However, in order to keep the "label" and the legend element
instance together, it is preferable to specify the label either at
artist creation, or by calling the
:meth:`~matplotlib.artist.Artist.set_label` method on the artist::

    line, = ax.plot([1, 2, 3], label='Inline label')
    # Overwrite the label by calling the method.
    line.set_label('Label via method')
    ax.legend()

Specific lines can be excluded from the automatic legend element
selection by defining a label starting with an underscore.
This is default for all artists, so calling :meth:`legend` without
any arguments and without setting the labels manually will result in
no legend being drawn.

For full control of which artists have a legend entry, it is possible
to pass an iterable of legend artists followed by an iterable of
legend labels respectively::

   legend((line1, line2, line3), ('label1', 'label2', 'label3'))

Parameters
----------

loc : int or string or pair of floats, default: 'upper right'
    The location of the legend. Possible codes are:

        ===============   =============
        Location String   Location Code
        ===============   =============
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        'right'           5
        'center left'     6
        'center right'    7
        'lower center'    8
        'upper center'    9
        'center'          10
        ===============   =============


    Alternatively can be a 2-tuple giving ``x, y`` of the lower-left
    corner of the legend in axes coordinates (in which case
    ``bbox_to_anchor`` will be ignored).

bbox_to_anchor : `~.BboxBase` or pair of floats
    Specify any arbitrary location for the legend in `bbox_transform`
    coordinates (default Axes coordinates).

    For example, to put the legend's upper right hand corner in the
    center of the axes the following keywords can be used::

       loc='upper right', bbox_to_anchor=(0.5, 0.5)

ncol : integer
    The number of columns that the legend has. Default is 1.

prop : None or :class:`matplotlib.font_manager.FontProperties` or dict
    The font properties of the legend. If None (default), the current
    :data:`matplotlib.rcParams` will be used.

fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
    Controls the font size of the legend. If the value is numeric the
    size will be the absolute font size in points. String values are
    relative to the current default font size. This argument is only
    used if `prop` is not specified.

numpoints : None or int
    The number of marker points in the legend when creating a legend
    entry for a line/:class:`matplotlib.lines.Line2D`.
    Default is ``None`` which will take the value from the
    ``legend.numpoints`` :data:`rcParam<matplotlib.rcParams>`.

scatterpoints : None or int
    The number of marker points in the legend when creating a legend
    entry for a scatter plot/
    :class:`matplotlib.collections.PathCollection`.
    Default is ``None`` which will take the value from the
    ``legend.scatterpoints`` :data:`rcParam<matplotlib.rcParams>`.

scatteryoffsets : iterable of floats
    The vertical offset (relative to the font size) for the markers
    created for a scatter plot legend entry. 0.0 is at the base the
    legend text, and 1.0 is at the top. To draw all markers at the
    same height, set to ``[0.5]``. Default ``[0.375, 0.5, 0.3125]``.

markerscale : None or int or float
    The relative size of legend markers compared with the originally
    drawn ones. Default is ``None`` which will take the value from
    the ``legend.markerscale`` :data:`rcParam <matplotlib.rcParams>`.

markerfirst : bool
    If *True*, legend marker is placed to the left of the legend label.
    If *False*, legend marker is placed to the right of the legend
    label.
    Default is *True*.

frameon : None or bool
    Control whether the legend should be drawn on a patch (frame).
    Default is ``None`` which will take the value from the
    ``legend.frameon`` :data:`rcParam<matplotlib.rcParams>`.

fancybox : None or bool
    Control whether round edges should be enabled around
    the :class:`~matplotlib.patches.FancyBboxPatch` which
    makes up the legend's background.
    Default is ``None`` which will take the value from the
    ``legend.fancybox`` :data:`rcParam<matplotlib.rcParams>`.

shadow : None or bool
    Control whether to draw a shadow behind the legend.
    Default is ``None`` which will take the value from the
    ``legend.shadow`` :data:`rcParam<matplotlib.rcParams>`.

framealpha : None or float
    Control the alpha transparency of the legend's background.
    Default is ``None`` which will take the value from the
    ``legend.framealpha`` :data:`rcParam<matplotlib.rcParams>`.
    If shadow is activated and framealpha is ``None`` the
    default value is being ignored.

facecolor : None or "inherit" or a color spec
    Control the legend's background color.
    Default is ``None`` which will take the value from the
    ``legend.facecolor`` :data:`rcParam<matplotlib.rcParams>`.
    If ``"inherit"``, it will take the ``axes.facecolor``
    :data:`rcParam<matplotlib.rcParams>`.

edgecolor : None or "inherit" or a color spec
    Control the legend's background patch edge color.
    Default is ``None`` which will take the value from the
    ``legend.edgecolor`` :data:`rcParam<matplotlib.rcParams>`.
    If ``"inherit"``, it will take the ``axes.edgecolor``
    :data:`rcParam<matplotlib.rcParams>`.

mode : {"expand", None}
    If `mode` is set to ``"expand"`` the legend will be horizontally
    expanded to fill the axes area (or `bbox_to_anchor` if defines
    the legend's size).

bbox_transform : None or :class:`matplotlib.transforms.Transform`
    The transform for the bounding box (`bbox_to_anchor`). For a value
    of ``None`` (default) the Axes'
    :data:`~matplotlib.axes.Axes.transAxes` transform will be used.

title : str or None
    The legend's title. Default is no title (``None``).

borderpad : float or None
    The fractional whitespace inside the legend border.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.borderpad`` :data:`rcParam<matplotlib.rcParams>`.

labelspacing : float or None
    The vertical space between the legend entries.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.labelspacing`` :data:`rcParam<matplotlib.rcParams>`.

handlelength : float or None
    The length of the legend handles.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.handlelength`` :data:`rcParam<matplotlib.rcParams>`.

handletextpad : float or None
    The pad between the legend handle and text.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.handletextpad`` :data:`rcParam<matplotlib.rcParams>`.

borderaxespad : float or None
    The pad between the axes and legend border.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.borderaxespad`` :data:`rcParam<matplotlib.rcParams>`.

columnspacing : float or None
    The spacing between columns.
    Measured in font-size units.
    Default is ``None`` which will take the value from the
    ``legend.columnspacing`` :data:`rcParam<matplotlib.rcParams>`.

handler_map : dict or None
    The custom dictionary mapping instances or types to a legend
    handler. This `handler_map` updates the default handler map
    found at :func:`matplotlib.legend.Legend.get_legend_handler_map`.

Returns
-------

:class:`matplotlib.legend.Legend` instance

Notes
-----

Not all kinds of artist are supported by the legend command. See
:ref:`sphx_glr_tutorials_intermediate_legend_guide.py` for details.

Examples
--------

.. plot:: gallery/api/legend.py
>>> 
================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]

================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]

Warning (from warnings module):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/legend.py", line 638
    % (loc, '\n\t'.join(self.codes)))
UserWarning: Unrecognized location "3". Falling back on "best"; valid locations are
	best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center


================== RESTART: /home/user/RTR105/derivative.py ==================
[]
[0.9735458557716262]
[0.9735458557716262, 0.8198443714771806]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893]
[0.9735458557716262, 0.8198443714771806, 0.536707487669259, 0.16883629268569678, -0.2256904405395585, -0.5845856156863268, -0.8511875759881149, -0.9834057339587118, -0.9603657496681809, -0.7857051300326893, -0.4869989464539695]
>>> 
