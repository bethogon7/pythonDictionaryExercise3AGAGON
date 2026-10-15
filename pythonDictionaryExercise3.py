fname = input("Enter file name: ")

fhand = open(fname)

counts = dict()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

print(counts)



