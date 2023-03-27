from my_dict import MyDict


def test_size_2():
    size = 2
    my_dict = MyDict(size)
    my_dict.put(1, "one")
    my_dict.put(2, "two")
    my_dict.put(3, "three")
    my_dict.get(2)
    my_dict.put(4, "four")
    assert all(elem in my_dict.data for elem in {2, 4}) and 3 not in my_dict.data


def test_size_3():
    size = 3
    my_dict = MyDict(size)
    my_dict.put(1, "one")
    my_dict.put(2, "two")
    my_dict.put(3, "three")
    my_dict.get(1)
    my_dict.get(2)
    my_dict.put(4, "four")
    assert all(elem in my_dict.data for elem in {1, 2, 4}) and 3 not in my_dict.data
