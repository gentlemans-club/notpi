import pytest
from os import path
from notpi import NotPi

def test_clear():
    sense = NotPi(init_pygame=False)

    sense.clear([0xFF, 0xFF, 0xFF])
    assert all(x==[0xFF, 0xFF, 0xFF] for x in sense.get_pixels())

    sense.clear()
    assert all(x==[0, 0, 0] for x in sense.get_pixels())

    sense.clear(0x22, 0x22, 0x22)
    assert all(x==[0x22, 0x22, 0x22] for x in sense.get_pixels())

def test_show_letter():
    sense = NotPi(init_pygame=False)

    with pytest.raises(ValueError):
        sense.show_letter("ab")

    sense.show_letter("A")

def test_set_pixels():
    sense = NotPi(init_pygame=False)

    short_list = [[1,1,1]] * 32
    full_list = [[1,1,1]] * 64

    with pytest.raises(ValueError):
        sense.set_pixels(short_list)

    sense.set_pixels(full_list)
    assert all(x==[1, 1, 1] for x in sense.get_pixels())

def test_flip_v():
    sense = NotPi(init_pygame=False)

    sense.set_pixel(0, 0, [255, 255, 255])

    assert all(x==255 for x in sense.get_pixel(0, 0))

    sense.flip_v()
    assert all(x==255 for x in sense.get_pixel(0, 7))


def test_flip_h():
    sense = NotPi(init_pygame=False)

    sense.set_pixel(0,0, [255, 255, 255])

    print(sense.get_pixel(0, 0))

    assert sense.get_pixel(0, 0) == [255, 255, 255]

    sense.flip_h()
    assert sense.get_pixel(7, 0) == [255, 255, 255]

def test_load_image():
    sense = NotPi(init_pygame=False)

    assert all(x==[0, 0, 0] for x in sense.get_pixels())

    testdir = path.dirname(path.abspath(__file__))
    sense.load_image(path.join(testdir, "test.png"))

    assert sense.get_pixel(2, 2) == [39, 130, 162]

    assert sense.get_pixel(1, 2) == [55, 161, 146]

    assert sense.get_pixel(0, 2) == [212, 166, 118]

def test_set_pixel():
    sense = NotPi(init_pygame=False)

    assert all(x==[0, 0, 0] for x in sense.get_pixels())

    sense.set_pixel(0, 0, [255, 255, 255])

    assert sense.get_pixel(0, 0) == [255, 255, 255]
