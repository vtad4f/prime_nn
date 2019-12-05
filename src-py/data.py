

from pybrain.datasets import SupervisedDataSet
import re


class Path: # https://primes.utm.edu/lists/small/millions/
   INPUT  = '../input'
   FIRST  =  INPUT + '/primes1.txt'
   SECOND =  INPUT + '/primes2.txt'
   
class Regex:
   NUMBER = re.compile(r' ([0-9]+) ', re.MULTILINE)
   
   
def TrainingData(fpath, limit = None):
   """
      BRIEF  Parse a text file containing prime numbers
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
   
   data = SupervisedDataSet(1, 1)
   
   begin = primes[0]
   end = primes[-1] if (limit is None) else (primes[0] + limit)
   primes_set = frozenset(primes)
   
   for n in range(begin, end + 1):
      data.addSample([n], [1 if n in primes else -1])
      
   return data
   
   
def TestData(fpath, limit = None):
   """
      BRIEF  Don't bother with a SupervisedDataSet
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
      
   begin = primes[0]
   end = primes[-1] if (limit is None) else (primes[0] + limit)
   primes_set = frozenset(primes)
   
   for n in range(begin, end + 1):
      yield (n, 1 if n in primes_set else -1)
      
      