class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    def getroi(self):
        return 7
class ICICI(SBI):
    def getroi(self):
        return 6

s1 = Bank()
s2 = SBI()
s3 = ICICI()

print(s1.getroi())
print(s2.getroi())
print(s3.getroi())