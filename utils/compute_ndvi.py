"""
author: rs
created_on: 5th March 2020
"""
import random
import numpy as np
from shapely.geometry import MultiPoint, Polygon


def get_ndvi_value(coordinates):
    """
    :param coordinates: coordinates on the land
    :return: NDVI value for the given coordinates
    """
    return random.random()


def compute_ndvi_score(land_coordinates):
    """
    :param land_coordinates: All the corners of the land
    :return: NDVI score
    """
    p = Polygon(land_coordinates)
    xmin, ymin, xmax, ymax = p.bounds
    # If the decimal degrees are not shared with much precision please increase the value of n to 1e3 or 1e7
    # This is similar to zooming in the map to ge the appropriate metric range for computation
    n = 1
    x = np.arange(np.floor(xmin * n)/n, np.ceil(xmax * n)/n, 1/n)
    y = np.arange(np.floor(ymin * n)/n, np.ceil(ymax * n)/n, 1/n)
    points = MultiPoint(np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))]))
    coordinates_inside_land = [(p.x, p.y) for p in points]
    total_no_coordinates_in_land = len(coordinates_inside_land)
    ndvi_score = 0
    for coord in coordinates_inside_land:
        ndvi_score = ndvi_score + get_ndvi_value(coord)
    ndvi_score =  ndvi_score / total_no_coordinates_in_land
    # Converting the ndvi score to the score value ranging between 300 and 900
    return 300 + (600 * ndvi_score)