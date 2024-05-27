# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not skus:
        return 0

    skus_lower = skus.lower()
    total = 0
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    if 'a' in skus_lower:
        a_count = skus_lower.count('a')
        multiple = a_count // 3
        remainder = a_count % 3

        total += (multiple * 130) + (remainder * 50)

    if 'b' in skus_lower:
        b_count = skus_lower.count('b')
        multiple = b_count // 2
        remainder = b_count % 2

        total += (multiple * 45) + (remainder * 30)

    if 'c' in skus_lower:
        c_count = skus_lower.count('c')
        total += 20 * c_count

    if 'd' in skus_lower:
        d_count = skus_lower.count('d')
        total += 15 * d_count

    if not a_count and not b_count and not c_count and not d_count:
        return -1

    return total



