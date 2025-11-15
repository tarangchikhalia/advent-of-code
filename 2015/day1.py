
def main(input: str) -> int:
    floor = 0
    for index,char in enumerate(input):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    #return floor
        if floor == -1:
           return index + 1
    return 0
    
if __name__ == "__main__":
    with open("./day1.txt", "r") as file:
        input = file.read()
    print(main(input=input))