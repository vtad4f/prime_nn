# Proposal
The goal of this project will be to use neural networks for prime number detection and/or factorization.
None of this matters once using quantum computers for decryption is commonplace. For now though,
whatever we come up with will need to run faster than the ECM, QS, or GNFS algorithms for large numbers
in order to be useful. That being said, in the early stages of the project the majority of time will be spent
focusing on the smaller primes (for the sake of faster run times). In any case, datasets of prime numbers
are readily available, which should make testing and training easier. It will probably be best to start by
reading the 'Shultz' article(s) described in the stackexchange page (below). We may want to repeat some of
the work they describe, but ideally we would try to find a different path forward.

# Works Consulted
- https://ai.stackexchange.com/questions/3389/could-a-neural-network-detect-primes
- https://www.quora.com/Which-is-the-fastest-prime-factorization-algorithm-to-date

# What It Accomplishes
This code (main.py) creates a neural network which could in theory be used to determine whether or not a number
is prime. The intent was for this to be a stepping stone towards prime number factorization.

# How It Does So
First a neural network is trained using a range of numbers (including either a small portion of 50% primes)
with varying degrees of randomness. The trained network is then run against a set of numbers similar to those
trained (the smallest prime and non-primes) and then the test set which starts just after the millionth prime
number. See the --help option for details.

# To Run
* source aliases.sh
* mkdir input
* setup
* cd src-py
* python main.py

# Development Notes
The majority of the development time went towards researching different python libraries that could be used
to implement a neural network. The first attempt was made with pylab, numpy and scipy, but in the end pybrain
was the best choice.

The first draft just used buildNetwork with no key word arguments. This led to some confusing results, as it
was assumed that the output layer would utilize the activation function. After some digging into the pybrain
source code it became apparent that the utility had plenty of flexibility.

Only the sig and tanh functions were attempted, as they were the simplest to implement first. There was some
experimenting with the 'recurrent' option, but it didn't seem to have any impact on the results. No attempts
were made to use the 'fast' option.

Even after fiddling significantly with randomness and a bit with preprocessing, there are very few options
that have an impact on the resulting neaural network. For the most part it simply states yes to all or no
to all numbers being primes. A few exceptions to this are present when using more random training.