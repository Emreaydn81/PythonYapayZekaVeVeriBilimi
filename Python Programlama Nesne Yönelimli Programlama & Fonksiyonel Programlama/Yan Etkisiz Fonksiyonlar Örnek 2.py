# Ornek2: Olumcul Yan Etkiler
#OOP

class lineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        
def read(self):
    self.lines = [line for line in self.file]
    
def count(self):
    return len(self.lines)

lc = lineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count

