

all_count =  .0
count = .0
for line in open('data/w2v.txt'):
    all_count += 1
    spl = line.strip().split()
    if spl[3] == spl[4]:
        count += 1

print('Accuracy: %f%%' % (100 * count / all_count))
