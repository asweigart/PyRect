# TODO - We need tests for when enableFloat is True.

import pytest
import sys

USING_PY_2 = sys.version_info[0] < 3

if USING_PY_2:
    ModuleNotFoundError = None

try:
    import pygame # Used for comparisons to Pygame's Rect class.
except (ModuleNotFoundError, ImportError):
    sys.exit('Pygame is required to run these tests so we can compare PygRect\'s rectangles to Pygame\'s rectangles.')

import pyrect


def _compareToPygameRect(rect, pygameRectleft, pygameRectTop, pygameRectWidth, pygameRectHeight):
    rect       = pyrect.Rect(pygameRectleft, pygameRectTop, pygameRectWidth, pygameRectHeight)
    pygameRect = pygame.Rect(pygameRectleft, pygameRectTop, pygameRectWidth, pygameRectHeight)
    assert rect.left == pygameRect.left
    assert rect.right == pygameRect.right
    assert rect.top == pygameRect.top
    assert rect.bottom == pygameRect.bottom

    assert rect.width == pygameRect.width
    assert rect.height == pygameRect.height

    assert rect.topleft == pygameRect.topleft
    assert rect.topright == pygameRect.topright
    assert rect.bottomleft == pygameRect.bottomleft
    assert rect.bottomright == pygameRect.bottomright

    assert rect.midtop == pygameRect.midtop
    assert rect.midbottom == pygameRect.midbottom
    assert rect.midleft == pygameRect.midleft
    assert rect.midleft == pygameRect.midleft

    assert rect.center == pygameRect.center
    assert rect.centerx == pygameRect.centerx
    assert rect.centery == pygameRect.centery


def test_enableFloat():
    rect = pyrect.Rect(1, 2, 10, 20)
    assert rect.enableFloat == False
    assert rect.topleft == (1, 2)
    rect.enableFloat = True
    assert rect.topleft == (1.0, 2.0)
    rect.enableFloat = False
    assert rect.topleft == (1, 2)

    with pytest.raises(pyrect.PyRectException):
        rect.enableFloat = 'invalid'

    with pytest.raises(AttributeError):
        del rect.enableFloat


def test_ctor():
    # Test basic positional and keyword arguments.
    r = pyrect.Rect(0, 1, 100, 200)
    _compareToPygameRect(r, 0, 1, 100, 200)
    assert r.left == 0
    assert r.top == 1
    assert r.width == 100
    assert r.height == 200

    r = pyrect.Rect(left=0, top=1, width=100, height=200)
    _compareToPygameRect(r, 0, 1, 100, 200)
    assert r.left == 0
    assert r.top == 1
    assert r.width == 100
    assert r.height == 200

    # Test float arguments with enableFloat
    r = pyrect.Rect(0.9, 1.9, 100.9, 200.9, enableFloat=True)
    assert r.left == 0.9
    assert r.top == 1.9
    assert r.width == 100.9
    assert r.height == 200.9

    # Test float arguments without enableFloat
    r = pyrect.Rect(0.9, 1.9, 100.9, 200.9, enableFloat=False)
    assert r.left == 0
    assert r.top == 1
    assert r.width == 100
    assert r.height == 200

    r = pyrect.Rect(0.9, 1.9, 100.9, 200.9) # enableFloat should be False by default
    assert r.left == 0
    assert r.top == 1
    assert r.width == 100
    assert r.height == 200


    # Test invalid settings
    with pytest.raises(pyrect.PyRectException):
        pyrect.Rect('invalid', 1, 100, 200)
    with pytest.raises(pyrect.PyRectException):
        pyrect.Rect(0, 'invalid', 100, 200)
    with pytest.raises(pyrect.PyRectException):
        pyrect.Rect(0, 1, 'invalid', 200)
    with pytest.raises(pyrect.PyRectException):
        pyrect.Rect(0, 1, 100, 'invalid')


def test_top():
    r = pyrect.Rect(0, 99, 100, 200)
    r.top = 0
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.top = 'invalid'

    with pytest.raises(AttributeError):
        del r.top

    r.enableFloat = True
    r.top = 99.1
    assert r.top == 99.1


