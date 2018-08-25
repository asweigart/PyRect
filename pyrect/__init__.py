import doctest

# TODO - finish doc tests

__version__ = '0.0.2'


class PyRectException(Exception):
    """
    This class exists for PyRect exceptions. If the PyRect module raises any
    non-PyRectException exceptions, this indicates there's a bug in PyRect.
    """
    pass



def _checkForIntOrFloat(arg):
    """Raises an exception if arg is not an int or float. Always returns None."""
    if not isinstance(arg, (int, float)):
        raise PyRectException('argument must be int or float, not %s' % (arg.__class__.__name__))


def _checkForInt(arg):
    """Raises an exception if arg is not an int. Always returns None."""
    if not isinstance(arg, int):
        raise PyRectException('argument must be int or float, not %s' % (arg.__class__.__name__))


def _checkForTwoIntOrFloatTuple(arg):
    try:
        if not isinstance(arg[0], (int, float)) or \
           not isinstance(arg[1], (int, float)):
            raise PyRectException('argument must be a two-item tuple containing int or float values')
    except:
        raise PyRectException('argument must be a two-item tuple containing int or float values')


def _checkForFourIntOrFloatTuple(arg):
    try:
        if not isinstance(arg[0], (int, float)) or \
           not isinstance(arg[1], (int, float)) or \
           not isinstance(arg[2], (int, float)) or \
           not isinstance(arg[3], (int, float)):
            raise PyRectException('argument must be a four-item tuple containing int or float values')
    except:
        raise PyRectException('argument must be a four-item tuple containing int or float values')


def _collides(rectOrPoint1, rectOrPoint2):
    """Returns True if rectOrPoint1 and rectOrPoint2 collide with each other."""


def _getRectsAndPoints(rectsOrPoints):
    points = []
    rects = []
    for rectOrPoint in rectsOrPoints:
        try:
            _checkForTwoIntOrFloatTuple(rectOrPoint)
            points.append(rectOrPoint)
        except PyRectException:
            try:
                _checkForFourIntOrFloatTuple(rectOrPoint)
            except:
                raise PyRectException('argument is not a point or a rect tuple')
            rects.append(rectOrPoint)
    return (rects, points)

'''
def collideAnyBetween(rectsOrPoints):
    """Returns True if any of the (x, y) or (left, top, width, height) tuples
    in rectsOrPoints collides with any other point or box tuple in rectsOrPoints.

    >>> p1 = (50, 50)
    >>> p2 = (100, 100)
    >>> p3 = (50, 200)
    >>> r1 = (-50, -50, 20, 20)
    >>> r2 = (25, 25, 50, 50)
    >>> collideAnyBetween([p1, p2, p3, r1, r2]) # p1 and r2 collide
    True
    >>> collideAnyBetween([p1, p2, p3, r1])
    False
    """
    # TODO - needs to be complete

    # split up
    rects, points = _getRectsAndPoints(rectsOrPoints)

    # compare points with each other
    if len(points) > 1:
        for point in points:
            if point != points[0]:
                return False

    # TODO finish
'''



'''
def collideAllBetween(rectsOrPoints):
    """Returns True if any of the (x, y) or (left, top, width, height) tuples
    in rectsOrPoints collides with any other point or box tuple in rectsOrPoints.

    >>> p1 = (50, 50)
    >>> p2 = (100, 100)
    >>> p3 = (50, 200)
    >>> r1 = (-50, -50, 20, 20)
    >>> r2 = (25, 25, 50, 50)
    >>> collideAllBetween([p1, p2, p3, r1, r2])
    False
    >>> collideAllBetween([p1, p2, p3, r1])
    False
    >>> collideAllBetween([p1, r2]) # Everything in the list collides with each other.
    True
    """

    # Check for valid arguments
    try:
        for rectOrPoint in rectsOrPoints:
            if len(rectOrPoint) == 2:
                _checkForTwoIntOrFloatTuple(rectOrPoint)
            elif len(rectOrPoint) == 4:
                _checkForFourIntOrFloatTuple(rectOrPoint)
            else:
                raise PyRectException()
    except:
        raise PyRectException('Arguments in rectsOrPoints must be 2- or 4-integer/float tuples.')

    raise NotImplementedError # return a list of all rects or points that collide with any other in the argument
'''

