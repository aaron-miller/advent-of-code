import re

class Password():
    def __init__(self, password_str):
        req_str, char_str, password_str = password_str.split(' ')
        self.min = int(req_str.split('-')[0])
        self.max = int(req_str.split('-')[1])
        self.char = char_str.split(':')[0]
        self.full_password = password_str

    def is_valid(self):
        if self.full_password.count(self.char) < self.min:
            return False
        elif self.full_password.count(self.char) > self.max:
            return False
        return True

assert Password("1-3 a: abcde").is_valid()
assert Password("1-3 b: cdefg").is_valid() == False
assert Password("2-9 c: ccccccccc").is_valid()

if __name__ == "__main__":
    total_count = 0
    with open('inputs/day02.txt', 'r')as f:
        for line in f.readlines():
            if Password(line).is_valid():
                total_count += 1
    print(total_count)