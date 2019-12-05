

from pybrain.datasets import SupervisedDataSet
import re


class Path: # https://primes.utm.edu/lists/small/millions/
   INPUT  = '../input'
   FIRST  =  INPUT + '/primes1.txt'
   SECOND =  INPUT + '/primes2.txt'
   
class Regex:
   NUMBER = re.compile(r' ([0-9]+) ', re.MULTILINE)
   
   
def TrainingData(fpath):
   """
      BRIEF  Parse a text file containing prime numbers
   """
   with open(fpath, 'r') as f:
      primes = map(int, Regex.NUMBER.findall(f.read()))
   
   data = SupervisedDataSet(1, 1)
   
   for n in range(primes[0], primes[0] + 500): # Keep it small for now
      data.addSample((n,), (1 if n in primes else 0,))
      
   return data
   
   