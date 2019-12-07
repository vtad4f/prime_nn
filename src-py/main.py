
from data import Path, Training, FirstNData, RandomRangeData
from pybrain.structure.modules import SigmoidLayer, TanhLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import sys


class Activation:
   SIG  = SigmoidLayer, 0, .5, 1
   TANH = TanhLayer, -1, 0, 1
   ALL  = [SIG, TANH]
   
def Train(nn, data, n_epoch = None):
   """
      BRIEF  Train using the data set
   """
   print("Training...")
   sys.stdout.flush()
   
   trainer = BackpropTrainer(nn, data)
   trainer.trainUntilConvergence(maxEpochs=n_epoch)
   
   
def Test(nn, data, threshold):
   """
      BRIEF  Test against the data set
   """
   print("Testing...")
   sys.stdout.flush()
   
   right = 0
   wrong = 0
   for (input, expected) in data:
      if nn.activate([input])[0] > threshold:
         if expected > threshold:
            right += 1
         else:
            wrong += 1
      else:
         if expected > threshold:
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
   parser.add_argument('act_fcn',  type=int, help='0=Sig, 1=Tanh', choices=range(len(Activation.ALL)))
   parser.add_argument('n_hidden', type=int, help='Number of hidden layers')
   parser.add_argument('n_nodes',  type=int, help='Number of nodes per hidden layer')
   parser.add_argument('n_epochs', type=int, help='Set a max number of epochs')
   parser.add_argument('data_len', type=int, help='Limit the data set size')
   args = parser.parse_args()
   
   fcn, low, mid, high = Activation.ALL[args.act_fcn]
   layers = [1] + [args.n_nodes]*args.n_hidden + [1]
   
   nn = buildNetwork(*layers, hiddenclass=fcn, outclass=fcn)
   
   Train(nn, Training(FirstNData(Path.FIRST,  low, high, args.data_len)), args.n_epochs)
   Test (nn,          FirstNData(Path.FIRST,  low, high, args.data_len) , mid)
   Test (nn,          FirstNData(Path.SECOND, low, high, args.data_len) , mid)
   
   