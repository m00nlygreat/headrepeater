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
new_content = []

p = re.compile(f'^{head_level} .+\n$')

for i, line in enumerate(f):
    if line == "---\n":
        print('horizontal line detected')
        print(r[i])
        m = p.match(r[i+2])
        if not m:
            new_content.append(line)
            for j in range(i, 0, -1):
                if p.match(r[j]):
                    new_content.append('\n')
                    new_content.append(r[j])
                    break
        else:
            new_content.append(line)
    else:
        new_content.append(line)

print(new_content)

n = open(output_path+'\\_'+original, 'w', encoding='utf-8')

for line in new_content:
    n.write(line)

f.close()
n.close()