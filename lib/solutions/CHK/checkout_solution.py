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

    if not set(skus) <= set(sku_dict.keys()):
        return -1

    for key, value in sku_dict.items():
        count = skus.count(key)

        if key == 'A':
            if count // 5:
                multiple = count // 5
                remainder = count % 5
                total += (multiple * 200)
                count = remainder

            if count // 3:
                multiple = count // 3
                remainder = count % 3
                total += (multiple * 130)
                count = remainder

            total += count * value
        elif key == 'B':
            multiple = count // 2
            remainder = count % 2
            total += (multiple * 45) + (remainder * value)
        elif key == 'E':
            multiple = count // 2

            if 'B' in skus:
                total += (-1 * sku_dict['B'] * multiple)
            total += count * value
        elif key == 'F':
            multiple = count // 3
            count += (-1 * multiple)
            total += count * value

        elif key == 'H':
            if count // 10:
                multiple = count // 10
                remainder = count % 10
                total += (multiple * 80)
                count = remainder

            if count // 5:
                multiple = count // 5
                remainder = count % 5
                total += (multiple * 45)
                count = remainder
            total += count * value
        elif key == 'K':
            multiple = count // 2
            remainder = count % 2
            total += (multiple * 150) + (remainder * value)
        elif key == 'N':
            multiple = count // 3

            if 'M' in skus:
                total += (-1 * sku_dict['M'] * multiple)
            total += count * value
        elif key == 'P':
            multiple = count // 5
            remainder = count % 5
            total += (multiple * 200) + (remainder * value)
        elif key == 'Q':
            multiple = count // 3
            remainder = count % 3
            total += (multiple * 80) + (remainder * value)
        elif key == 'R':
            multiple = count // 3

            if 'Q' in skus:
                total += (-1 * sku_dict['Q'] * multiple)
            total += count * value
        elif key == 'U':
            multiple = count // 4
            count += (-1 * multiple)
            total += count * value
        elif key == 'V':
            if count // 3:
                multiple = count // 3
                remainder = count % 3
                total += (multiple * 130)
                count = remainder

            if count // 2:
                multiple = count // 2
                remainder = count % 2
                total += (multiple * 90)
                count = remainder

            total += count * value
        else:
            total += count * value

    return total
