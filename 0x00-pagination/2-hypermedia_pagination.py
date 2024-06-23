#!/usr/bin/env python3
"""
    Hypermedia pagination
"""

from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in
    a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on
        pagination parameters.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be an integer greater than 0"

        dataset = self.dataset()
        total_items = len(dataset)
        start_index, end_index = index_range(page, page_size)

        if start_index >= total_items:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
             method that takes the same arguments
             (and defaults) as get_page and returns a dictionary
             containing the following key-value pairs:
        """
        data = self.get_page(page, page_size)
        total_itemes = len(self.dataset())
        total_pages = math.ceil(total_itemes / page_size)

        Hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return Hyper_dict
