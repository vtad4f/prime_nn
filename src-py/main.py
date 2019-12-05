
from data import TrainingData, TestData, Path
from pybrain.structure.modules import SigmoidLayer, TanhLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import sys


class Activation:
   SIG  = SigmoidLayer, .5
   TANH = TanhLayer, 0
   ALL  = [SIG, TANH]
   
def Train(nn, data, n_epoch):
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
      if nn.activate([input]) > threshold:
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
   parser.add_argument('act_fcn',  type=int,     help='0=Sig, 1=Tanh', choices=range(len(Activation.ALL)))
   parser.add_argument('n_hidden', type=int)
   parser.add_argument('n_nodes',  type=int,     help='Number of nodes per hidden layer')
   parser.add_argument('--limit',  default=None, help='Optionally limit the data set sizes', metavar='N')
   parser.add_argument('--epoch',  default=None, help='Optionally set a max number of epochs', metavar='N')
   args = parser.parse_args()
   
   fcn, threshold = Activation.ALL[args.act_fcn]
   layers = [1] + [args.n_nodes]*args.n_hidden + [1]
   
   nn = buildNetwork(*layers, hiddenclass=fcn, outclass=fcn)
   
   limit = args.limit if (args.limit is None) else int(args.limit)
   epoch = args.epoch if (args.epoch is None) else int(args.epoch)
   
   Train(nn, TrainingData(Path.FIRST , limit), epoch)
   Test (nn,     TestData(Path.FIRST , limit), threshold)
   Test (nn,     TestData(Path.SECOND, limit), threshold)
   
   