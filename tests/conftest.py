import pickle

from tests.fixtures.layer import (
    layer,
    layer_error,
    coverage,
    distance,
    height,
    water,
    artificial,
)
from tests.fixtures.alpha import alpha, alpha_error
from tests.fixtures.thresholds import thresholds, thresholds_error
from tests.fixtures.mask_size import mask_size, mask_size_error
from tests.fixtures.invert import invert, invert_error
from tests.fixtures.as_array import as_array, as_array_error
from tests.fixtures.fuel_models import fuel_models, fuel_models_error
from tests.fixtures.tree_height import tree_height, tree_height_error

from tests.files.benchmarks.test_data import (
    COMPOSITE_TEST_DATA,
    DISTANCE_TEST_DATA,
    FUEL_TEST_DATA,
    HEIGHT_TEST_DATA,
    INDEX_TEST_DATA,
    SLOPE_TEST_DATA,
    ASPECT_TEST_DATA,
)


def pytest_sessionfinish(session, exitstatus):
    COMPOSITE_TEST_DATA.dump("tests/files/benchmarks/composite.pkl")

    DISTANCE_TEST_DATA.dump("tests/files/benchmarks/distance.pkl")

    FUEL_TEST_DATA.dump("tests/files/benchmarks/fuel.pkl")

    HEIGHT_TEST_DATA.dump("tests/files/benchmarks/height.pkl")

    INDEX_TEST_DATA.dump("tests/files/benchmarks/index.pkl")

    SLOPE_TEST_DATA.dump("tests/files/benchmarks/slope.pkl")
    ASPECT_TEST_DATA.dump("tests/files/benchmarks/aspect.pkl")
