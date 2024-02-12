import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.fuel import fuel


def test(data_fuel):
    """Test fuel map creation function."""
    coverage = data_fuel.get("coverage", None)
    height = data_fuel.get("height", None)
    distance = data_fuel.get("distance", None)
    water = data_fuel.get("water", None)
    artificial = data_fuel.get("artificial", None)
    models = data_fuel.get("models", None)
    tree_height = data_fuel.get("tree_height", None)
    alpha = data_fuel.get("alpha", None)
    as_array = data_fuel.get("as_array", None)
    result = data_fuel.get("result", None)

    f = fuel(
        coverage=coverage,
        height=height,
        distance=distance,
        water=water,
        artificial=artificial,
        models=models,
        tree_height=tree_height,
        alpha=alpha,
        as_array=as_array,
    )
    f_count = f.array.shape[-1] if len(f.array.shape) > 2 else 1
    f_result = f.array[:, :, :-1] if f_count > 2 else f.array
    f_alpha = f.array[:, :, -1] if alpha is not None else None

    assert (as_array and isinstance(f, np.ndarray)) or (
            not as_array and isinstance(f, Layer)
    )
    assert (alpha is None and f_count == 1) or (
            alpha is not None and f_count == 2
    )
    assert f_result == result
    assert f_alpha == alpha


def test_errors(data_fuel_error):
    """Test fuel map creation function for expected errors."""
    coverage = data_fuel_error.get("coverage", None)
    height = data_fuel_error.get("height", None)
    distance = data_fuel_error.get("distance", None)
    water = data_fuel_error.get("water", None)
    artificial = data_fuel_error.get("artificial", None)
    models = data_fuel_error.get("models", None)
    tree_height = data_fuel_error.get("tree_height", None)
    alpha = data_fuel_error.get("alpha", None)
    as_array = data_fuel_error.get("as_array", None)
    error = data_fuel_error.get("error", None)

    with pytest.raises(error):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )
