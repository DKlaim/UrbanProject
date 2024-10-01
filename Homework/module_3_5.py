def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first if first != 0 else 1


result = get_multiplied_digits(402030)
print(result)


# # Вариант с обратным условием, для самообразования =)
# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     if len(str_number) == 1:
#         return first if first != 0 else 1
#     else:
#         return first * get_multiplied_digits(int(str_number[1:]))
#
#
# result = get_multiplied_digits(40203)
# print(result)
