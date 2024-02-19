import pytest


@pytest.fixture(
    params=[
        {
            "data_path": "tests/files/sample/ADSM_1.tif",
            "info_path": "tests/files/sample/ADSM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADSM_2.tif",
            "info_path": "tests/files/sample/ADSM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADSM_3.tif",
            "info_path": "tests/files/sample/ADSM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADSM_4.tif",
            "info_path": "tests/files/sample/ADSM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADSM_5.tif",
            "info_path": "tests/files/sample/ADSM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADTM_1.tif",
            "info_path": "tests/files/sample/ADTM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADTM_2.tif",
            "info_path": "tests/files/sample/ADTM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADTM_3.tif",
            "info_path": "tests/files/sample/ADTM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADTM_4.tif",
            "info_path": "tests/files/sample/ADTM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/ADTM_5.tif",
            "info_path": "tests/files/sample/ADTM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_1.tif",
            "info_path": "tests/files/sample/AO_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_2.tif",
            "info_path": "tests/files/sample/AO_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_3.tif",
            "info_path": "tests/files/sample/AO_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_4.tif",
            "info_path": "tests/files/sample/AO_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_5.tif",
            "info_path": "tests/files/sample/AO_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_6.tif",
            "info_path": "tests/files/sample/AO_6.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_7.tif",
            "info_path": "tests/files/sample/AO_7.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_8.tif",
            "info_path": "tests/files/sample/AO_8.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_9.tif",
            "info_path": "tests/files/sample/AO_9.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_10.tif",
            "info_path": "tests/files/sample/AO_10.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_11.tif",
            "info_path": "tests/files/sample/AO_11.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_12.tif",
            "info_path": "tests/files/sample/AO_12.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_13.tif",
            "info_path": "tests/files/sample/AO_13.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_14.tif",
            "info_path": "tests/files/sample/AO_14.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_15.tif",
            "info_path": "tests/files/sample/AO_15.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_16.tif",
            "info_path": "tests/files/sample/AO_16.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_17.tif",
            "info_path": "tests/files/sample/AO_17.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_18.tif",
            "info_path": "tests/files/sample/AO_18.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_19.tif",
            "info_path": "tests/files/sample/AO_19.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/AO_20.tif",
            "info_path": "tests/files/sample/AO_20.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDSM_1.tif",
            "info_path": "tests/files/sample/SDSM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDSM_2.tif",
            "info_path": "tests/files/sample/SDSM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDSM_3.tif",
            "info_path": "tests/files/sample/SDSM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDSM_4.tif",
            "info_path": "tests/files/sample/SDSM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDSM_5.tif",
            "info_path": "tests/files/sample/SDSM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDTM_1.tif",
            "info_path": "tests/files/sample/SDTM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDTM_2.tif",
            "info_path": "tests/files/sample/SDTM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDTM_3.tif",
            "info_path": "tests/files/sample/SDTM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDTM_4.tif",
            "info_path": "tests/files/sample/SDTM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SDTM_5.tif",
            "info_path": "tests/files/sample/SDTM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_1.tif",
            "info_path": "tests/files/sample/SO_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_2.tif",
            "info_path": "tests/files/sample/SO_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_3.tif",
            "info_path": "tests/files/sample/SO_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_4.tif",
            "info_path": "tests/files/sample/SO_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_5.tif",
            "info_path": "tests/files/sample/SO_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_6.tif",
            "info_path": "tests/files/sample/SO_6.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_7.tif",
            "info_path": "tests/files/sample/SO_7.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_8.tif",
            "info_path": "tests/files/sample/SO_8.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_9.tif",
            "info_path": "tests/files/sample/SO_9.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_10.tif",
            "info_path": "tests/files/sample/SO_10.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_11.tif",
            "info_path": "tests/files/sample/SO_11.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_12.tif",
            "info_path": "tests/files/sample/SO_12.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_13.tif",
            "info_path": "tests/files/sample/SO_13.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_14.tif",
            "info_path": "tests/files/sample/SO_14.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_15.tif",
            "info_path": "tests/files/sample/SO_15.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_16.tif",
            "info_path": "tests/files/sample/SO_16.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_17.tif",
            "info_path": "tests/files/sample/SO_17.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_18.tif",
            "info_path": "tests/files/sample/SO_18.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_19.tif",
            "info_path": "tests/files/sample/SO_19.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/SO_20.tif",
            "info_path": "tests/files/sample/SO_20.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDSM_1.tif",
            "info_path": "tests/files/sample/TDSM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDSM_2.tif",
            "info_path": "tests/files/sample/TDSM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDSM_3.tif",
            "info_path": "tests/files/sample/TDSM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDSM_4.tif",
            "info_path": "tests/files/sample/TDSM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDSM_5.tif",
            "info_path": "tests/files/sample/TDSM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDTM_1.tif",
            "info_path": "tests/files/sample/TDTM_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDTM_2.tif",
            "info_path": "tests/files/sample/TDTM_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDTM_3.tif",
            "info_path": "tests/files/sample/TDTM_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDTM_4.tif",
            "info_path": "tests/files/sample/TDTM_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TDTM_5.tif",
            "info_path": "tests/files/sample/TDTM_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_1.tif",
            "info_path": "tests/files/sample/TO_1.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_2.tif",
            "info_path": "tests/files/sample/TO_2.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_3.tif",
            "info_path": "tests/files/sample/TO_3.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_4.tif",
            "info_path": "tests/files/sample/TO_4.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_5.tif",
            "info_path": "tests/files/sample/TO_5.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_6.tif",
            "info_path": "tests/files/sample/TO_6.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_7.tif",
            "info_path": "tests/files/sample/TO_7.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_8.tif",
            "info_path": "tests/files/sample/TO_8.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_9.tif",
            "info_path": "tests/files/sample/TO_9.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_10.tif",
            "info_path": "tests/files/sample/TO_10.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_11.tif",
            "info_path": "tests/files/sample/TO_11.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_12.tif",
            "info_path": "tests/files/sample/TO_12.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_13.tif",
            "info_path": "tests/files/sample/TO_13.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_14.tif",
            "info_path": "tests/files/sample/TO_14.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_15.tif",
            "info_path": "tests/files/sample/TO_15.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_16.tif",
            "info_path": "tests/files/sample/TO_16.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_17.tif",
            "info_path": "tests/files/sample/TO_17.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_18.tif",
            "info_path": "tests/files/sample/TO_18.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_19.tif",
            "info_path": "tests/files/sample/TO_19.json",
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/TO_20.tif",
            "info_path": "tests/files/sample/TO_20.json",
            "scale": 1,
        },
    ]
)
def data_import(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param


@pytest.fixture(
    params=[
        {
            "data_path": "tests/files/sample/AAAA.tif",
            "error": FileNotFoundError,
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/BBBB.tif",
            "error": FileNotFoundError,
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/CCCC.tif",
            "error": FileNotFoundError,
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/DDDD.tif",
            "error": FileNotFoundError,
            "scale": 1,
        },
        {
            "data_path": "tests/files/sample/EEEE.tif",
            "error": FileNotFoundError,
            "scale": 1,
        },
    ]
)
def data_import_error(request):
    """Fixture that defines the layer initialization data to be tested."""
    return request.param
