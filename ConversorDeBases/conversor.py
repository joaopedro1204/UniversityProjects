def converter_base(num: int, b: int) -> int:
    """
    Convert a number from base 10, 2, 8 or 16 to same bases listed before. The parameter values must be given in the
    same base.

    :param num: int
    :param b: int
    :return: None
    """

# Algorithm for convert

    # start
    stack = []
    q = num

    while True:
        r = q % b
        q = q // b

        if q == 0:
            stack.insert(0, r)
            break

        else:
            stack.insert(0, r)

    # end

    # for returning the result in type int
    for k, v in enumerate(stack):
        stack[k] = str(v)

    num = ''.join(stack)

    return int(num)


n = converter_base(0b100, 0b1010)
print(n)
