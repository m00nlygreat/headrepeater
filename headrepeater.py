import os, sys, re

try:
    output_path = sys.argv[3]
except:
    output_path = os.getcwd()

try:
    head_level = '#'*sys.argv[2]
except:
    head_level = '##'

try:
    original = sys.argv[1]
except:
    original = 'orig.md'



print(output_path)
print(head_level)
print(os.path.isfile(sys.argv[1]))



f = open(original,"r", encoding='utf8')
r = f.readlines()
f.seek(0)
processed = []

p = re.compile(f'^{head_level} .+\n$')

for i, line in enumerate(f):
    if line == "---\n":
        # print('horizontal line detected')
        # print(r[i])
        m = p.match(r[i+2])
        if not m:
            processed.append(line)
            for j in range(i, 0, -1):
                if p.match(r[j]):
                    processed.append('\n')
                    processed.append(r[j])
                    break
        else:
            processed.append(line)
    else:
        processed.append(line)

# print(processed)

column_seperated = []

tail = -1
for i, line in enumerate(processed):
    if line == "***\n":
        before = []
        for j in range(i, 0, -1):
            if p.match(processed[j]) or processed[j] == "---\n":
                break
            else:
                if processed[j]!="***\n":
                    before.insert(0, processed[j])
                if j!=i:
                    column_seperated.pop()

        print(before)
        column_seperated.append("\n")
        column_seperated.append("::: {.columns}\n")
        column_seperated.append("::: {.column}\n")

        for line in before:
            column_seperated.append(line)

        column_seperated.append(":::\n")
        column_seperated.append("::: {.column}\n")
        tail = 0 
        after = []
        for j in range(i, len(processed)):
            if p.match(processed[j]) or processed[j] == "---\n":
                tail -= 2
                break
            else:
                after.append(processed[j])
                tail += 1
        print(tail)
    else:
        column_seperated.append(line)
        if tail == 0:
            column_seperated.append(":::\n")
            column_seperated.append(":::\n")
            column_seperated.append("\n")
        tail -= 1

n = open(output_path+'\\_'+original, 'w', encoding='utf-8')

for line in column_seperated:
    n.write(line)

f.close()
n.close()