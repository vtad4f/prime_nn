

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
   
   end = primes[-1] if (limit is None) else (primes[0] + limit)
   for n in range(primes[0], end + 1):
      data.addSample([n], [1 if n in primes else 0])
      
   return data
   
   
def TestData(fpath, limit = None):
   """
      BRIEF  Don't bother with a SupervisedDataSet
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
      
   end = primes[-1] if (limit is None) else (primes[0] + limit)
   for n in range(primes[0], end + 1):
      yield (n, 1 if n in primes else 0)
      
      