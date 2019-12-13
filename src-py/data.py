

from pybrain.datasets import SupervisedDataSet
import random
import re


class Path: # https://primes.utm.edu/lists/small/millions/
   INPUT  = '../input'
   FIRST  =  INPUT + '/primes1.txt'
   SECOND =  INPUT + '/primes2.txt'
   
class Regex:
   NUMBER = re.compile(r' ([0-9]+) ', re.MULTILINE)
   
   
def Training(tuples):
   """
      BRIEF  Parse a text file containing prime numbers
   """
   data = SupervisedDataSet(1, 1)
   for input, expected in tuples:
      data.addSample([input], [expected])
   return data
   
   
def Preprocessing(data):
   """
      BRIEF  Alter the data set before training
   """
   for i in reversed(range(len(data))):
      n = data[i][0]
      if n % 2 == 0 or n % 5 == 0:
         data.pop(i)
   return data
   
   
def FirstN(fpath, low, high, data_len):
   """
      BRIEF  Take 'data_len' numbers, starting at the first prime number,
             including both primes and non-primes
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
      
   begin = primes[0]
   end = primes[0] + data_len
   primes_set = frozenset(primes)
   
   data = []
   for n in range(begin, end + 1):
      data.append((n, high if n in primes_set else low))
      
   return data
   
   
def RandomRange(fpath, low, high, data_len):
   """
      BRIEF  Take half primes and half non-primes (the first data_len/2 primes)
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
      
   max_start = len(primes) - int(data_len/2)
   start = random.randint(0, max_start)
   primes_subset = primes[start:int(start + data_len/2 + 1)]
   
   data = set(primes_subset)
   while len(data) < int(data_len * 3 / 2):
      data.add(random.randint(primes_subset[0], primes_subset[-1]))
      
   primes_subset = set(primes_subset)
   
   return [(n, high if n in primes_subset else low) for n in data]
   
   
def Random(fpath, low, high, data_len):
   """
      BRIEF  Half primes and non-primes, randomly sampled
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
      
   begin, end = primes[0], primes[-1]
   
   data = set()
   while len(data) < data_len / 2:
      data.add(primes.pop(random.randint(0, len(primes) - 1)))
      
   while len(data) < data_len:
      data.add(random.randint(begin, end))
      
   primes_subset = set(primes)
   
   return [(n, high if n in primes_subset else low) for n in data]
   
   