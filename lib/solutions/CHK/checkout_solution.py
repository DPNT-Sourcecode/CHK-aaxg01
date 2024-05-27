

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    skus_lower = skus.lower()
    total = 0
    if 'a' in skus_lower:
        a_count = skus_lower.count('a')

    if 'b' in skus_lower:
        b_count = skus_lower.count('b')

    if 'c' in skus_lower:
        c_count = skus_lower.count('c')
        total += 20 * c_count

    if 'd' in skus_lower:
        d_count = skus_lower.count('d')
        total += 15 * d_count

    if not a_count or not b_count or not c_count or not d_count:
        return -1



