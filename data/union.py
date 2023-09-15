import sys
sys.path.insert(1, '../../../')
from experiments import RUN1
import os
import random
import re
from tqdm import tqdm

path = '../../../ptb-induced-trees/{}-{}.txt'.format
output_dir = 'union_run1/'
KEEP_LENGTH_SAME = True

for fold in ['test','train','valid']:
    data = sum([open(path(fold, r)).readlines() for r in RUN1], [])
    data = [re.sub(r'\(.*? ', '(. ', line.strip()) for line in tqdm(data) if len(line.strip())]
    random.shuffle(data)
    if KEEP_LENGTH_SAME:
        data = data[:len(data)//len(RUN1)]
    open(os.path.join(output_dir, fold+'.txt'), 'w').write('\n'.join(data))