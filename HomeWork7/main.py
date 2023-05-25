def codingDate(user_list):
    first_res = int(user_list[3][1], 16) << 12
    second_res = int(user_list[2][1], 16) << 5
    third_res = int(user_list[1][1], 16) << 3
    fourth_res = int(user_list[0][1], 16)

    return first_res + second_res + third_res + fourth_res


def main(user_list):
    return str(codingDate(user_list))
