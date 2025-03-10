# -*- coding: utf-8 -*-
"""greedy_matching.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Pdb8rDMR8IZeTf0RAn9JLyq5rWJD_O4
"""
import os
os.system('wget http://nlp.stanford.edu/data/wordvecs/glove.6B.zip')
os.system('unzip glove.6B.zip')
import numpy as np
import math
import itertools
embeddings_dict = {}
with open("glove.6B.300d.txt", 'r') as f:
  for line in f:
    values = line.split()
    word = values[0]
    vector = np.asarray(values[1:], "float32")
    embeddings_dict[word] = vector

def process_input(ref_list,hypo_list):
  import numpy as np
  max_score=0
  count=0
  score_sum=0
  for i,hyp_sent in enumerate(hypo_list[:-1]):
    for j, hyp in enumerate(hyp_sent.split(' ')):
      count += 1
      a=hyp.lower()
      try:
        i1 = embeddings_dict[a]
      except KeyError :
        i1= np.zeros((300,1))
      for k,ref_sent in enumerate(ref_list[:-1]):
        for l,ref in enumerate(ref_sent.split(' ')):
          b=ref.lower()
          try:
            i2 = embeddings_dict[b]
          except KeyError :
            i2 = np.zeros((300,1))
          score=sim_score(i1,i2)
          max_score=max(max_score,score)
      score_sum += max_score
      max_score = 0
  return (score_sum/count)

def sim_score(i1,i2):
  c=0
  for i in range(0,i1.shape[0]):
    c+=i1[i,0]*i2[i,0]
  cosine = c/np.sqrt(np.sum(np.multiply(i1,i1),axis=0)*np.sum(np.multiply(i2,i2),axis=0))
  return cosine

if __name__=='__main__':
  ref_list=input().split('.')
  hypo_list=input().split('.')
  score1=process_input(ref_list,hypo_list)
  score2=process_input(hypo_list,ref_list)
  print((score1+score2)/2)