class Rect(object):
    def __init__(self, left, top, width, height, enableFloat=False):
        _checkForIntOrFloat(width)
        _checkForIntOrFloat(height)
        _checkForIntOrFloat(left)
        _checkForIntOrFloat(top)

        self._enableFloat = enableFloat

        if enableFloat:
            self._width  = float(width)
            self._height = float(height)
            self._left   = float(left)
            self._top    = float(top)
        else:
            self._width  = int(width)
            self._height = int(height)
            self._left   = int(left)
            self._top    = int(top)


    # OPERATOR OVERLOADING / DUNDER METHODS
    def __repr__(self):
        """Return a string of the constructor function call to create this Rect object."""
        return '%s(left=%s, top=%s, width=%s, height=%s)' % (self.__class__.__name__, self._left, self._top, self._width, self._height)


    def __str__(self):
        """Return a string representation of this Rect object."""
        return '(x=%s, y=%s, w=%s, h=%s)' % (self._left, self._top, self._width, self._height)

    @property
    def enableFloat(self):
        """
        A Boolean attribute that determines if this rectangle uses floating point
        numbers for its position and size. False, by default.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.enableFloat
        False
        >>> r.enableFloat = True
        >>> r.top = 3.14
        >>> r
        Rect(left=0.0, top=3.14, width=10.0, height=20.0)
        """
        return self._enableFloat

    @enableFloat.setter
    def enableFloat(self, value):
        if not isinstance(value, bool):
            raise PyRectException('enableFloat must be set to a bool value')
        self._enableFloat = value

        if self._enableFloat:
            self._left = float(self._left)
            self._top = float(self._top)
            self._width = float(self._width)
            self._height = float(self._height)
        else:
            self._left = int(self._left)
            self._top = int(self._top)
            self._width = int(self._width)
            self._height = int(self._height)


    @enableFloat.deleter
    def enableFloat(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # LEFT SIDE PROPERTY
    @property
    def left(self):
        """
        The x coordinate for the left edge of the rectangle. `x` is an alias for `left`.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.left
        0
        >>> r.left = 50
        >>> r
        Rect(left=50, top=0, width=10, height=20)
        """
        return self._left

    @left.setter
    def left(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._left = value
        else:
            self._left = int(value)


    @left.deleter
    def left(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    x = left # x is an alias for left


    # TOP SIDE PROPERTY
    @property
    def top(self):
        """
        The y coordinate for the top edge of the rectangle. `y` is an alias for `top`.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.top
        0
        >>> r.top = 50
        >>> r
        Rect(left=0, top=50, width=10, height=20)
        """
        return self._top

    @top.setter
    def top(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._top = value
        else:
            self._top = int(value)

    @top.deleter
    def top(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))

    y = top # y is an alias for top


    # RIGHT SIDE PROPERTY
    @property
    def right(self):
        """
        The x coordinate for the right edge of the rectangle.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.right
        10
        >>> r.right = 50
        >>> r
        Rect(left=40, top=0, width=10, height=20)
        """
        return self._left + self._width

    @right.setter
    def right(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._left = value - self._width
        else:
            self._left = int(value) - self._width

    @right.deleter
    def right(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM SIDE PROPERTY
    @property
    def bottom(self):
        """The y coordinate for the bottom edge of the rectangle.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.bottom
        20
        >>> r.bottom = 30
        >>> r
        Rect(left=0, top=10, width=10, height=20)
        """
        return self._top + self._height

    @bottom.setter
    def bottom(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._top = value - self._height
        else:
            self._top = int(value) - self._height

    @bottom.deleter
    def bottom(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # TOP LEFT CORNER PROPERTY
    @property
    def topleft(self):
        """
        The x and y coordinates for the top right corner of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.topleft
        (0, 0)
        >>> r.topleft = (30, 30)
        >>> r
        Rect(left=30, top=30, width=10, height=20)
        """
        return (self._left, self._top)

    @topleft.setter
    def topleft(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0]
            self._top = value[1]
        else:
            self._left = int(value[0])
            self._top = int(value[1])

    @topleft.deleter
    def topleft(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM LEFT CORNER PROPERTY
    @property
    def bottomleft(self):
        """
        The x and y coordinates for the bottom right corner of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.bottomleft
        (0, 20)
        >>> r.bottomleft = (30, 30)
        >>> r
        Rect(left=30, top=10, width=10, height=20)
        """
        return (self._left, self._top + self._height)

    @bottomleft.setter
    def bottomleft(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0]
            self._top = value[1] - self._height
        else:
            self._left = int(value[0])
            self._top = int(value[1]) - self._height

    @bottomleft.deleter
    def bottomleft(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # TOP RIGHT CORNER PROPERTY
    @property
    def topright(self):
        """
        The x and y coordinates for the top right corner of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.topright
        (10, 0)
        >>> r.topright = (30, 30)
        >>> r
        Rect(left=20, top=30, width=10, height=20)
        """
        return (self._left + self._width, self._top)

    @topright.setter
    def topright(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - self._width
            self._top = value[1]
        else:
            self._left = int(value[0]) - self._width
            self._top = int(value[1])

    @topright.deleter
    def topright(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM RIGHT CORNER PROPERTY
    @property
    def bottomright(self):
        """
        The x and y coordinates for the bottom right corner of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.bottomright
        (10, 20)
        >>> r.bottomright = (30, 30)
        >>> r
        Rect(left=20, top=10, width=10, height=20)
        """
        return (self._left + self._width, self._top + self._height)

    @bottomright.setter
    def bottomright(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - self._width
            self._top = value[1] - self._height
        else:
            self._left = int(value[0]) - self._width
            self._top = int(value[1]) - self._height

    @bottomright.deleter
    def bottomright(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF TOP SIDE PROPERTY
    @property
    def midtop(self):
        """
        The x and y coordinates for the midpoint of the top edge of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.midtop
        (5, 0)
        >>> r.midtop = (40, 50)
        >>> r
        Rect(left=35, top=50, width=10, height=20)
        """
        if self._enableFloat:
            return (self._left + (self._width / 2.0), self._top)
        else:
            return (self._left + (self._width // 2), self._top)

    @midtop.setter
    def midtop(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - (self._width / 2.0)
            self._top = value[1]
        else:
            self._left = int(value[0]) - (self._width // 2)
            self._top = int(value[1])

    @midtop.deleter
    def midtop(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF BOTTOM SIDE PROPERTY
    @property
    def midbottom(self):
        """
        The x and y coordinates for the midpoint of the bottom edge of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.midbottom
        (5, 20)
        >>> r.midbottom = (40, 50)
        >>> r
        Rect(left=35, top=30, width=10, height=20)
        """
        if self._enableFloat:
            return (self._left + (self._width / 2.0), self._top + self._height)
        else:
            return (self._left + (self._width // 2), self._top + self._height)

    @midbottom.setter
    def midbottom(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - (self._width / 2.0)
            self._top = value[1] - self._height
        else:
            self._left = int(value[0]) - (self._width // 2)
            self._top = int(value[1]) - self._height

    @midbottom.deleter
    def midbottom(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF LEFT SIDE PROPERTY
    @property
    def midleft(self):
        """
        The x and y coordinates for the midpoint of the left edge of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.midleft
        (0, 10)
        >>> r.midleft = (40, 50)
        >>> r
        Rect(left=40, top=40, width=10, height=20)
        """
        if self._enableFloat:
            return (self._left, self._top + (self._height / 2.0))
        else:
            return (self._left, self._top + (self._height // 2))


    @midleft.setter
    def midleft(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0]
            self._top = value[1] - (self._height / 2.0)
        else:
            self._left = int(value[0])
            self._top = int(value[1]) - (self._height // 2)

    @midleft.deleter
    def midleft(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF RIGHT SIDE PROPERTY
    @property
    def midright(self):
        """
        The x and y coordinates for the midpoint of the right edge of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.midright
        (10, 10)
        >>> r.midright = (40, 50)
        >>> r
        Rect(left=30, top=40, width=10, height=20)
        """
        if self._enableFloat:
            return (self._left + self._width, self._top + (self._height / 2.0))
        else:
            return (self._left + self._width, self._top + (self._height // 2))


    @midright.setter
    def midright(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - self._width
            self._top = value[1] - (self._height / 2.0)
        else:
            self._left = int(value[0]) - self._width
            self._top = int(value[1]) - (self._height // 2)

    @midright.deleter
    def midright(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # CENTER POINT PROPERTY
    @property
    def center(self):
        """
        The x and y coordinates for the center of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.center
        (5, 10)
        >>> r.center = (40, 50)
        >>> r
        Rect(left=35, top=40, width=10, height=20)
        """
        if self._enableFloat:
            return (self._left + (self._width / 2.0), self._top + (self._height / 2.0))
        else:
            return (self._left + (self._width // 2), self._top + (self._height // 2))

    @center.setter
    def center(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._left = value[0] - (self._width / 2.0)
            self._top = value[1] - (self._height / 2.0)
        else:
            self._left = int(value[0]) - (self._width // 2)
            self._top = int(value[1]) - (self._height // 2)

    @center.deleter
    def center(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # X COORDINATE OF CENTER POINT PROPERTY
    @property
    def centerx(self):
        """
        The x coordinate for the center of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.centerx
        5
        >>> r.centerx = 50
        >>> r
        Rect(left=45, top=0, width=10, height=20)
        """
        if self._enableFloat:
            return self._left + (self._width / 2.0)
        else:
            return self._left + (self._width // 2)

    @centerx.setter
    def centerx(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._left = value - (self._width / 2.0)
        else:
            self._left = int(value) - (self._width // 2)

    @centerx.deleter
    def centerx(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # Y COORDINATE OF CENTER POINT PROPERTY
    @property
    def centery(self):
        """
        The y coordinate for the center of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.centery
        10
        >>> r.centery = 50
        >>> r
        Rect(left=0, top=40, width=10, height=20)
        """
        if self._enableFloat:
            return self._top + (self._height / 2.0)
        else:
            return self._top + (self._height // 2)

    @centery.setter
    def centery(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._top = value - (self._height / 2.0)
        else:
            self._top = int(value) - (self._height // 2)

    @centery.deleter
    def centery(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # SIZE PROPERTY (i.e. (width, height))
    @property
    def size(self):
        """
        The width and height of the rectangle, as a tuple.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.size
        (10, 20)
        >>> r.size = (40, 50)
        >>> r
        Rect(left=0, top=0, width=40, height=50)
        """
        return (self._width, self._height)

    @size.setter
    def size(self, value):
        _checkForTwoIntOrFloatTuple(value)
        if self._enableFloat:
            self._width = value[0]
            self._height = value[1]
        else:
            self._width = int(value[0])
            self._height = int(value[1])

    @size.deleter
    def size(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # WIDTH PROPERTY
    @property
    def width(self):
        """
        The width of the rectangle. `w` is an alias for `width`.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.width
        10
        >>> r.width = 50
        >>> r
        Rect(left=0, top=0, width=50, height=20)
        """
        return self._width

    @width.setter
    def width(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._width = value
        else:
            self._width = int(value)

    @width.deleter
    def width(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))

    w = width

    # HEIGHT PROPERTY
    @property
    def height(self):
        """
        The height of the rectangle. `h` is an alias for `height`

        >>> r = Rect(0, 0, 10, 20)
        >>> r.height
        20
        >>> r.height = 50
        >>> r
        Rect(left=0, top=0, width=10, height=50)
        """
        return self._height

    @height.setter
    def height(self, value):
        _checkForIntOrFloat(value)
        if self._enableFloat:
            self._height = value
        else:
            self._height = int(value)

    @height.deleter
    def height(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))

    h = height


    # AREA PROPERTY
    @property
    def area(self):
        """The area of the `Rect`, which is simply the width times the height.
        This is a read-only attribute.

        >>> r = Rect(0, 0, 10, 20)
        >>> r.area
        200
        """
        return self._width * self._height


    # BOX PROPERTY
    @property
    def box(self):
        """A tuple of four integers: (left, top, width, height).

        >>> r = Rect(0, 0, 10, 20)
        >>> r.box
        (0, 0, 10, 20)
        >>> r.box = (5, 15, 100, 200)
        >>> r.box
        (5, 15, 100, 200)"""
        return (self._left, self._top, self._width, self._height)

    @box.setter
    def box(self, value):
        _checkForFourIntOrFloatTuple(value)
        if self._enableFloat:
            self._left   = float(value[0])
            self._top    = float(value[1])
            self._width  = float(value[2])
            self._height = float(value[3])
        else:
            self._left   = int(value[0])
            self._top    = int(value[1])
            self._width  = int(value[2])
            self._height = int(value[3])


    @box.deleter
    def box(self):
        raise PyRectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    def move(self, xOffset, yOffset):
        """Moves this Rect object by the given offsets. The xOffset and yOffset
        arguments can be any integer value, positive or negative.
        >>> r = Rect(0, 0, 100, 100)
        >>> r.move(10, 20)
        >>> r
        Rect(left=10, top=20, width=100, height=100)
        """
        _checkForIntOrFloat(xOffset)
        _checkForIntOrFloat(yOffset)
        if self._enableFloat:
            self._left += xOffset
            self._top += yOffset
        else:
            self._left += int(xOffset)
            self._top += int(yOffset)


    def copy(self):
        """Return a copied `Rect` object with the same position and size as this
        `Rect` object.

        >>> r1 = Rect(0, 0, 100, 150)
        >>> r2 = r1.copy()
        >>> r1 == r2
        True
        >>> r2
        Rect(left=0, top=0, width=100, height=150)
        """
        return Rect(self._left, self._top, self._width, self._height)


    def inflate(self, widthChange=0, heightChange=0):
        """Increases the size of this Rect object by the given offsets. The
        rectangle's center doesn't move. Negative values will shrink the
        rectangle.

        >>> r = Rect(0, 0, 100, 150)
        >>> r.inflate(20, 40)
        >>> r
        Rect(left=-10, top=-20, width=120, height=190)
        """
        originalCenter = self.center
        self.width += widthChange
        self.height += heightChange
        self.center = originalCenter


    def clamp(self, otherRect):
        """Centers this Rect object at the center of otherRect.

        >>> r1 =Rect(0, 0, 100, 100)
        >>> r2 = Rect(-20, -90, 50, 50)
        >>> r2.clamp(r1)
        >>> r2
        Rect(left=25, top=25, width=50, height=50)
        >>> r1.center == r2.center
        True
        """
        self.center = otherRect.center

    '''
    def intersection(self, otherRect):
        """Returns a new Rect object of the overlapping area between this
        Rect object and otherRect.

        `clip()` is an alias for `intersection()`.
        """
        pass

    clip = intersection
    '''

    def union(self, otherRect):
        """Adjusts the width and height to also cover the area of `otherRect`.

        >>> r1 = Rect(0, 0, 100, 100)
        >>> r2 = Rect(-10, -10, 100, 100)
        >>> r1.union(r2)
        >>> r1
        Rect(left=-10, top=-10, width=110, height=110)
        """

        # TODO - Change otherRect so that it could be a point as well.

        unionLeft   = min(self._left, otherRect._left)
        unionTop    = min(self._top, otherRect._top)
        unionRight  = max(self.right, otherRect.right)
        unionBottom = max(self.bottom, otherRect.bottom)

        self._left   = unionLeft
        self._top    = unionTop
        self._width  = unionRight - unionLeft
        self._height = unionBottom - unionTop


    def unionAll(self, otherRects):
        """Adjusts the width and height to also cover all the `Rect` objects in
        the `otherRects` sequence.

        >>> r = Rect(0, 0, 100, 100)
        >>> r1 = Rect(0, 0, 150, 100)
        >>> r2 = Rect(-10, -10, 100, 100)
        >>> r.unionAll([r1, r2])
        >>> r
        Rect(left=-10, top=-10, width=160, height=110)
        """

        # TODO - Change otherRect so that it could be a point as well.

        otherRects = list(otherRects)
        otherRects.append(self)

        unionLeft   = min([r._left  for r in otherRects])
        unionTop    = min([r._top   for r in otherRects])
        unionRight  = max([r.right  for r in otherRects])
        unionBottom = max([r.bottom for r in otherRects])

        self._left   = unionLeft
        self._top    = unionTop
        self._width  = unionRight - unionLeft
        self._height = unionBottom - unionTop

    """
    def fit(self, other):
        pass # TODO - needs to be complete
    """


    def normalize(self):
        """Rect objects with a negative width or height cover a region where the
        right/bottom edge is to the left/above of the left/top edge, respectively.
        The `normalize()` method sets the `width` and `height` to positive if they
        were negative.

        The Rect stays in the same place, though with the `top` and `left`
        attributes representing the true top and left side.

        >>> r = Rect(0, 0, -10, -20)
        >>> r.normalize()
        >>> r
        Rect(left=-10, top=-20, width=10, height=20)
        """
        if self._width < 0:
            self._width = -self._width
            self._left -= self._width
        if self._height < 0:
            self._height = -self._height
            self._top -= self._height
        # Note: No need to intify here, since the four attributes should already be ints and no multiplication was done.


    def __contains__(self, value): # for either points or other Rect objects. For Rects, the *entire* Rect must be in this Rect.
        if isinstance(value, Rect):
            return value.topleft in self and value.topright in self and value.bottomleft in self and value.bottomright in self

        # Check if value is an (x, y) sequence or a (left, top, width, height) sequence.
        try:
            len(value)
        except:
            raise PyRectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))

        if len(value) == 2:
            # Assume that value is an (x, y) sequence.
            _checkForTwoIntOrFloatTuple(value)
            x, y = value
            return self._left < x < self._left + self._width and self._top < y < self._top + self._height

        elif len(value) == 4:
            # Assume that value is an (x, y) sequence.
            _checkForFourIntOrFloatTuple(value)
            left, top, width, height = value
            return (left, top) in self and (left + width, top) in self and (left, top + height) in self and (left + width, top + height) in self
        else:
            raise PyRectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))


    def collide(self, value):
        """Returns `True` if value collides with this `Rect` object, where value can
        be an (x, y) tuple, a (left, top, width, height) box tuple, or another `Rect`
        object. If value represents a rectangular area, any part of that area
        can collide with this `Rect` object to make `collide()` return `True`.
        Otherwise, returns `False`."""

        # Note: This code is similar to __contains__(), with some minor changes
        # because __contains__() requires the rectangular are to be COMPELTELY
        # within the Rect object.
        if isinstance(value, Rect):
            return value.topleft in self or value.topright in self or value.bottomleft in self or value.bottomright in self

        # Check if value is an (x, y) sequence or a (left, top, width, height) sequence.
        try:
            len(value)
        except:
            raise PyRectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))

        if len(value) == 2:
            # Assume that value is an (x, y) sequence.
            _checkForTwoIntOrFloatTuple(value)
            x, y = value
            return self._left < x < self._left + self._width and self._top < y < self._top + self._height

        elif len(value) == 4:
            # Assume that value is an (x, y) sequence.
            left, top, width, height = value
            return (left, top) in self or (left + width, top) in self or (left, top + height) in self or (left + width, top + height) in self
        else:
            raise PyRectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))


    '''
    def collideAny(self, rectsOrPoints):
        """Returns True if any of the (x, y) or (left, top, width, height)
        tuples in rectsOrPoints is inside this Rect object.

        >> r = Rect(0, 0, 100, 100)
        >> p1 = (150, 80)
        >> p2 = (100, 100) # This point collides.
        >> r.collideAny([p1, p2])
        True
        >> r1 = Rect(50, 50, 10, 20) # This Rect collides.
        >> r.collideAny([r1])
        True
        >> r.collideAny([p1, p2, r1])
        True
        """
        # TODO - needs to be complete
        pass # returns True or False
        raise NotImplementedError
'''

    '''
    def collideAll(self, rectsOrPoints):
        """Returns True if all of the (x, y) or (left, top, width, height)
        tuples in rectsOrPoints is inside this Rect object.
        """

        pass # return a list of all rects or points that collide with any other in the argument
        raise NotImplementedError
'''

    # TODO - Add overloaded operators for + - * / and others once we can determine actual use cases for them.

    """NOTE: All of the comparison magic methods compare the box tuple of Rect
    objects. This is the behavior of the pygame Rect objects. Originally,
    I thought about having the <, <=, >, and >= operators compare the area
    of Rect objects. But at the same time, I wanted to have == and != compare
    not just area, but all four left, top, width, and height attributes.
    But that's weird to have different comparison operators comparing different
    features of a rectangular area. So I just defaulted to what Pygame does
    and compares the box tuple. This means that the == and != operators are
    the only really useful comparison operators, so I decided to ditch the
    other operators altogether and just have Rect only support == and !=.
    """

    def __eq__(self, other):
        if isinstance(other, Rect):
            return other.box == self.box
        else:
            raise PyRectException('Rect objects can only be compared with other Rect objects')


    def __ne__(self, other):
        if isinstance(other, Rect):
            return other.box != self.box
        else:
            raise PyRectException('Rect objects can only be compared with other Rect objects')



if __name__ == '__main__':
    print(doctest.testmod())

