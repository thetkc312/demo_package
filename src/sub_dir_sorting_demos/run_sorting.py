import inner_dir_sorting_methods as idsm

def different_sorts(important_list: list = [7, 3, 9, 1, 5, 2, 10, 8, 4, 6]):

    # Create an instance of the SortList class
    sorter = idsm.SortList(important_list)

    # Sort the list
    yield sorter.sort_list()
    yield sorter.reverse_list()
    yield sorter.reverse_sort_list()
    yield sorter.set_sort_list()
