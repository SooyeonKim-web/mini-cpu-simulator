from alu import ALU
from register_file import RegisterFile
class CPU:
    def __init__(self):
        self.alu=ALU()
        self.rf=RegisterFile()
    def execute(self, command,src1,src2,ans):
        if command=="ADD":
            val1=self.rf.read(src1)
            val2=self.rf.read(src2)
            result=self.alu.add(val1,val2)
            self.rf.write(ans,result)
        elif command=="SUB":
            val1=self.rf.read(src1)
            val2=self.rf.read(src2)
            result=self.alu.sub(val1,val2)
            self.rf.write(ans,result)
        elif command=="SQRT":
            val1=self.rf.read(src1)
            result=self.alu.sqrt(val1)
            self.rf.write(ans,result)
        elif command=="MOV":
            val1=self.rf.read(src1)
            self.rf.write(ans,val1)
        elif command=="MUL":
            val1=self.rf.read(src1)
            val2=self.rf.read(src2)
            result=self.alu.mul(val1,val2)
            self.rf.write(ans, result)
        elif command=="DIV":
            val1=self.rf.read(src1)
            val2=self.rf.read(src2)
            result=self.alu.div(val1,val2)
            self.rf.write(ans, result)
cpu=CPU()
