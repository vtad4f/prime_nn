
from nn2_data import Data, Path
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import sys

n_inputs = 1
n_hidden = 3
n_output = 1

nn = buildNetwork(n_inputs, n_hidden, n_output, bias=True)

print("Test: {0}".format(nn.activate([5])))
sys.stdout.flush()

trainer = BackpropTrainer(nn, TrainingData(Path.FIRST))
for epoch in range(100):
   print(trainer.train())
   sys.stdout.flush()
   
print("Test: {0}".format(nn.activate([5])))
sys.stdout.flush()
