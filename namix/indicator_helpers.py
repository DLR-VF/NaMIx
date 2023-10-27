#!/usr/bin/env python3
# coding:utf-8
"""
@module indicator_helpers.py
@author Daniel Krajzewicz
@date 31.08.2023
@copyright Institut fuer Verkehrsforschung,
           Deutsches Zentrum fuer Luft- und Raumfahrt
@description Computes colors and performs norming on indicators
@licence Eclipse Public Licence 2.0
"""
import matplotlib
import numpy
import os
import pickle


def to_colors(buildings, indicator_normed, colmap, min_value=1, max_value=10):
    """
    Converts the buildings' normed indicators to a color from the given color map

    :param buildings: buildings dataset
    :type buildings: Geopandas.GeoDataFrame:POINT
    :param indicator_normed: indicate if "origin" or "destination"
    :type indicator_normed: dict(str, float)
    :param colmap: The matplotlib colormap to use
    :type colmap: matplotlib.colors.Colormap
    :param min_value: The minimum value
    :type min_value: float
    :param max_value: The maximum value
    :type max_value: float

    :return colors: An array with colors matching the order of items in buildings
    :rtype colors: numpy.array(str)
    """
    colormap = matplotlib.colormaps[colmap]
    colors = []
    for index, row in buildings.iterrows():
        value = (indicator_normed[row.mid] - min_value) / (max_value - min_value)
        colors.append(colormap(value))
    return numpy.asarray(colors)


def load_indicator_pickle(indicator_pickle_name):
    """
    Loads and returns a dictionary of (normed) indicator values
    if the given pickle file exists. Otherwise returns None.
    :param indicator_pickle_name: The name of the pickle that contains the (normed) indicator values
    :type indicator_pickle_name: str

    :return values: A map from building ID to the respective indicator value
    :rtype values: dict(str, float)
    """
    if not os.path.exists(indicator_pickle_name):
        return None
    fd = open(indicator_pickle_name, "rb")
    indicator = pickle.load(fd)
    fd.close()
    return indicator


def write_indicator_pickle(indicator_pickle_name, indicator_values):
    """
    Writes the given values dictionary into the named file
    if the given pickle file exists. Otherwise returns None.
    :param indicator_pickle_name: The name of the pickle into which the values shall be written
    :type indicator_pickle_name: str
    :param indicator_values: A map from building ID to the respective indicator value
    :type indicator_values: dict(str, float)
    """
    fd = open(indicator_pickle_name, "wb")
    pickle.dump(indicator_values, fd)
    fd.close()


def get_normed(buildings, indicator_values):
    """
    The minimum and maximum of the indicator values is determined
    and the values are afterwards normed to be in range between 1 and 10.

    :param buildings: buildings dataset
    :type buildings: Geopandas.GeoDataFrame:POINT
    :param indicator_values: The indicator values
    :type indicator_values: dict(str, float)

    :return normed_values: A map from building ID to the respetive normed indicator value
    :rtype normed_values: dict(str, float)
    """
    mmax = None
    mmin = None
    for index, row in buildings.iterrows():
        mmin = indicator_values[row.mid] if mmin is None else min(mmin, indicator_values[row.mid])
        mmax = indicator_values[row.mid] if mmax is None else max(mmax, indicator_values[row.mid])
    indicator_normed = {}
    if mmax!=0:
        for index, row in buildings.iterrows():
            indicator_normed[row.mid] = (indicator_values[row.mid]-mmin) / (mmax-mmin) * 9. + 1.
    else:
        indicator_normed = indicator_values.copy()
    return indicator_normed


def get_reverse_normed(buildings, indicator_values):
    """
    The minimum and maximum of the indicator values is determined
    and the values are afterwards normed to be in range between 1 and 10, first,
    and the mirrored so that minimum and maximum are exchanged.

    :param buildings: buildings dataset
    :type buildings: Geopandas.GeoDataFrame:POINT
    :param indicator_values: The indicator values
    :type indicator_values: dict(str, float)

    :return normed_values: A map from building ID to the respetive normed indicator value
    :rtype normed_values: dict(str, float)
    """
    indicator_normed = get_normed(buildings, indicator_values)
    for b in indicator_normed:
        indicator_normed[b] = 11. - indicator_normed[b]
    return indicator_normed
