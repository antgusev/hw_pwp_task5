from decorator1 import logger


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.counter = -1
        self.counter_ins = 0
        self.len_list_of_list = len(list_of_list)

    def __iter__(self):
        self.counter += 1
        self.counter_ins = 0
        return self

    def __next__(self):
        if self.counter == self.len_list_of_list:
            raise StopIteration
        else:
            if self.counter_ins == len(self.list_of_list[self.counter]):
                self.counter += 1
                self.counter_ins = 0
            else:
                list_1 = self.list_of_list[self.counter]
                item = list_1[self.counter_ins]
                self.counter_ins += 1
                return item
                        

        # else:   
        #     list_1 = self.list_of_list[self.counter]
        #     item = list_1[self.counter_inside]
        #     return item


@logger
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()