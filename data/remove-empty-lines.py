model = 'sdiora1943591871'
fold = 'train'

with open(f'data/{model}/org-{fold}.txt', 'r') as f:
    lines = f.readlines()

print(len(lines))
lines = [line for line in lines if line.strip()]
print(len(lines))

with open(f'data/{model}/org-{fold}.txt', 'w') as f:
    f.write(''.join(lines))