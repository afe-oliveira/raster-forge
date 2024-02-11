import json
import random
from itertools import combinations

import pytest

from rforge.containers.raster import Raster


def test_init(data_raster_init):
    scale = data_raster_init.get("scale")
    layers = data_raster_init.get("layers")

    r = Raster(scale, layers)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.layers == layers


def test_init_errors(data_raster_init_errors):
    scale = data_raster_init_errors.get("scale", None)
    layers = data_raster_init_errors.get("layers", None)
    error = data_raster_init_errors.get("error", None)

    with pytest.raises(error):
        r = Raster(scale, layers)


def test_add(data_raster_init):
    scale = data_raster_init.get("scale")
    layers = data_raster_init.get("layers")

    r = Raster(scale)

    for key, value in layers.items():
        r.add_layer(value, key)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.layers == layers


def test_delete(data_raster_init):
    scale = data_raster_init.get("scale")
    layers = data_raster_init.get("layers")

    r = Raster(scale, layers)
    keys = list(layers.keys())

    for key in keys:
        r.remove_layer(key)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.layers == {}


def test_edit(data_raster_init):
    scale = data_raster_init.get("scale")
    layers = data_raster_init.get("layers")

    r = Raster(scale, layers)
    original_keys = list(layers.keys())
    shuffled_keys = original_keys.copy()
    random.shuffle(shuffled_keys)
    keys = dict(zip(original_keys, shuffled_keys))

    for original_key, shuffled_key in keys.items():
        r.edit_layer(original_key, shuffled_key)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.layers == {}
    for original_key, shuffled_key in keys.items():
        assert shuffled_key in r.layers
        assert r.layers[shuffled_key] == layers[original_key]


def test_import(data_import):
    data_path = data_import.get("data_path", None)
    info_path = data_import.get("info_path", None)
    scale = data_import.get("scale", None)

    with open(info_path, 'r') as json_file:
        info = json.load(json_file)

    bands = []
    for r in range(1, info['band_num'] + 1):
        bands.extend(list(combinations(range(1, info['band_num'] + 1), r)))

    for combination in bands:
        import_config = []
        for i in combination:
            aux = {'id': i, 'name': f"Layer {i}"}
            import_config.append(aux)

        r = Raster(scale)
        r.import_layers(data_path, import_config)

        assert isinstance(r, Raster)
        assert r.scale == scale
        assert r.count == len(combination)