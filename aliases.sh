#!/bin/bash

function clean  { git clean -dfqX ; }
function x      { git update-index --chmod=+x $1 ; }
function reload { git fetch ; git rebase origin/master ; source aliases.sh ; }

function frun   { sbatch batch.sub ; } # run job on mst forge
function fls    { squeue -u vtad4f ; } # list running jobs
function fkill  { scancel $1       ; } # kill a running job

BASE_URL=https://primes.utm.edu/lists/small/millions
   TRAIN=primes1
    TEST=primes2

function setup
{
   [[ -f input/$TRAIN.txt && -f input/$TEST.txt ]] && return 0
   [[ ! -d input ]] && echo "Run 'mkdir input' first!"
   cd input                                   && \
   curl $BASE_URL/$TRAIN.zip -k -o $TRAIN.zip && \
   curl $BASE_URL/$TEST.zip -k -o $TEST.zip   && \
   unzip $TRAIN.zip                           && \
   unzip $TEST.zip                            && \
   rm $TRAIN.zip                              && \
   rm $TEST.zip                               && \
   cd -
}

