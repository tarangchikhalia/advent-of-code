
def nice_or_naughty(input: list[str]) -> int:
    nice = 0
    for string in input:
        length = len(string)
        num_vowels = 0
        double_letters = 0
        valid_string = True
        for index, char in enumerate(string):
            if char in "aeiou":
                num_vowels += 1
            if index < length-1 and string[index+1] == char:
                double_letters += 1
            if index < length-1 and char in "acpx" and ord(char)+1 == ord(string[index+1]):
                valid_string = False
        if valid_string and num_vowels>=3 and double_letters>=1:
            nice += 1
    return nice


def nice_or_naughty2(input: list[str]) -> int:
    nice = 0
    for string in input:
        # Rule 1: contains a pair of any two letters that appears at least twice in the string without overlapping
        has_sandwich = any(string[i] == string[i+2] for i in range(len(string)-2))

        # Rule 2: Pair appears twice without overlap
        has_pair = False
        for i in range(len(string) - 1):
            pair = string[i:i+2]
            # Check if pair appears again after position i+1 (no overlap)
            if pair in string[i+2:]:
                has_pair = True
                break
        
        if has_sandwich and has_pair:
            nice += 1
    return nice

if __name__ == "__main__":
    with open("day5.txt", "r") as file:
        input = file.readlines()
        print(nice_or_naughty2(input))
        

