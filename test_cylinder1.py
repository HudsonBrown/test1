from cylinder import volume_cylinder, area_cylinder
from pytest import raises

def test_volume_cylinder():
    flag = False
    assert (volume_cylinder(1, 2), 4) == 1.5708
    assert (volume_cylinder(0.1, 4), 6) == 0.031416


def test_area_cylinder():
    assert (area_cylinder(1, 2), 4) == 7.8540
    