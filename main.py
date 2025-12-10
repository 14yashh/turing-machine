class TuringMachine:
    def __init__(self, tape_input):
        self.tape = ['B'] + list(tape_input) + ['B']
        self.head_position = 1
        self.current_state = 'q0'
        self.halted = False

    def step(self):
        if self.head_position < 0:
            self.tape.insert(0, 'B')
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.append('B')

        char_under_head = self.tape[self.head_position]

        if self.current_state == 'q0':
            if char_under_head == '0':
                self.tape[self.head_position] = '1'
                self.head_position += 1
            elif char_under_head == '1':
                self.tape[self.head_position] = '0'
                self.head_position += 1
            elif char_under_head == 'B':
                self.head_position -= 1
                self.current_state = 'q1'
            else:
                self.halted = True

        elif self.current_state == 'q1':
            if char_under_head == '0':
                self.head_position -= 1
            elif char_under_head == '1':
                self.head_position -= 1
            elif char_under_head == 'B':
                self.head_position += 1
                self.current_state = 'q2'

        elif self.current_state == 'q2':
            self.halted = True

    def run(self):
        while not self.halted:
            self.step()
        result = "".join(self.tape).replace('B', '')
        return result

user_input = input("Enter a binary number: ")

is_valid = True
for char in user_input:
    if char not in ['0', '1']:
        is_valid = False
        break

if is_valid and user_input:
    tm = TuringMachine(user_input)
    result = tm.run()
    print(f"1's complement: {result}")
else:
    print("number invalid")