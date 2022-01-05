Data = [int(x) for x in open(
        "1.TXT", 
        "r").read().split("\n")]

# first part
Frequency = sum(Data)
print(Frequency)

#second part
Frequency = 0
Duplicates = set()

i = 0

while True:
     Frequency += Data[i]
     if Frequency in Duplicates:
         break
     Duplicates.add(Frequency)
     i = (i + 1) % len(Data)

print(Frequency)