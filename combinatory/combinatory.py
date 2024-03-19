import sys
import itertools

passDict = ["1", "2", "3", "4", "5"]

def generate_values(l):
  L = list(map(lambda x: ''.join(x) ,list(itertools.permutations(l, len(l)))))
  for e in L:
    print(e)

def make_subset(d, fn):
  for L in range(2, 5):
      for subset in itertools.combinations(d, L):
        fn(list(subset))

def brute_force_dict(d):
  make_subset(d, generate_values)

def main(argv):
  if len(argv) == 0:
    print("Error: Missing input file")
  else:
    print(brute_force_dict(passDict))
    
if (__name__ == '__main__'):
  main(sys.argv[1:])