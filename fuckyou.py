from itertools import combinations_with_replacement

alphabets = ['A', 'B', 'C', 'D', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for (a,b,c) in combinations_with_replacement(alphabets, 3):
    print (a + b + c)
