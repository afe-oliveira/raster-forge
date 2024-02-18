import numpy as np
import pytest
from rforge.containers.layer import Layer
from rforge.processes.topography import aspect, slope


def test_slope(data_topography):
    """Test slope map creation function."""
    dem = data_topography.get("dem", None)
    units = data_topography.get("units", None)
    alpha = data_topography.get("alpha", None)
    as_array = data_topography.get("as_array", None)
    result = data_topography.get("result_slope", None)

    s = slope(dem=dem, units=units, alpha=alpha, as_array=as_array)
    assert (as_array and np.allclose(s, result, atol=0.01)) or (
        not as_array and s == result
    )


def test_aspect(data_topography):
    """Test aspect map creation function."""
    dem = data_topography.get("dem", None)
    units = data_topography.get("units", None)
    alpha = data_topography.get("alpha", None)
    as_array = data_topography.get("as_array", None)
    result = data_topography.get("result_aspect", None)

    a = aspect(dem=dem, units=units, alpha=alpha, as_array=as_array)
    assert (as_array and np.allclose(a, result, atol=0.01)) or (
        not as_array and a == result
    )


def test_slope_errors(data_topography_error):
    """Test slope map creation function for expected errors."""
    dem = data_topography_error.get("dem", None)
    units = data_topography_error.get("units", None)
    alpha = data_topography_error.get("alpha", None)
    as_array = data_topography_error.get("as_array", None)
    error = data_topography_error.get("error", None)

    with pytest.raises(error):
        s = slope(dem=dem, units=units, alpha=alpha, as_array=as_array)


def test_aspect_errors(data_topography_error):
    """Test aspect map creation function for expected errors."""
    dem = data_topography_error.get("dem", None)
    units = data_topography_error.get("units", None)
    alpha = data_topography_error.get("alpha", None)
    as_array = data_topography_error.get("as_array", None)
    error = data_topography_error.get("error", None)

    with pytest.raises(error):
        a = aspect(dem=dem, units=units, alpha=alpha, as_array=as_array)
