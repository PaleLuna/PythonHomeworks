def first_node(args, left, right, middle=0):
    key = 2
    match args[key]:
        case "JULIA":
            return left
        case "SQL":
            return middle
        case "CVS":
            return right


def second_node(args, left, right, middle=0):
    key = 0
    match args[key]:
        case 1963:
            return left(args, third_node(args, fourth_node(args, 0, 1), 3, 2))
        case 2008:
            return middle(args, third_node(args, 4, 6, 5), 7)
        case 1999:
            return right


def third_node(args, left, right, middle=0):
    key = 3
    match args[key]:
        case 1978:
            return left
        case 1975:
            return middle
        case 1987:
            return right


def fourth_node(args, left, right, middle=0):
    key = 4
    match args[key]:
        case 1967:
            return left
        case 2020:
            return right


def main(args):
    fucn = second_node(args, third_node, 8, fourth_node)
    return first_node(args, fucn, 10, 9)
