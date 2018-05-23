# TODO - We need tests for when enableFloat is True.

import os
import pytest
import sys

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
    with pytest.raises(pyrect.RectException):
        pyrect.Rect('invalid', 1, 100, 200)
    with pytest.raises(pyrect.RectException):
        pyrect.Rect(0, 'invalid', 100, 200)
    with pytest.raises(pyrect.RectException):
        pyrect.Rect(0, 1, 'invalid', 200)
    with pytest.raises(pyrect.RectException):
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

    with pytest.raises(pyrect.RectException):
        r.top = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.top

def test_bottom():
    r = pyrect.Rect(0, 99, 100, 200)
    r.bottom = 200
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.RectException):
        r.bottom = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.bottom

def test_left():
    r = pyrect.Rect(99, 0, 100, 200)
    r.left = 0
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.RectException):
        r.left = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.left

def test_right():
    r = pyrect.Rect(99, 0, 100, 200)
    r.right = 100
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.RectException):
        r.right = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.right

def test_width():
    r = pyrect.Rect(0, 0, 101, 200)
    r.width = 100
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.RectException):
        r.width = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.width

def test_height():
    r = pyrect.Rect(0, 0, 100, 201)
    r.height = 200
    assert r.left == 0
    assert r.top == 0
    assert r.right == 100
    assert r.bottom == 200
    assert r.width == 100
    assert r.height == 200

    with pytest.raises(pyrect.RectException):
        r.height = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.height

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

    with pytest.raises(pyrect.RectException):
        r.topleft = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.topleft = 42

    with pytest.raises(pyrect.RectException):
        del r.topleft

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

    with pytest.raises(pyrect.RectException):
        r.topright = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.topright = 42

    with pytest.raises(pyrect.RectException):
        del r.topright

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

    with pytest.raises(pyrect.RectException):
        r.bottomleft = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.bottomleft = 42

    with pytest.raises(pyrect.RectException):
        del r.bottomleft

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

    with pytest.raises(pyrect.RectException):
        r.bottomright = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.bottomright = 42

    with pytest.raises(pyrect.RectException):
        del r.bottomright

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

    with pytest.raises(pyrect.RectException):
        r.midleft = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.midleft = 42

    with pytest.raises(pyrect.RectException):
        del r.midleft

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

    with pytest.raises(pyrect.RectException):
        r.midright = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.midright = 42

    with pytest.raises(pyrect.RectException):
        del r.midright

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

    with pytest.raises(pyrect.RectException):
        r.midtop = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.midtop = 42

    with pytest.raises(pyrect.RectException):
        del r.midtop

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

    with pytest.raises(pyrect.RectException):
        r.midbottom = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.midbottom = 42

    with pytest.raises(pyrect.RectException):
        del r.midbottom

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

    with pytest.raises(pyrect.RectException):
        r.center = 'invalid'
    with pytest.raises(pyrect.RectException):
        r.center = 42

    with pytest.raises(pyrect.RectException):
        del r.center

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

    with pytest.raises(pyrect.RectException):
        r.centerx = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.centerx

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

    with pytest.raises(pyrect.RectException):
        r.centery = 'invalid'

    with pytest.raises(pyrect.RectException):
        del r.centery


def test__checkForIntOrFloat():
    pyrect._checkForIntOrFloat(42)
    pyrect._checkForIntOrFloat(3.14)
    with pytest.raises(pyrect.RectException):
        pyrect._checkForIntOrFloat('invalid')


def test__checkForTwoIntOrFloatTuple():
    pyrect._checkForTwoIntOrFloatTuple((0, 0))
    pyrect._checkForTwoIntOrFloatTuple((0.5, 0))
    pyrect._checkForTwoIntOrFloatTuple((0, 0.5))
    pyrect._checkForTwoIntOrFloatTuple((0.5, 0.5))

    # Test invalid values
    with pytest.raises(pyrect.RectException):
        pyrect._checkForTwoIntOrFloatTuple('invalid')
    with pytest.raises(pyrect.RectException):
        pyrect._checkForTwoIntOrFloatTuple(('invalid', 0))
    with pytest.raises(pyrect.RectException):
        pyrect._checkForTwoIntOrFloatTuple((0, 'invalid'))
    with pytest.raises(pyrect.RectException):
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

    with pytest.raises(pyrect.RectException):
        r.box = ('invalid', 1, 100, 200)
    with pytest.raises(pyrect.RectException):
        r.box = (0, 'invalid', 100, 200)
    with pytest.raises(pyrect.RectException):
        r.box = (0, 1, 'invalid', 200)
    with pytest.raises(pyrect.RectException):
        r.box = (0, 1, 100, 'invalid')


def test_operators():
    r1 = pyrect.Rect(0, 0, 100, 100)
    r2 = pyrect.Rect(0, 0, 100, 100)

    assert r1 == r2


if __name__ == '__main__':
    pytest.main()
