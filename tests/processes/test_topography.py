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
    result = data_topography.get("result", None)

    s = slope(dem=dem, units=units, alpha=alpha, as_array=as_array)
    s_count = s.array.shape[-1] if len(s.array.shape) > 2 else 1
    if as_array:
        s_result = s[:, :, :-1] if s_count > 2 else s
    else:
        s_result = s.array[:, :, :-1] if s_count > 2 else s.array
    s_alpha = s.array[:, :, -1] if alpha is not None else None

    assert (as_array and isinstance(s, np.ndarray)) or (
        not as_array and isinstance(s, Layer)
    )
    assert (alpha is None and s_count == 1) or (alpha is not None and s_count == 2)
    assert s_result == result
    assert s_alpha == alpha


def test_aspect(data_topography):
    """Test aspect map creation function."""
    dem = data_topography.get("index", None)
    units = data_topography.get("parameters", None)
    alpha = data_topography.get("thresholds", None)
    as_array = data_topography.get("as_array", None)
    result = data_topography.get("result", None)

    a = aspect(dem=dem, units=units, alpha=alpha, as_array=as_array)
    a_count = a.array.shape[-1] if len(a.array.shape) > 2 else 1
    if as_array:
        a_result = a[:, :, :-1] if a_count > 2 else a
    else:
        a_result = a.array[:, :, :-1] if a_count > 2 else a.array
    a_alpha = a.array[:, :, -1] if alpha is not None else None

    assert (as_array and isinstance(a, np.ndarray)) or (
        not as_array and isinstance(a, Layer)
    )
    assert (alpha is None and a_count == 1) or (alpha is not None and a_count == 2)
    assert a_result == result
    assert a_alpha == alpha


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
