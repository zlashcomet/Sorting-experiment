"""
Sorting.py

This module contains the implementation of various sorting algorithms, which I implemented
by applying knowledge from HKUST's COMP3711-Design and Analysis of Algorithms course.
"""
import numpy as np
from Time_Analysis import Gulag
from Time_Analysis import sorting_time

@sorting_time
def bubble_sort(citizens: list[int]) -> None:
    """It sorts the data using the bubble sort algorithm.

    Args:
        citizens (list[int]): The list of comrades to be sorted.
    """
    for i in range(len(citizens)):
        for j in range(0, len(citizens)-i-1):
            if citizens[j] > citizens[j+1]:
                citizens[j], citizens[j+1] = citizens[j+1], citizens[j]

@sorting_time
def insertion_sort(citizens: list[int]) -> None:
    """It sorts the data using the insertion sort algorithm.

    Args:
        citizens (list[int]): The list of comrades to be sorted.
    """
    for i in range(1, len(citizens)):
        key: int = citizens[i]
        j = i-1
        while j >= 0 and key < citizens[j]:
            citizens[j+1] = citizens[j]
            j -= 1
        citizens[j+1] = key

@sorting_time
def tim_sort(citizens: list[int]) -> None:
    """It sorts the data using the default algorithm from Python which is TimSort.

    Args:
        data (list[int]): The list of comrades to be sorted.
    """
    citizens.sort()

def merge(obedient: list[int], uneducated_comrades: list[int], citizens: list[int]) -> None:
    """It merges the obedient and behaved_comrades to form the final list of citizens.

    Args:
        obedient (list[int]): In-order comrades.
        behaved_comrades (list[int]): Disobedient comrades.
        citizens (list[int]): The list of comrades to be sorted.
    """
    oIdx: int = 0
    bIdx: int = 0
    while(oIdx < len(obedient) and bIdx < len(uneducated_comrades)):
        if uneducated_comrades[bIdx] > obedient[oIdx]:
            citizens[oIdx+bIdx] = obedient[oIdx]
            oIdx += 1
        else:
            citizens[oIdx+bIdx] = uneducated_comrades[bIdx]
            bIdx += 1
    while(oIdx < len(obedient)):
        citizens[oIdx+bIdx] = obedient[oIdx]
        oIdx += 1
    while(bIdx < len(uneducated_comrades)):
        citizens[oIdx+bIdx] = uneducated_comrades[bIdx]
        bIdx += 1

@sorting_time
def merge_sort(citizens: list[int]) -> None:
    """It sorts the data using the merge sort algorithm.

    Args:
        citizens (list[int]): The list of comrades to be sorted.
    """
    if len(citizens) > 1:
        mid = len(citizens) // 2
        L: list[int] = citizens[:mid]
        R: list[int] = citizens[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, citizens)

def partition(citizens: list[int], low: int, high: int) -> int:
    """It partitions the list of citizens for quick sort.

    Args:
        citizens (list[int]): The list of comrades to be sorted.
        low (int): The lower bound of the list.
        high (int): The upper bound of the list.

    Returns:
        i + 1 (int): The partition index.
    """
    pivot_index = np.random.randint(low, high+1)
    pivot = citizens[pivot_index]
    citizens[pivot_index], citizens[high] = citizens[high], citizens[pivot_index]
    i = low - 1
    for j in range(low, high):
        if citizens[j] <= pivot:
            i = i + 1
            citizens[i], citizens[j] = citizens[j], citizens[i]
    citizens[i + 1], citizens[high] = citizens[high], citizens[i + 1]
    return i + 1

@sorting_time
def quick_sort(citizens: list[int], low: int, high: int) -> None:
    """It sorts the data using the quick sort algorithm.

    Args:
        citizens (list[int]): The list of comrades to be sorted.
        low (int): The lower bound of the list.
        high (int): The upper bound of the list.
    """
    if low < high:
        pi = partition(citizens, low, high)
        quick_sort(citizens, low, pi - 1)
        quick_sort(citizens, pi + 1, high)

@sorting_time
def stalin_sort(citizens: list[int]) -> None:
    """It sorts the data using the Stalin sort algorithm.

    Note:
        Do NOT disobey the leader, or else O_o

    Args:
        citizens (list[int]): The list of comrades to be sorted.
    """
    obedient: list[int] = [citizens[0]]
    for i in range(1, len(citizens)):
        if citizens[i] >= obedient[-1]:
            obedient.append(citizens[i])
    citizens[:] = obedient

@sorting_time
def recursive_stalin_sort(citizens: list[int]) -> list[int]:
    """It sorts the data using the recursive Stalin sort algorithm.

    Note:
        Here we don't execute disobedient (remove elements from a list). Instead,
        we relocate the disobedient comrades to a Gulag for re-education (sorting recursively).
        After re-education, they are allowed to rejoin the obedient comrades.

    Args:
        citizens (list[int]): The list of comrades to be sorted.

    Returns:
        citizens (list[int]): The sorted list of comrades.

    """

    # Early exit if the list is empty or has only one element
    if len(citizens) <= 1 :
        return citizens
    
    gulag: Gulag = Gulag()
    obedient: list[int] = [citizens[0]]
    for i in range(1, len(citizens)):
        if citizens[i] >= obedient[-1]:
            obedient.append(citizens[i])
        else:
            gulag.imprison(citizens[i])
    if len(gulag) > 0:
        # Recursively sort the disobedient comrades to make them obedient
        educated_comrades: list[int] = recursive_stalin_sort(gulag.inmates)

        # Merge the obedient and behaved_comrades to form the final list of citizens
        merge(obedient, educated_comrades, citizens)

    return citizens