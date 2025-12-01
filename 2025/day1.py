
def get_password(input: str) -> int:
    password = 0
    pointer = 50
    for rotation in input:
        rotation = rotation.strip()
        direction = rotation[0]
        clicks = int(rotation[1:])
        if direction == "R":
            pointer = pointer + clicks
            pointer = pointer % 100
        elif direction == "L":
            pointer = pointer - clicks
            pointer = pointer % 100
        if pointer == 0:
            password += 1
    return password

def get_password_part2(input: str) -> int:
    """
    Count every time the dial points at 0 during any click.
    For each rotation, count how many times we pass through 0.
    """
    password = 0
    pointer = 50
    for rotation in input:
        rotation = rotation.strip()
        direction = rotation[0]
        clicks = int(rotation[1:])

        if direction == "R":
            pointer = pointer + clicks
            password += pointer // 100
            pointer = pointer % 100
        elif direction == "L":
            start_pos = pointer  # Remember where we started
            pointer = pointer - clicks
            if pointer <= 0:
                if start_pos > 0:
                    password += (abs(pointer) // 100) + 1
                else:  # start_pos == 0
                    password += abs(pointer) // 100
            pointer = pointer % 100
    return password

if __name__ == "__main__":
    with open("./day1.txt", "r") as f:
        input = f.readlines()
        print(f"Part 1: {get_password(input)}")
        print(f"Part 2: {get_password_part2(input)}")
