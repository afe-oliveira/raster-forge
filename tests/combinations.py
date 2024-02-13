import itertools
import random
from typing import Optional


def get_combinations(data: dict, number: Optional[int] = None):
    keys = list(data.keys())
    combinations = list(itertools.product(*data.values()))

    list_of_dicts = [
        {key: value for key, value in zip(keys, combo)} for combo in combinations
    ]
    if number is not None:
        list_of_dicts = random.sample(list_of_dicts, min(number, len(list_of_dicts)))

    return list_of_dicts
