import os
import time


class TuringMachine:
    def __init__(self, tape_input):
        self.tape = ['B'] + list(tape_input) + ['B']
        self.head_position = 1
        self.current_state = 'q0'
        self.halted = False

    def print_tape(self):
        # Clear screen for animation effect
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Current State: {self.current_state}")

        border = "-" * (len(self.tape) * 4 + 1)

        content = ""
        for char in self.tape:
            content += f"| {char} "
        content += "|"

        pointer = " " * (self.head_position * 4 + 2) + "^"

        print(border)
        print(content)
        print(border)
        print(pointer)

        # Pause to let user see the step
        time.sleep(1)

    def step(self):
        # Expand tape if head moves out of bounds
        if self.head_position < 0:
            self.tape.insert(0, 'B')
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.append('B')

        char_under_head = self.tape[self.head_position]

        # --- STATE q0: Flip Bits (Move Right) ---
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

        # --- STATE q1: Rewind Head (Move Left) ---
        elif self.current_state == 'q1':
            if char_under_head == '0' or char_under_head == '1':
                self.head_position -= 1
            elif char_under_head == 'B':
                # --- STAY LOGIC ---
                # Found the start (Blank).
                # Switch to q2 (Halt) immediately. DO NOT move head.
                self.current_state = 'q2'

        # --- STATE q2: Halt ---
        elif self.current_state == 'q2':
            self.halted = True

    def run(self):
        while not self.halted:
            self.print_tape()
            self.step()

        self.print_tape()  # Show final state
        result = "".join(self.tape).replace('B', '')
        return result


# --- Main Execution ---
if __name__ == "__main__":
    user_input = input("Enter a binary number: ")

    is_valid = True
    for char in user_input:
        if char not in ['0', '1']:
            is_valid = False
            break

    if is_valid and user_input:
        tm = TuringMachine(user_input)
        result = tm.run()
        print(f"\nFinal Result (1's complement): {result}")
    else:
        print("number invalid")