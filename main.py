def encrypt(value: str, depth: int) -> str:
    rail: list[list[str]] = [['\n' for _ in range(len(value))]
                             for depth in range(depth)]

    direction: bool = False
    row, col = 0, 0

    for char in range(len(value)):
        if (row == 0) or (row == depth - 1):
            direction = not direction

        rail[row][col] = value[char]
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    result: list[str] = []

    for depth in range(depth):
        for char in range(len(value)):
            if rail[depth][char] != '\n':
                result.append(rail[depth][char])

    return "".join(result)


def decrypt(value: str, depth: int) -> str:
    pass


if __name__ == "__main__":
    print(encrypt("Olivier Kobialka", 2))
    print(encrypt("Olivier Kobialka", 3))
    print(encrypt("Olivier Kobialka", 4))
    print(encrypt("Olivier Kobialka", 21))
