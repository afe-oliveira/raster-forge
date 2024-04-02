import hashlib
import pickle

import numpy as np
import pytest
from rforge.library.processes.fuel import fuel

from tests.files.benchmarks.test_data import FUEL_TEST_DATA

np.random.seed(42)

FUEL_TEST_DATA.clear()

with open("tests/files/benchmarks/fuel.pkl", "rb") as file:
    TESTS = pickle.load(file)


def test(
    coverage,
    height,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function."""
    input_code = hashlib.sha256(
        pickle.dumps(
            [
                coverage,
                height,
                distance,
                water,
                artificial,
                fuel_models,
                tree_height,
                alpha,
                as_array,
            ]
        )
    ).hexdigest()
    result = TESTS.get(input_code, None)

    f = fuel(
        coverage=coverage,
        height=height,
        distance=distance,
        water=water,
        artificial=artificial,
        models=fuel_models,
        tree_height=tree_height,
        alpha=alpha,
        as_array=as_array,
    )

    FUEL_TEST_DATA.add(input_code, f)

    assert (as_array and np.allclose(f, result, atol=0.01)) or (
        not as_array and f == result
    )


def test_coverage_error(
    layer_error,
    height,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        f = fuel(
            coverage=layer_error[0],
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_height_error(
    coverage,
    layer_error,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        f = fuel(
            coverage=coverage,
            height=layer_error[0],
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_distance_error(
    coverage,
    height,
    layer_error,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=layer_error[0],
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_water_error(
    coverage,
    height,
    distance,
    layer_error,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=layer_error[0],
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_artificial_error(
    coverage,
    height,
    distance,
    water,
    layer_error,
    fuel_models,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(layer_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=layer_error[0],
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_fuel_models_error(
    coverage,
    height,
    distance,
    water,
    artificial,
    fuel_models_error,
    tree_height,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(fuel_models_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models_error[0],
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array,
        )


def test_tree_height_error(
    coverage,
    height,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height_error,
    alpha,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(tree_height_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height_error[0],
            alpha=alpha,
            as_array=as_array,
        )


def test_alpha_error(
    coverage,
    height,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha_error,
    as_array,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(alpha_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha_error[0],
            as_array=as_array,
        )


def test_as_array_error(
    coverage,
    height,
    distance,
    water,
    artificial,
    fuel_models,
    tree_height,
    alpha,
    as_array_error,
):
    """Test fuel map creation function for expected errors."""
    with pytest.raises(as_array_error[1]):
        f = fuel(
            coverage=coverage,
            height=height,
            distance=distance,
            water=water,
            artificial=artificial,
            models=fuel_models,
            tree_height=tree_height,
            alpha=alpha,
            as_array=as_array_error[0],
        )
