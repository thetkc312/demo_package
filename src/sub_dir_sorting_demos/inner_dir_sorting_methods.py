class SortList:
    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort

    def sort_list(self):
        return sorted(self.list_to_sort)
    
    def reverse_list(self):
        return list(reversed(self.list_to_sort))
    
    def reverse_sort_list(self):
        return sorted(self.list_to_sort, reverse=True)
    
    def set_sort_list(self):
        return sorted(set(self.list_to_sort))
    