def test_bottom():
    r = pyrect.Rect(0, 99, 100, 200)
    r.bottom = 200
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.bottom = 'invalid'

    with pytest.raises(AttributeError):
        del r.bottom

    r.enableFloat = True
    r.bottom = 99.1
    assert r.bottom == 99.1


def test_left():
    r = pyrect.Rect(99, 0, 100, 200)
    r.left = 0
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.left = 'invalid'

    with pytest.raises(AttributeError):
        del r.left

    r.enableFloat = True
    r.left = 99.1
    assert r.left == 99.1


def test_right():
    r = pyrect.Rect(99, 0, 100, 200)
    r.right = 100
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.right = 'invalid'

    with pytest.raises(AttributeError):
        del r.right

    r.enableFloat = True
    r.right = 99.1
    assert r.right == 99.1


def test_width():
    r = pyrect.Rect(0, 0, 101, 200)
    r.width = 100
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.width = 'invalid'

    with pytest.raises(AttributeError):
        del r.width

    r.enableFloat = True
    r.width = 99.1
    assert r.width == 99.1


def test_height():
    r = pyrect.Rect(0, 0, 100, 201)
    r.height = 200
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.height = 'invalid'

    with pytest.raises(AttributeError):
        del r.height

    r.enableFloat = True
    r.height = 99.1
    assert r.height == 99.1


def test_topleft():
    r = pyrect.Rect(0, 99, 100, 200)
    r.topleft = (100, 150)
    assert r.topleft == (100, 150)
    assert r.left == 100
    assert r.top == 150
    assert r.right == 200
    assert r.bottom == 350
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.topleft = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.topleft = 42

    with pytest.raises(AttributeError):
        del r.topleft

    r.enableFloat = True
    r.topleft = (99.1, 99.2)
    assert r.topleft == (99.1, 99.2)


def test_topright():
    r = pyrect.Rect(0, 99, 100, 200)
    r.topright = (100, 150)
    assert r.topright == (100, 150)
    assert r.left == 0
    assert r.top == 150
    assert r.right == 100
    assert r.bottom == 350
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.topright = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.topright = 42

    with pytest.raises(AttributeError):
        del r.topright

    r.enableFloat = True
    r.topright = (99.1, 99.2)
    assert r.topright == (99.1, 99.2)


def test_bottomleft():
    r = pyrect.Rect(0, 99, 100, 200)
    r.bottomleft = (100, 150)
    assert r.bottomleft == (100, 150)
    assert r.left == 100
    assert r.top == -50
    assert r.right == 200
    assert r.bottom == 150
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.bottomleft = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.bottomleft = 42

    with pytest.raises(AttributeError):
        del r.bottomleft

    r.enableFloat = True
    r.bottomleft = (99.1, 99.2)
    assert r.bottomleft == (99.1, 99.2)


def test_bottomright():
    r = pyrect.Rect(0, 99, 100, 200)
    r.bottomright = (100, 150)
    assert r.bottomright == (100, 150)
    assert r.left == 0
    assert r.top == -50
    assert r.right == 100
    assert r.bottom == 150
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.bottomright = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.bottomright = 42

    with pytest.raises(AttributeError):
        del r.bottomright

    r.enableFloat = True
    r.bottomright = (99.1, 99.2)
    assert r.bottomright == (99.1, 99.2)


def test_midleft():
    r = pyrect.Rect(0, 99, 100, 200)
    r.midleft = (100, 150)
    assert r.midleft == (100, 150)
    assert r.left == 100
    assert r.top == 50
    assert r.right == 200
    assert r.bottom == 250
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.midleft = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.midleft = 42

    with pytest.raises(AttributeError):
        del r.midleft

    r.enableFloat = True
    r.midleft = (99.1, 99.2)
    assert r.midleft == (99.1, 99.2)


def test_midright():
    r = pyrect.Rect(0, 99, 100, 200)
    r.midright = (100, 150)
    assert r.midright == (100, 150)
    assert r.left == 0
    assert r.top == 50
    assert r.right == 100
    assert r.bottom == 250
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.midright = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.midright = 42

    with pytest.raises(AttributeError):
        del r.midright

    r.enableFloat = True
    r.midright = (99.1, 99.2)
    assert r.midright == (99.1, 99.2)


