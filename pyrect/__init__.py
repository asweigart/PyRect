import doctest

# TODO - finish doc tests

__version__ = '0.0.1'


class RectException(Exception):
    pass # This class exists just for PyRect exceptions.



def _checkForIntOrFloat(arg):
    """Raises an exception if arg is not an int or float. Always returns None."""
    if not isinstance(arg, (int, float)):
        raise RectException('argument must be int or float, not %s' % (arg.__class__.__name__))


def _checkForInt(arg):
    """Raises an exception if arg is not an int. Always returns None."""
    if not isinstance(arg, int):
        raise RectException('argument must be int or float, not %s' % (arg.__class__.__name__))


def _checkForTwoIntOrFloatTuple(arg):
    try:
        if not isinstance(arg[0], (int, float)) or \
           not isinstance(arg[1], (int, float)):
            raise RectException('argument must be a two-item tuple containing int or float values')
    except:
        raise RectException('argument must be a two-item tuple containing int or float values')


def _checkForFourIntOrFloatTuple(arg):
    try:
        if not isinstance(arg[0], (int, float)) or \
           not isinstance(arg[1], (int, float)) or \
           not isinstance(arg[2], (int, float)) or \
           not isinstance(arg[3], (int, float)):
            raise RectException('argument must be a four-item tuple containing int or float values')
    except:
        raise RectException('argument must be a four-item tuple containing int or float values')


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
    pass # returns True or False


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

    # TODO - needs to be complete
    pass # return a list of all rects or points that collide with any other in the argument


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
        return self._enableFloat

    @enableFloat.setter
    def enableFloat(self, value):
        if not isinstance(value, bool):
            raise RectException('enableFloat must be set to a bool value')
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # LEFT SIDE PROPERTY
    @property
    def left(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    x = left # x is an alias for left


    # TOP SIDE PROPERTY
    @property
    def top(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))

    y = top # y is an alias for top


    # RIGHT SIDE PROPERTY
    @property
    def right(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM SIDE PROPERTY
    @property
    def bottom(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # TOP LEFT CORNER PROPERTY
    @property
    def topleft(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM LEFT CORNER PROPERTY
    @property
    def bottomleft(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # TOP RIGHT CORNER PROPERTY
    @property
    def topright(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOTTOM RIGHT CORNER PROPERTY
    @property
    def bottomright(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF TOP SIDE PROPERTY
    @property
    def midtop(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF BOTTOM SIDE PROPERTY
    @property
    def midbottom(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF LEFT SIDE PROPERTY
    @property
    def midleft(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # MIDDLE OF RIGHT SIDE PROPERTY
    @property
    def midright(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # CENTER POINT PROPERTY
    @property
    def center(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # X COORDINATE OF CENTER POINT PROPERTY
    @property
    def centerx(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # Y COORDINATE OF CENTER POINT PROPERTY
    @property
    def centery(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # SIZE PROPERTY (i.e. (width, height))
    @property
    def size(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # WIDTH PROPERTY
    @property
    def width(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # HEIGHT PROPERTY
    @property
    def height(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


    # BOX PROPERTY
    @property
    def box(self):
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
        raise RectException('%r object attributes aren\'t deletable' % (self.__class__.__name__))


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
        """Return a copied Rect object with the same position and size as this
        Rect object.
        >>> r1 = Rect(0, 0, 100, 150)
        >>> r2 = r1.copy()
        >>> r1 == r2
        True
        >>> r2
        Rect(left=0, top=0, width=100, height=150)
        """
        return Rect(self._left, self._top, self._width, self._height)


    def inflate(self, xOffset=0, yOffset=0):
        """Increases the size of this Rect object by the given offsets. The
        rectangle's center doesn't move. Negative values will shrink the
        rectangle.

        >>> r = Rect(0, 0, 100, 150)
        >>> r.inflate(20, 40)
        >>> r
        Rect(left=-10, top=-10, width=120, height=190)
        """
        pass


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


    def intersection(self, otherRect):
        """Returns a new Rect object of the overlapping area between this
        Rect object and otherRect.
        """
        pass

    clip = intersection


    def union(self, otherRect):
        """Adjusts the width and height to also cover the area of otherRect.

        >>> r1 = Rect(0, 0, 100, 100)
        >>> r2 = Rect(-10, -10, 100, 100)
        >>> r1.union(r2)
        >>> r1
        Rect(left=-10, top=-10, width=110, height=110)
        """
        unionLeft   = min(self._left, otherRect._left)
        unionTop    = min(self._top, otherRect._top)
        unionRight  = max(self.right, otherRect.right)
        unionBottom = max(self.bottom, otherRect.bottom)

        self._left   = unionLeft
        self._top    = unionTop
        self._width  = unionRight - unionLeft
        self._height = unionBottom - unionTop


    def unionAll(self, otherRects):
        """Adjusts the width and height to also cover all the Rect objects in
        the otherRects sequence.

        >>> r = Rect(0, 0, 100, 100)
        >>> r1 = Rect(0, 0, 150, 100)
        >>> r2 = Rect(-10, -10, 100, 100)
        >>> r.unionAll([r1, r2])
        >>> r
        Rect(left=-10, top=-10, width=160, height=110)
        """
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


    def fit(self, other):
        pass # TODO - needs to be complete


    def normalize(self):
        """Sets the width and height to positive if they were negative. The Rect stays in the same place, though with the top and left attributes representing the true top and left side."""
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
            raise RectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))

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
            raise RectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))


    def collide(self, value):
        """Returns True if value collides with this Rect object, where value can
        be an (x, y) tuple, a (left, top, width, height) tuple, or another Rect
        object. If value represents a rectangular area, any part of that area
        can collide with this Rect object to make collide() return True.
        Otherwise, returns False."""

        # Note: This code is similar to __contains__(), with some minor changes
        # because __contains__() requires the rectangular are to be COMPELTELY
        # within the Rect object.
        if isinstance(value, Rect):
            return value.topleft in self or value.topright in self or value.bottomleft in self or value.bottomright in self

        # Check if value is an (x, y) sequence or a (left, top, width, height) sequence.
        try:
            len(value)
        except:
            raise RectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))

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
            raise RectException('in <Rect> requires an (x, y) tuple, a (left, top, width, height) tuple, or a Rect object as left operand, not %s' % (value.__class__.__name__))



    def collideAny(self, rectsOrPoints):
        """Returns True if any of the (x, y) or (left, top, width, height)
        tuples in rectsOrPoints is inside this Rect object.

        >>> r = Rect(0, 0, 100, 100)
        >>> p1 = (150, 80)
        >>> p2 = (100, 100) # This point collides.
        >>> r.collideAny([p1, p2])
        True
        >>> r1 = Rect(50, 50, 10, 20) # This Rect collides.
        >>> r.collideAny([r1])
        True
        >>> r.collideAny([p1, p2, r1])
        True
        """
        # TODO - needs to be complete
        pass # returns True or False


    def collideAll(self, rectsOrPoints):
        """Returns True if all of the (x, y) or (left, top, width, height)
        tuples in rectsOrPoints is inside this Rect object.
        """

        pass # return a list of all rects or points that collide with any other in the argument

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
            raise RectException('Rect objects can only be compared with other Rect objects')


    def __ne__(self, other):
        if isinstance(other, Rect):
            return other.box != self.box
        else:
            raise RectException('Rect objects can only be compared with other Rect objects')



if __name__ == '__main__':
    doctest.testmod()

