import pytest

from rforge.containers.raster import Raster
from rforge.containers.layer import Layer


def test_init(data_raster_init):
    scale = data_raster_init.get("scale")
    layers = data_raster_init.get("layers")

    r = Raster(scale)
    for i in range(len(layers)):
        r.add_layer(layers[i], str(i))

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.count == len(layers)

    for i in range(len(layers)):
        r.remove_layer(str(i))

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.count == 0