def test_midtop():
    r = pyrect.Rect(0, 99, 100, 200)
    r.midtop = (100, 150)
    assert r.midtop == (100, 150)
    assert r.left == 50
    assert r.top == 150
    assert r.right == 150
    assert r.bottom == 350
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.midtop = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.midtop = 42

    with pytest.raises(AttributeError):
        del r.midtop

    r.enableFloat = True
    r.midtop = (99.1, 99.2)
    assert r.midtop == (99.1, 99.2)


def test_midbottom():
    r = pyrect.Rect(0, 99, 100, 200)
    r.midbottom = (100, 150)
    assert r.midbottom == (100, 150)
    assert r.left == 50
    assert r.top == -50
    assert r.right == 150
    assert r.bottom == 150
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.midbottom = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.midbottom = 42

    with pytest.raises(AttributeError):
        del r.midbottom

    r.enableFloat = True
    r.midbottom = (99.1, 99.2)
    assert r.midbottom == (99.1, 99.2)


def test_center():
    r = pyrect.Rect(0, 99, 100, 200)
    r.center = (100, 150)
    assert r.center == (100, 150)
    assert r.left == 50
    assert r.top == 50
    assert r.right == 150
    assert r.bottom == 250
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.center = 'invalid'
    with pytest.raises(pyrect.PyRectException):
        r.center = 42

    with pytest.raises(AttributeError):
        del r.center

    r.enableFloat = True
    r.center = (99.1, 99.2)
    assert r.center == (99.1, 99.2)


def test_centerx():
    r = pyrect.Rect(0, 150, 100, 200)
    r.centerx = 100
    assert r.centerx == 100
    assert r.left == 50
    assert r.top == 150
    assert r.right == 150
    assert r.bottom == 350
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.centerx = 'invalid'

    with pytest.raises(AttributeError):
        del r.centerx

    r.enableFloat = True
    r.centerx = 99.1
    assert r.centerx == 99.1


def test_centery():
    r = pyrect.Rect(0, 99, 100, 200)
    r.centery = 100
    assert r.centery == 100
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.PyRectException):
        r.centery = 'invalid'

    with pytest.raises(AttributeError):
        del r.centery

    r.enableFloat = True
    r.centery = 99.1
    assert r.centery == 99.1


def test_size():
    r = pyrect.Rect(0, 0, 100, 200)
    r.size = (22, 33)
    assert r.size == (22, 33)
    assert r.left == 0
    assert r.top == 0
    assert r.right == 22
    assert r.bottom == 33
    assert r.width == 22
    assert r.height == 33

    with pytest.raises(pyrect.PyRectException):
        r.size = 'invalid'

    with pytest.raises(AttributeError):
        del r.size

    r.enableFloat = True
    r.size = (99.1, 99.2)
    assert r.size == (99.1, 99.2)


def test__checkForIntOrFloat():
    pyrect._checkForIntOrFloat(42)
    pyrect._checkForIntOrFloat(3.14)
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForIntOrFloat('invalid')


def test__checkForInt():
    pyrect._checkForInt(42)
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForInt(3.14)


def test__checkForTwoIntOrFloatTuple():
    pyrect._checkForTwoIntOrFloatTuple((0, 0))
    pyrect._checkForTwoIntOrFloatTuple((0.5, 0))
    pyrect._checkForTwoIntOrFloatTuple((0, 0.5))
    pyrect._checkForTwoIntOrFloatTuple((0.5, 0.5))

    # Test invalid values
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForTwoIntOrFloatTuple('invalid')
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForTwoIntOrFloatTuple(('invalid', 0))
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForTwoIntOrFloatTuple((0, 'invalid'))
    with pytest.raises(pyrect.PyRectException):
        pyrect._checkForTwoIntOrFloatTuple(('invalid', 'invalid'))


def test_str():
    r = pyrect.Rect(20, 30, 100, 150)
    assert str(r) == '(x=20, y=30, w=100, h=150)'


