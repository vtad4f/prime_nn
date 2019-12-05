
from data import TrainingData, TestData, Path
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import sys


def Train(nn, data, n_epoch):
   """
      BRIEF  Train using the data set
   """
   print("Training...")
   sys.stdout.flush()
   
   trainer = BackpropTrainer(nn, data)
   trainer.trainUntilConvergence(maxEpochs=n_epoch)
   
   
def Test(nn, data):
   """
      BRIEF  Test against the data set
   """
   print("Testing...")
   sys.stdout.flush()
   
   right = 0
   wrong = 0
   for (input, output) in data:
      if nn.activate([input]) > 0:
         if output > 0:
            right += 1
         else:
            wrong += 1
      else:
         if output > 0:
            wrong += 1
         else:
            right += 1
            
   print('right, wrong = {0}, {1} = {2:.2f}'.format(right, wrong, right / float(right + wrong)))
   sys.stdout.flush()
   
   
if __name__ == '__main__':
   """
      BRIEF  Main Execution
   """
   # Parse args
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('n_hidden'  , type=int)
   parser.add_argument('--limit', default=None, help='Optionally limit the data set sizes', metavar='N')
   parser.add_argument('--epoch', default=None, help='Optionally set a max number of epochs', metavar='N')
   args = parser.parse_args()
   
   n_inputs = 1
   n_output = 1
   
   limit = args.limit if (args.limit is None) else int(args.limit)
   epoch = args.epoch if (args.epoch is None) else int(args.epoch)
   
   nn = buildNetwork(n_inputs, args.n_hidden, n_output, bias=True)
   
   Train(nn, TrainingData(Path.FIRST , limit), epoch)
   Test (nn,     TestData(Path.FIRST , limit))
   Test (nn,     TestData(Path.SECOND, limit))
   
   