# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not skus:
        return 0

    total = 0
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0

    if not set(skus) <= {'A', 'B', 'C', 'D', 'E'}:
        return -1

    if 'A' in skus:
        a_count += skus.count('A')

    if 'B' in skus:
        b_count += skus.count('B')

    if 'C' in skus:
        c_count += skus.count('C')

    if 'D' in skus:
        d_count += skus.count('D')

    if 'E' in skus:
        e_count += skus.count('E')
        e_multiple = e_count // 2
        e_remainder = e_count % 2

        b_count += (-1 * e_multiple)

    a_multiple = a_count // 3
    a_remainder = a_count % 3

    if a_count % 3:
        a_multiple = a_count // 3
        a_remainder = a_count % 3
        total += (a_multiple * 130) + (a_remainder * 50)
    elif a_count % 5:
        a_multiple = a_count // 5
        a_remainder = a_count % 5
        total += (a_multiple * 200) + (a_remainder * 50)
    else:
        a_remainder = a_count
        total += a_remainder * 50

    b_multiple = b_count // 2
    b_remainder = b_count % 2

    total += (b_multiple * 45) + (b_remainder * 30)
    total += 20 * c_count
    total += 15 * d_count
    total += 40 * e_count

    return total

