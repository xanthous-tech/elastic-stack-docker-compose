#! /usr/local/bin/python2

from json_minify import json_minify

fin = open('./demo_elastic_search.jl', 'r')
fout = open('./demo_es.jl', 'w')

current_line = ''

for line in fin.readlines():
  line_no_whitespace = line.replace('\n', '')
  current_line = current_line + line_no_whitespace
  if line_no_whitespace == '}':
    current_line = json_minify(current_line)
    fout.write(current_line + '\n')
    current_line = ''

fout.close()
print "done"
