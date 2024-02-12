import itertools

import numpy as np
from rforge.containers.layer import Layer

PRESETS_LAYER = {
    f"{x}": Layer(array=np.full((5, 5), x))
    for x in [
        1,
        10,
        100,
        1000,
        10000,
        1.0,
        10.0,
        100.0,
        1000.0,
        10000.0,
    ]
}

PRESETS_ARRAY = {
    f"{x}": np.full((5, 5), x)
    for x in [
        1,
        10,
        100,
        1000,
        10000,
        1.0,
        10.0,
        100.0,
        1000.0,
        10000.0,
    ]
}

PRESETS_ERROR = {f"{x}": np.full((5, 5), x) for x in ["Layer", True, False, None]}


def get_combinations(data: dict):
    keys = list(data.keys())
    value_lists = list(data.values())
    combinations = list(itertools.product(*value_lists))

    list_of_dictionaries = []
    for combination in combinations:
        dictionary = dict(zip(keys, combination))
        list_of_dictionaries.append(dictionary)

    print(list_of_dictionaries)
    return list_of_dictionaries
