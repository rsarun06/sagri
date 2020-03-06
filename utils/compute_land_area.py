"""
author: rs
created_on: 5th March 2020
"""


def compute_land_area(land_coordinates):
    """
    To compute Area of the land by Shoelase string method (computing the polygons area)
    :param land_coordinates: Land coordinates  as a list of tuple
    :return: Land area in cents
    """
    n = len(land_coordinates)  # Number of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += land_coordinates[i][0] * land_coordinates[j][1]
        area -= land_coordinates[j][0] * land_coordinates[i][1]
    area = abs(area) / 2.0
    return area * 1e9
