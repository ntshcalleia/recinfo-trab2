import math 
from hashlib import sha224, md5, blake2b, sha256, sha1, sha384, sha512
from bitarray import bitarray

hash_functions = [sha224, md5, blake2b, sha256, sha1, sha384, sha512]
prob = 0.1 # probabilidade de retornar falso positivo
n_terms = 11160 # quantidade de termos do esperada
filter_size = int(-(n_terms * math.log(prob))/(math.log(2)**2)) # número de bits do filtro
n_hashes = int((filter_size/n_terms) * math.log(2)) # número de funções hash a serem usadas (3)
if (n_hashes > len(hash_functions)):
  n_hashes = len(hash_functions)

def get_bits(terms):
  def hash_term(term):
    bits = []
    for i in range(n_hashes):
      bit = int(hash_functions[i](term.encode('utf-8')).hexdigest(), 16) % filter_size
      bits.append(bit)
    return bits
  
  if isinstance(terms, str):
    bits = hash_term(terms)
  else:
    bits = []
    for term in terms:
      bits = bits + hash_term(term)

  return bits

class BloomFilter:
  def __init__(self):
    self.bit_array = bitarray(filter_size)
    self.bit_array.setall(0) 
  
  def add(self, terms):
    bits = get_bits(terms)
    for bit in bits:
      self.bit_array[bit] = True
  
  def verify(self, terms):
    bits = get_bits(terms)
    for bit in bits:
      if self.bit_array[bit] == False:
        return False
    return True
