# TODO - We need tests for when enableFloat is True.

import os
import pytest
import sys

USING_PY_2 = sys.version_info[0] < 3

if USING_PY_2:
    ModuleNotFoundError = None

try:
    import pygame # Used for comparisons to Pygame's Rect class.
except (ModuleNotFoundError, ImportError):
    sys.exit('Pygame is required to run these tests so we can compare PygRect\'s rectangles to Pygame\'s rectangles.')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyrect


def _compareToPygameRect(rect, pygameRectLeft, pygameRectTop, pygameRectWidth, pygameRectHeight):
    rect       = pyrect.Rect(pygameRectLeft, pygameRectTop, pygameRectWidth, pygameRectHeight)
    pygameRect = pygame.Rect(pygameRectLeft, pygameRectTop, pygameRectWidth, pygameRectHeight)
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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

    with pytest.raises(pyrect.PyRectException):
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



if __name__ == '__main__':
    pytest.main()
