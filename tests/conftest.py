import pickle

from tests.fixtures.containers.array import array, array_error
from tests.fixtures.containers.bounds import bounds, bounds_error
from tests.fixtures.containers.crs import crs, crs_error
from tests.fixtures.containers.data_import import data_import, data_import_error
from tests.fixtures.containers.driver import driver, driver_error
from tests.fixtures.containers.layer_units import layer_units, layer_units_error
from tests.fixtures.containers.no_data import no_data, no_data_error
from tests.fixtures.containers.transform import transform, transform_error

from tests.fixtures.processes.layer import (
    layer,
    layer_error,
    coverage,
    distance,
    height,
    water,
    artificial,
    dtm,
    dsm,
)
from tests.fixtures.processes.alpha import alpha, alpha_error
from tests.fixtures.processes.thresholds import thresholds, thresholds_error
from tests.fixtures.processes.mask_size import mask_size, mask_size_error
from tests.fixtures.processes.as_array import as_array, as_array_error
from tests.fixtures.processes.fuel_models import fuel_models, fuel_models_error
from tests.fixtures.processes.index_id import index_id, index_id_error
from tests.fixtures.processes.binarize import binarize, binarize_error
from tests.fixtures.processes.layer_list import layer_list, layer_list_error
from tests.fixtures.processes.gamma import gamma
from tests.fixtures.processes.angle_units import angle_units, angle_units_error
from tests.fixtures.processes.index_parameters import index_parameters, index_parameters_error
from tests.fixtures.processes.tree_height import tree_height, tree_height_error
from tests.fixtures.processes.invert import invert, invert_error

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
    return
    COMPOSITE_TEST_DATA.dump("tests/files/benchmarks/composite.pkl")

    DISTANCE_TEST_DATA.dump("tests/files/benchmarks/distance.pkl")

    FUEL_TEST_DATA.dump("tests/files/benchmarks/fuel.pkl")

    HEIGHT_TEST_DATA.dump("tests/files/benchmarks/height.pkl")

    INDEX_TEST_DATA.dump("tests/files/benchmarks/index.pkl")

    SLOPE_TEST_DATA.dump("tests/files/benchmarks/slope.pkl")
    ASPECT_TEST_DATA.dump("tests/files/benchmarks/aspect.pkl")