def test_repr():
    r = pyrect.Rect(20, 30, 100, 150)
    assert repr(r) == 'Rect(left=20, top=30, width=100, height=150)'


def test_box():
    # Test invalid settings
    r = pyrect.Rect(0, 0, 100, 100)

    assert r.box == (0, 0, 100, 100)
    r.box = (1, 2, 3, 4)
    assert r.left == 1
    assert r.top == 2
    assert r.width == 3
    assert r.height == 4

    with pytest.raises(pyrect.PyRectException):
        r.box = ('invalid', 1, 100, 200)
    with pytest.raises(pyrect.PyRectException):
        r.box = (0, 'invalid', 100, 200)
    with pytest.raises(pyrect.PyRectException):
        r.box = (0, 1, 'invalid', 200)
    with pytest.raises(pyrect.PyRectException):
        r.box = (0, 1, 100, 'invalid')

    with pytest.raises(AttributeError):
        del r.box

    r.enableFloat = True
    assert r.box == (1.0, 2.0, 3.0, 4.0)


def test_operators():
    r1 = pyrect.Rect(0, 0, 100, 100)
    r2 = pyrect.Rect(0, 0, 100, 100)

    assert r1 == r2


def test_copy():
    r = pyrect.Rect(0, 0, 100, 100)
    c = r.copy()

    assert r == c


def test_eq_ne():
    r1 = pyrect.Rect(0, 0, 100, 100)
    r2 = pyrect.Rect(0, 0, 100, 100)

    assert r1 == r2
    assert not r1 != r2


