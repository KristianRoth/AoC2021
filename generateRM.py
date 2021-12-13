#!/usr/local/bin/python3
import os
import subprocess
import timeit
content = [
  '# 🎄 Advent of Code 2021 🎄',
  'Solutions for [Advent of Code](https://adventofcode.com/2021) 2021 written in python3. My objective this year is to [code golf](https://en.wikipedia.org/wiki/Code_golf) solutions that are somewhat fast.',
  'Every solution reads input file as it is in the AoC website. Every solution also prints solutions to both of the days problems and nothing else.',
  '## Solution info for days'
]

dirs = [f for f in os.listdir('.') if os.path.isdir(f) and f[0] != '.']
dirs.sort(key=lambda s: int(s.replace('aoc','')))

content.append('| Day | Chars | Time | #1 | #2 |')
content.append('| --- | --- | --- | --- | --- |')
for dir in dirs:
  fileName = dir + '/' + dir + '.py'
  lengthOfSolution = str(sum([ len(l) for l in open(fileName) if len(l) != 1 and l[0] != '#']) - 1)
  os.chdir(dir)
  start = timeit.default_timer()
  subprocess.call(['python3', dir+'.py'])
  time = '{:.2f}s'.format(timeit.default_timer() - start)
  os.chdir('..')
  content.append(f'| [{dir.replace("aoc", "Day ").capitalize()}]({fileName}) | {lengthOfSolution} | {time} | ✅ | ✅ |')

with open('README.md', 'w') as file:
    file.write('\n'.join(content))