import heapq

def total_wrapping_paper(input: list[str]) -> int:
    total_wp = 0
    for line in input:
        dims: list[int] = [int(x) for x in line.split("x")]
        sides: list[int] = [dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0]]
        total_wp += 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides) 
    return total_wp
    
def total_ribbon(input: list[str]) -> int:
    total_ribbon = 0
    for line in input:
        dims: list[int] = [int(x) for x in line.split("x")]
        min1, min2 = heapq.nsmallest(2, dims)
        perimeter = min1 + min1 + min2 + min2
        cubic = dims[0]*dims[1]*dims[2]
        total_ribbon += perimeter + cubic
    return total_ribbon

if __name__ == "__main__":
    with open("day2.txt", "r") as file:
        input = file.readlines()
    print(total_wrapping_paper(input))
    print(total_ribbon(input))