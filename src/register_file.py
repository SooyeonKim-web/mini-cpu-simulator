class RegisterFile:
    def __init__(self):
        self.registers = [0] * 8
    def read(self, index):
        return self.registers[index]
    def write(self, index, value):
        self.registers[index]=value
    def dump(self):
        for i,vall in enumerate(self.registers):
            print(f"R{i}:{vall}")
