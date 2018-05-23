======
PyRect
======
PyRect is a simple module with a Rect class for Pygame-like rectangular areas.

This module is like a stand-alone version of Pygame's Rect class. It is similar to the Rect module by Simon Wittber, but compatible with both Python 2 and 3.

Currently under development, though the basic features work.

Examples
========

    >>> import pyrect
    >>> rectangle = pyrect.Rect(0, 0, 20, 10)
    >>> rectangle.topleft
    (0, 0)
    >>> rectangle.bottomright
    (20, 10)
    >>> rectangle.width
    20
    >>> rectangle.height
    10
    >>> rectangle.width = 100 # updating one attribute automatically updates all the others
    >>> rectangle.bottomright
    (100, 10)
    >>> rectangle.left = 50
    >>> rectangle.topleft
    (50, 0)
    >>> rectangle.bottomright
    (150, 10)
    >>> rectangle.box # the box tuple shows (left, top, width, height)
    (50, 0, 100, 10)

    >>> floatRectangle = pyrect.Rect(0, 0.2, 20.4, 10.6, enableFloat=True) # allow float values
    >>> floatRectangle.box
    (0.0, 0.2, 20.4, 10.6)

    >>> intRectangle = pyrect.Rect(0, 0.2, 20.4, 10.6) # integers-only by default
    >>> intRectangle.box
    (0, 0, 20, 10)
