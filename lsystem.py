
import sys

class Lsystem:
    def __init__(self, filename = None):
        '''initializes Lsystem object with empty base and rules field'''
        self.filename = filename
        self.base = ''
        self.rules = []
        if self.filename != None:
            self.read(filename)


    def getBase(self):
        '''returns lsystem base'''
        return self.base


    def setBase(self, b):
        '''sets lsystem base'''
        self.base = b


    def getRule(self, i):
        '''returns lsystem rules'''
        return self.rules[i:]


    def addRule(self, newrule):
        '''adds new rule to lsystem rules field'''
        self.rules.append(newrule)


    def numRules(self):
        '''returns number of rules in rules field'''
        return len(self.rules)


    def read(self, filename):
        '''opens/reads file and creates lsystem rules and base'''
        self.rules = []
        file_obj = open(filename, 'r')

        for line in file_obj:
            line = line.strip()
            words = line.split(' ')
            if words[0] == 'base':
                self.setBase(words[1])
            elif words[0] == 'rule':
                self.addRule(words[1:])
                
        file_obj.close()


    def replace(self, istring):
        '''creates lsystem string'''
        tstring = ''
        for char in istring:
            found = False
            for rule in self.rules:
                if rule[0] == char:
                    tstring += rule[1]
                    found = True
                    break
            if found == False:
                tstring += char
        return tstring  

    
    def buildString(self, iterations):
        '''creates lsystem string with certain number of iterations'''
        nstring = self.base
        for i in range(iterations):
            nstring = self.replace(nstring)
        return nstring

    
def main(argv):
    '''opens file and prints lsystem'''
    if len(argv) < 2:
        print('Usage: lsystem.py <filename>')
        exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read(filename)

    print(lsys)
    print(lsys.getBase())

    for i in range( lsys.numRules() ):
        rule = lsys.getRule(i)
        print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString(iterations)
    print(lstr)

if __name__ == "__main__":
    main(sys.argv)


                



