#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            is_valid_type1 = isinstance(my_list_1[i], (int, float))
            is_valid_type2 = isinstance(my_list_2[i], (int, float))

            if not is_valid_type1 or not is_valid_type2:
                raise TypeError("wrong type")

            result.append(my_list_1[i] / my_list_2[i])

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
