
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
   n_inputs = 1
   n_hidden = 20
   n_output = 1
   
   data_limit = 500
   n_epoch    = 100
   
   nn = buildNetwork(n_inputs, n_hidden, n_output, bias=True)
   
   Train(nn, TrainingData(Path.FIRST, data_limit), n_epoch)
   Test(nn, TestData(Path.FIRST, data_limit))
   Test(nn, TestData(Path.SECOND, data_limit))
   
   