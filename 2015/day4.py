import hashlib

def main(input:str):
    prefix = "000000"
    num = 1
    while True:
        string = input + str(num)
        encoded_str = string.encode("utf-8")
        md5_hash = hashlib.md5()
        md5_hash.update(encoded_str)
        hex_digest = md5_hash.hexdigest()
        if hex_digest[:6] == prefix:
            print(num)
            break
        num += 1


if __name__ == "__main__":
    input = "bgvyzdsv"
    # encoded_str = input.encode("utf-8")
    # md5_hash = hashlib.md5()
    # md5_hash.update(encoded_str)
    # hex_digest = md5_hash.hexdigest()
    # print(hex_digest)
    main(input)
