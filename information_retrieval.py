import re, datetime
from bloomfilter import BloomFilter
from bitarray import bitarray

def tokenize_terms(terms):
  return [(term.lower()) for term in re.split("\W+", terms)]

class Document:
  def __init__(self, terms, doc_id):
    self.id = doc_id
    self.terms = terms
    self.terms = tokenize_terms(self.terms)
    self.signature = BloomFilter()
    self.signature.add(self.terms)

  def verify(self, query):
    if isinstance(query, str):
      if query not in self.terms:
        return False
    elif isinstance(query, list):
      for term in query:
        if term not in self.terms:
          return False
    else:
      return False
    return True

class SignatureIndex:
  def __init__(self):
    self.docs = {}
  
  def __len__(self):
    return len(self.docs) # number of documents in index

  def add(self, doc):
    self.docs[doc.id] = doc
  
  def verify(self, query):
    result = []
    for doc_id in self.docs:
      if (self.docs[doc_id].signature.verify(query)):
        result.append(doc_id)
    return result
  
  def test(self, query_string):
    print("Query: " + query_string)
    query = tokenize_terms(query_string)
    false_positives = 0
    a = datetime.datetime.now()
    result = self.verify(query)
    b = datetime.datetime.now()
    c = b - a
    print("Query processing time: " + str(c.total_seconds()) + "s")
    for doc_id in result:
      if (self.docs[doc_id].verify(query) == False):
        false_positives = false_positives + 1

    if len(result) > 0:
      print("False positives: " + str(false_positives/len(result)*100) + "%")
    print(str(len(result)) + " match(es) out of " + str(len(self)) + " documents.\n")

class InvertedIndex:
  def __init__(self):
    self.terms = {}
    self.n = 0
  
  def __len__(self):
    return self.n
  
  def add(self, doc):
    for term in doc.terms:
      if term in self.terms:
        self.terms[term].append(doc)
      else:
        self.terms[term] = []
        self.terms[term].append(doc)
    self.n = self.n + 1
  
  def verify(self, query):
    if isinstance(query, list):
      result = set(self.terms[query[0]])
      for term in query[1:]:
        try:
          result = result.intersection(self.terms[term])
        except:
          return []
      return result
    try:
      return self.terms[query]
    except:
      return []

  def test(self, query_string):
    print("Query: " + query_string)
    query = tokenize_terms(query_string)
    a = datetime.datetime.now()
    result = self.verify(query)
    b = datetime.datetime.now()
    c = b - a
    print("Query processing time: " + str(c.total_seconds()) + "s")
    print(str(len(result)) + " match(es) out of " + str(len(self)) + " documents.\n")