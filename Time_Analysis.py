"""
Analysis.py

This file contains the analysis of the sorting algorithms implemented in the Sorting.py file.
"""
import numpy as np
import time
from typing import Any

class Gulag:
    """It represents a Gulag where disobedient comrades are imprisoned for re-education.

    Attributes:
        inmates (list[int]): The list of disobedient comrades.
    """

    def __init__(self):
        self.inmates: list[int] = []

    def imprison(self, disobedient: int) -> None:
        """Imprison a disobedient comrade.

        Args:
            disobedient (int): The disobedient(out of order) comrade to be imprisoned.
        """
        self.inmates.append(disobedient)

    def __len__(self):
        return len(self.inmates)

def sorting_time(func) -> Any:
    """It is a decorator to record the time taken to sort the data.

    Args:
        func (Any): The function to be decorated.

    Returns:
        wrapper: The decorated function.
    """
    def wrapper(*args, **kwargs) -> Any:
        """It records the time taken to sort the data.

        Returns:
            result (Any): The result of the decorated function if any.
        """
        if wrapper.depth == 0:
            wrapper.start = time.perf_counter()
        wrapper.depth += 1
        result = func(*args, **kwargs)
        wrapper.depth -= 1
        if wrapper.depth == 0:
            end = time.perf_counter()
            print(f"Time taken to examine comrades using {func.__name__}: {(end - wrapper.start)*1000:.3f} ms")
        return result
    
    wrapper.depth = 0
    wrapper.__name__ = func.__name__
    return wrapper

def Examine_Comrades(length: int = 300) -> list[int]:
    """It generates a list of random integers representing comrades.

    Args:
        length (int, optional): Numbers of comrades. Defaults to 300.

    Returns:
        list: The list containing the comrades.
    """

    data = np.random.randint(low=0, high=100, size=length)
    return data.tolist()