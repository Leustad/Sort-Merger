# python 3.x
import heapq
import contextlib
import itertools

infiles = ['1.txt', '2.txt'] # Path to the files
line_endings = ['\n', '\n\r', '\r']

# Each file must have an empty line et the end.
for file in infiles:
    with open(file, 'r+') as f:
        last_line = f.readlines()[-1]
        if last_line[-1] not in line_endings:
            f.write('\n')

def without_dub(it):
    # Disregard the duplicated lines
    return (line for line, grp in itertools.groupby(it))
    
def keyfunc(s):
    # Decide the function key to sort with
    return s.split('\t')[1] + '\n'
    
with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(fn)) for fn in infiles]
    with open('output.txt', 'w') as f:
        f.writelines(without_dub(heapq.merge(*files, key=keyfunc))) # Disregards the duplicated line
        # f.writelines(heapq.merge(*files, key=keyfunc)) # Uses the duplicated lines