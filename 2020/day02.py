class MinMaxPasswordValidator():
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

class PositionalPasswordValidator():
    def __init__(self, password_str):
        req_str, char_str, password_str = password_str.split(' ')
        self.pos1 = int(req_str.split('-')[0])
        self.pos2 = int(req_str.split('-')[1])
        self.char = char_str.split(':')[0]
        self.full_password = password_str

    def is_valid(self):
        if not self.full_password[self.pos1 - 1] == self.char:
            if not self.full_password[self.pos2 - 1] == self.char:
                return False
        
        if self.full_password[self.pos1 - 1] == self.char:
            if self.full_password[self.pos2 - 1] == self.char:
                return False

        return True

assert MinMaxPasswordValidator("1-3 a: abcde").is_valid()
assert MinMaxPasswordValidator("1-3 b: cdefg").is_valid() == False
assert MinMaxPasswordValidator("2-9 c: ccccccccc").is_valid()

assert PositionalPasswordValidator("1-3 a: abcde").is_valid()
assert PositionalPasswordValidator("1-3 b: cdefg").is_valid() == False
assert PositionalPasswordValidator("2-9 c: ccccccccc").is_valid() == False

if __name__ == "__main__":
    p1_total_count = 0
    p2_total_count = 0
    with open('inputs/day02.txt', 'r')as f:
        for line in f.readlines():
            if MinMaxPasswordValidator(line).is_valid():
                p1_total_count += 1
            if PositionalPasswordValidator(line).is_valid():
                p2_total_count += 1
    print(f"part one: {p1_total_count}")
    print(f"part two: {p2_total_count}")