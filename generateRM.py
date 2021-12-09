import os
import subprocess
import timeit
content = [
  '# 🎄 Advent of Code 2021 🎄',
  'Solutions for [Advent of Code](https://adventofcode.com/2021) 2021 written in python3. My objective this year is to [code golf](https://en.wikipedia.org/wiki/Code_golf) solutions that are somewhat fast',
  'Every solution reads input file as is in the AoC website and only prints solutions for both first and second question',
  '## Solution info for days'
]

dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
dirs.sort()

for dir in dirs:
  content.append(f'#### {dir.replace("aoc", "Day ").capitalize()}')
  fileName = dir + '/' + dir + '.py'
  lengthOfSolution = str(sum([ len(l) for l in open(fileName) if len(l) != 1 and l[0] != '#']) - 1)
  os.chdir(dir)
  start = timeit.default_timer()
  subprocess.call(['time', 'python3', dir+'.py'])
  time = '{:.2f}s'.format(timeit.default_timer() - start)
  os.chdir('..')
  content.append(f'``` Characters used: {lengthOfSolution}, Execution took: {time}```')

with open('README.md', 'w') as file:
    file.write('\n\n'.join(content))