def removing_duplicate_columns(table):
    for i in range(len(table)):
        unique_list = []
        for j in range(len(table[i])):
            if table[i][j] not in unique_list:
                unique_list.append(table[i][j])
        table[i] = unique_list


def column_separation(table, separate="#"):
    for row_ind in range(len(table)):
        for coll_ind in range(len(table[row_ind])):
            if separate in table[row_ind][coll_ind]:
                separate_row = table[row_ind][coll_ind].split(separate)[::-1]
                table[row_ind] = separate_row + table[row_ind][1:]


def transformations(table, separate="@", separate1=","):
    for row_ind in range(len(table)):
        for coll_ind in range(len(table[row_ind])):
            el = table[row_ind][coll_ind]
            if "." in el:
                el = el.replace(".", "-")
                table[row_ind][coll_ind] = el
            if separate in el:
                separate_ind = el.index(separate)
                table[row_ind][coll_ind] = el[:separate_ind]
            if separate1 in el:
                separate_ind = el.index(separate1)
                table[row_ind][coll_ind] = el[:separate_ind]


def main(table):
    result_table = [row[:] for row in table]
    removing_duplicate_columns(result_table)
    column_separation(result_table)
    transformations(result_table)
    return result_table
