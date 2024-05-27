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

    if not set(skus) <= {'A', 'B', 'C', 'D'}:
        return -1

    if 'A' in skus:
        a_count = skus.count('A')
        multiple = a_count // 3
        remainder = a_count % 3

        total += (multiple * 130) + (remainder * 50)

    if 'B' in skus:
        b_count = skus.count('B')
        multiple = b_count // 2
        remainder = b_count % 2

        total += (multiple * 45) + (remainder * 30)

    if 'C' in skus:
        c_count = skus.count('C')
        total += 20 * c_count

    if 'D' in skus:
        d_count = skus.count('D')
        total += 15 * d_count

    return total





