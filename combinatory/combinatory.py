import sys
import itertools

def generate_values(l):
  L = list(map(lambda x: ''.join(x) ,list(itertools.permutations(l, len(l)))))
  for e in L:
    print(e)

def make_subset(d, min, max, fn):
  for L in range(int(min), int(max)):
      for subset in itertools.combinations(d, L):
        fn(list(subset))

def brute_force_dict(d, min, max):
  make_subset(d, min, max, generate_values)

def make_dict_list(file_name):
  with open(file_name, encoding="utf8") as f:
      lines = f.read().splitlines()
  return lines

def main(argv):
  if len(argv) != 3:
    print("Error: Invalid paramters. Must be: filename minWords maxWords")
    print("Example:  combinatory.py words.txt 2 5")
  else:
    passDict = make_dict_list(argv[0])
    min = int(argv[1])
    max = int(argv[2])
    brute_force_dict(passDict, min, max)
    
if (__name__ == '__main__'):
  main(sys.argv[1:])