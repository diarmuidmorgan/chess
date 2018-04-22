#!/bin/bash

d -1 data/explodedCleanChess1.csv > data/finalExplodedChess.csv

for filename in $(ls data/explodedCleanChess*.csv); do sed 1d $filename >> data/finalExplodedChess.csv; done