def test_onChange_intRects():
    # TODO - using a global variable means this test can't be executed in parallel
    global spam
    def callbackFn(oldBox, newBox):
        global spam
        spam = 'changed'

    # testing side changes
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.left = 0
    assert spam == 'unchanged'
    r.left = 1000 # changing left
    assert spam == 'changed'

    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.top = 10
    assert spam == 'unchanged'
    r.top = 1000 # changing top
    assert spam == 'changed'

    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.right = 100
    assert spam == 'unchanged'
    r.right = 1000 # changing right
    assert spam == 'changed'

    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.bottom = 210
    assert spam == 'unchanged'
    r.bottom = 1000 # changing bottom
    assert spam == 'changed'

    # testing size changes
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.width = 100
    assert spam == 'unchanged'
    r.width = 1000 # changing width
    assert spam == 'changed'

    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.height = 200
    assert spam == 'unchanged'
    r.height = 1000 # changing height
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.size = (100, 200)
    assert spam == 'unchanged'
    r.size = (1000, 200) # changing width
    assert spam == 'changed'

    spam = 'unchanged'
    r.size = (1000, 1000) # changing height
    assert spam == 'changed'

    spam = 'unchanged'
    r.size = (2000, 2000) # changing width and height
    assert spam == 'changed'


    # testing corner changes
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.topleft = (0, 10)
    assert spam == 'unchanged'
    r.topleft = (1000, 10) # changing left
    assert spam == 'changed'

    spam = 'unchanged'
    r.topleft = (1000, 1000) # changing top
    assert spam == 'changed'

    spam = 'unchanged'
    r.topleft = (2000, 2000) # changing top and left
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.topright = (100, 10)
    assert spam == 'unchanged'
    r.topright = (1000, 10) # changing right
    assert spam == 'changed'

    spam = 'unchanged'
    r.topright = (1000, 1000) # changing top
    assert spam == 'changed'

    spam = 'unchanged'
    r.topright = (2000, 2000) # changing top and left
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.bottomleft = (0, 210)
    assert spam == 'unchanged'
    r.bottomleft = (1000, 10) # changing left
    assert spam == 'changed'

    spam = 'unchanged'
    r.bottomleft = (1000, 1000) # changing bottom
    assert spam == 'changed'

    spam = 'unchanged'
    r.bottomleft = (2000, 2000) # changing bottom and left
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.bottomright = (100, 210)
    assert spam == 'unchanged'
    r.bottomright = (1000, 210) # changing right
    assert spam == 'changed'

    spam = 'unchanged'
    r.bottomright = (1000, 1000) # changing bottom
    assert spam == 'changed'

    spam = 'unchanged'
    r.bottomright = (2000, 2000) # changing bottom and right
    assert spam == 'changed'


    # test midpoints
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.midleft = (0, 110)
    assert spam == 'unchanged'
    r.midleft = (1000, 110) # changing right
    assert spam == 'changed'

    spam = 'unchanged'
    r.midleft = (1000, 1000) # changing mid left
    assert spam == 'changed'

    spam = 'unchanged'
    r.midleft = (2000, 2000) # changing mid left and right
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.midright = (100, 110)
    assert spam == 'unchanged'
    r.midright = (1000, 110) # changing right
    assert spam == 'changed'

    spam = 'unchanged'
    r.midright = (1000, 1000) # changing mid right
    assert spam == 'changed'

    spam = 'unchanged'
    r.midright = (2000, 2000) # changing mid right and right
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.midtop = (50, 10)
    assert spam == 'unchanged'
    r.midtop = (1000, 10) # changing mid top
    assert spam == 'changed'

    spam = 'unchanged'
    r.midtop = (1000, 1000) # changing top
    assert spam == 'changed'

    spam = 'unchanged'
    r.midtop = (2000, 2000) # changing mid top and top
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.midbottom = (50, 210)
    assert spam == 'unchanged'
    r.midbottom = (1000, 210) # changing mid bottom
    assert spam == 'changed'

    spam = 'unchanged'
    r.midbottom = (1000, 1000) # changing bottom
    assert spam == 'changed'

    spam = 'unchanged'
    r.midbottom = (2000, 2000) # changing bottom and mid bottom
    assert spam == 'changed'

    # testing center
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.center = (50, 110)
    assert spam == 'unchanged'
    r.center = (1000, 110) # changing centerx
    assert spam == 'changed'

    spam = 'unchanged'
    r.center = (1000, 1000) # changing centery
    assert spam == 'changed'

    spam = 'unchanged'
    r.center = (2000, 2000) # changing centerx and centery
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.centerx = 50
    assert spam == 'unchanged'
    r.centerx = 1000 # changing centerx
    assert spam == 'changed'


    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.centery = 110
    assert spam == 'unchanged'
    r.centery = 1000 # changing mid bottom
    assert spam == 'changed'

    # testing box
    spam = 'unchanged'
    r = pyrect.Rect(0, 10, 100, 200, onChange=callbackFn)
    r.box = (0, 10, 100, 200)
    assert spam == 'unchanged'
    r.box = (1000, 10, 100, 200) # changing left
    assert spam == 'changed'

    spam = 'unchanged'
    r.box = (1000, 2000, 100, 200) # changing top
    assert spam == 'changed'

    spam = 'unchanged'
    r.box = (1000, 2000, 3000, 200) # changing width
    assert spam == 'changed'

    spam = 'unchanged'
    r.box = (1000, 2000, 3000, 4000) # changing height
    assert spam == 'changed'


def test_readonly():
    r = pyrect.Rect(0, 10, 100, 200, readOnly=True)
    with pytest.raises(pyrect.PyRectException):
        r.left = 1000
    with pytest.raises(pyrect.PyRectException):
        r.right = 1000
    with pytest.raises(pyrect.PyRectException):
        r.top = 1000
    with pytest.raises(pyrect.PyRectException):
        r.bottom = 1000
    with pytest.raises(pyrect.PyRectException):
        r.centerx = 1000
    with pytest.raises(pyrect.PyRectException):
        r.centery = 1000
    with pytest.raises(pyrect.PyRectException):
        r.width = 1000
    with pytest.raises(pyrect.PyRectException):
        r.height = 1000
    with pytest.raises(pyrect.PyRectException):
        r.topleft = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.topright = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.bottomleft = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.bottomright = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.size = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.midleft = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.midright = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.midtop = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.midbottom = (1000, 2000)
    with pytest.raises(pyrect.PyRectException):
        r.box = (1000, 2000, 3000, 4000)


if __name__ == '__main__':
    pytest.main()
