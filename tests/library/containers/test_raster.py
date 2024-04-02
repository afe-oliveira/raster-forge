import json
from itertools import combinations

import pytest
from rforge.library.containers.raster import Raster


def test_init(scale, layer_dict):
    r = Raster(scale, layer_dict)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert r.layers == layer_dict


def test_init_scale_error(scale_error, layer_dict):
    with pytest.raises(scale_error[1]):
        r = Raster(scale_error[0], layer_dict)


def test_init_layer_dict_error(scale, layer_dict_error):
    with pytest.raises(layer_dict_error[1]):
        r = Raster(scale, layer_dict_error[1])


def test_add(scale, layer_dict_name, layer_dict_value):
    r = Raster(scale)
    r.add_layer(layer_dict_value, layer_dict_name)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert (
        layer_dict_name in r.layers.keys()
        and r.layers[layer_dict_name] == layer_dict_value
    )


def test_add_name_error(scale, layer_dict_name_error, layer_dict_value):
    r = Raster(scale)
    with pytest.raises(layer_dict_name_error[1]):
        r.add_layer(layer_dict_value, layer_dict_name_error[0])


def test_add_layer_error(scale, layer_dict_name, layer_dict_value_error):
    r = Raster(scale)
    with pytest.raises(layer_dict_value_error[1]):
        r.add_layer(layer_dict_value_error[0], layer_dict_name)


def test_delete(scale, layer_dict_name, layer_dict_name_alt, layer_dict_value):
    r = Raster(
        scale,
        {layer_dict_name: layer_dict_value, layer_dict_name_alt: layer_dict_value},
    )
    r.remove_layer(layer_dict_name)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert layer_dict_name not in r.layers.keys()


def test_delete_error(
    scale, layer_dict_name, layer_dict_name_alt, layer_dict_value, layer_dict_name_error
):
    r = Raster(
        scale,
        {layer_dict_name: layer_dict_value, layer_dict_name_alt: layer_dict_value},
    )

    with pytest.raises(layer_dict_name_error[1]):
        r.remove_layer(layer_dict_name_error[0])


def test_edit(scale, layer_dict_name, layer_dict_name_alt, layer_dict_value):
    r = Raster(scale, {layer_dict_name: layer_dict_value})
    r.edit_layer(layer_dict_name, layer_dict_name_alt)

    assert isinstance(r, Raster)
    assert r.scale == scale
    assert layer_dict_name_alt in r.layers.keys()
    assert layer_dict_name not in r.layers.keys()
    assert r.layers[layer_dict_name_alt] == layer_dict_value


def test_edit_current_name_error(
    scale, layer_dict_name, layer_dict_name_alt, layer_dict_value, layer_dict_name_error
):
    r = Raster(scale, {layer_dict_name: layer_dict_value})

    with pytest.raises(layer_dict_name_error[1]):
        r.edit_layer(layer_dict_name_error[0], layer_dict_name_alt)


def test_edit_new_name_error(
    scale, layer_dict_name, layer_dict_value, layer_dict_name_error
):
    r = Raster(scale, {layer_dict_name: layer_dict_value})

    with pytest.raises(layer_dict_name_error[1]):
        r.edit_layer(layer_dict_name, layer_dict_name_error[0])


def test_import(data_import):
    data_path = data_import.get("data_path", None)
    info_path = data_import.get("info_path", None)
    scale = data_import.get("scale", None)

    with open(info_path, "r") as json_file:
        info = json.load(json_file)

    bands = []
    for r in range(1, info["band_num"] + 1):
        bands.extend(list(combinations(range(1, info["band_num"] + 1), r)))
    bands.append(None)

    for combination in bands:
        import_config = []
        if combination is not None:
            for i in combination:
                aux = {"id": i, "name": f"Layer {i}"}
                import_config.append(aux)
        else:
            import_config = None

        r = Raster(scale)
        r.import_layers(data_path, import_config)

        assert isinstance(r, Raster)
        assert r.scale == scale
        if combination is not None:
            assert r.count == len(combination)
        else:
            assert r.count == info["band_num"]


def test_import_errors(data_import_error):
    data_path = data_import_error.get("data_path", None)
    scale = data_import_error.get("scale", None)
    error = data_import_error.get("error", None)

    with pytest.raises(error):
        r = Raster(scale)
        r.import_layers(data_path, None)
