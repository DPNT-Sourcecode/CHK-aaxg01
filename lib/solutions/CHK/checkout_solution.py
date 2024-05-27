# noinspection PyUnusedLocal
# skus = unicode string

sku_dict = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}


def checkout(skus: str) -> int:
    if not skus:
        return 0

    total = 0
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0

    if not set(skus) <= set(sku_dict.keys()):
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

        if b_count:
            b_count += (-1 * e_multiple)

    if 'F' in skus:
        f_count += skus.count('F')
        f_multiple = f_count // 3

        f_count += (-1 * f_multiple)

    if 'G' in skus:
        g_count += skus.count('G')
    if 'H' in skus:
        h_count += skus.count('H')

    if a_count // 5:
        a_multiple = a_count // 5
        a_remainder = a_count % 5
        total += (a_multiple * 200)
        a_count = a_remainder

    if a_count // 3:
        a_multiple = a_count // 3
        a_remainder = a_count % 3
        total += (a_multiple * 130)
        a_count = a_remainder

    if h_count // 10:
        h_multiple = h_count // 10
        h_remainder = h_count % 10
        total += (h_multiple * 80)
        h_count = h_remainder

    if h_count // 5:
        h_multiple = h_count // 5
        h_remainder = h_count % 5
        total += (h_multiple * 45)
        h_count = h_remainder

    b_multiple = b_count // 2
    b_remainder = b_count % 2

    total += sku_dict['A'] * a_count
    total += (b_multiple * 45) + (b_remainder * sku_dict['B'])
    total += sku_dict['C'] * c_count
    total += sku_dict['D'] * d_count
    total += sku_dict['E'] * e_count
    total += sku_dict['F'] * f_count
    total += sku_dict['G'] * g_count
    total += sku_dict['H'] * h_count

    return total
