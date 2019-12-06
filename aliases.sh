#!/bin/bash

function clean  { git clean -dfqX ; }
function x      { git update-index --chmod=+x $1 ; }
function reload { git fetch ; git rebase origin/master ; source aliases.sh ; }

function frun   { sbatch batch.sub ; } # run job on mst forge
function fls    { squeue -u vtad4f ; } # list running jobs
function fkill  { scancel $1       ; } # kill a running job

BASE_URL=https://primes.utm.edu/lists/small/millions

function setup
{
   [[ -f input/primes1.txt && -f input/primes2.txt ]] && return 0
   [[ ! -d input ]] && echo "Run 'mkdir input' first!"
   cd input                                     && \
   curl $BASE_URL/primes1.zip -k -o primes1.zip && \
   curl $BASE_URL/primes2.zip -k -o primes2.zip && \
   unzip primes1.zip                            && \
   unzip primes2.zip                            && \
   rm primes1.zip                               && \
   rm primes2.zip                               && \
   cd -
}

