import pytest
from hamcrest import assert_that, close_to, is_

from shapes import *

CIRCLE_DATA = [(1.0, 6.28, 3.14), (2.0, 12.56, 12.56), (10.0, 62.8, 314.15)]

SQUARE_DATA = [(1.0, 4.0, 1.0), (2.0, 8.0, 4.0), (10.0, 40.0, 100.0)]

RECTANGLE_DATA = [
    ([1.0, 1.0], 4.0, 1.0),
    ([2.0, 3.0], 10.0, 6.0),
    ([10.0, 37.0], 94.0, 370.0),
]

TRIANGLE_DATA = [
    ([1.0, 1.0], 3.41, 0.5),
    ([3.0, 4.0], 12.0, 6.0),
    ([10.0, 2], 22.20, 10.0),
]


@pytest.mark.parametrize("radius, perimeter, _", CIRCLE_DATA)
def test_perimeter_circle(radius, perimeter, _):
    assert_that(circle_perimeter(radius), is_(close_to(perimeter, 1e-1)))


@pytest.mark.parametrize("radius, _, area", CIRCLE_DATA)
def test_area_circle(radius, _, area):
    assert_that(circle_area(radius), is_(close_to(area, 1e-1)))


@pytest.mark.parametrize("side, perimeter, _", SQUARE_DATA)
def test_perimeter_square(side, perimeter, _):
    assert_that(square_perimeter(side), is_(close_to(perimeter, 1e-1)))


@pytest.mark.parametrize("side, _, area", SQUARE_DATA)
def test_area_square(side, _, area):
    assert_that(square_area(side), is_(close_to(area, 1e-1)))


@pytest.mark.parametrize("dims, perimeter, _", RECTANGLE_DATA)
def test_perimeter_rectangle(dims, perimeter, _):
    assert_that(rectangle_perimeter(*dims), is_(close_to(perimeter, 1e-1)))


@pytest.mark.parametrize("dims, _, area", RECTANGLE_DATA)
def test_area_rectangle(dims, _, area):
    assert_that(rectangle_area(*dims), is_(close_to(area, 1e-1)))


@pytest.mark.parametrize("dims, perimeter, _", TRIANGLE_DATA)
def test_perimeter_right_triangle(dims, perimeter, _):
    assert_that(right_triangle_perimeter(*dims), is_(close_to(perimeter, 1e-1)))


@pytest.mark.parametrize("dims, _, area", TRIANGLE_DATA)
def test_area_right_right_triangle(dims, _, area):
    assert_that(right_triangle_area(*dims), is_(close_to(area, 1e-1)))
