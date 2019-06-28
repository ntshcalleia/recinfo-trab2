import datetime, pickle, re, json
from information_retrieval import Document, SignatureIndex, InvertedIndex

if __name__ == "__main__":
  try:
    t0 = datetime.datetime.now()
    with open("WikipediaSignatureIndex.p", "rb") as pickle_file:
      signature_index = pickle.load(pickle_file)
    with open("WikipediaInvertedIndex.p", "rb") as pickle_file:
      inverted_index = pickle.load(pickle_file)
    t1 = datetime.datetime.now()
    loaded_from_file = True
  except:
    loaded_from_file = False
    t0 = datetime.datetime.now()
    signature_index = SignatureIndex()
    inverted_index = InvertedIndex()

    with open("wiki-articles-1000.json") as file:
      reviews = [json.loads(str(review)) for review in file.read().strip().split('\n')]
      for i, review in enumerate(reviews):
        r = Document(review["body"], review["url"])
        signature_index.add(r)
        inverted_index.add(r)
      t1 = datetime.datetime.now()
      pickle.dump(signature_index, open("WikipediaSignatureIndex.p", "wb"))
      pickle.dump(inverted_index, open("WikipediaInvertedIndex.p", "wb"))
  
  print("Index size: " + str(len(inverted_index)) + " documents")
  print("Index loaded with pickle? " + str(loaded_from_file))
  delta = t1 - t0
  print("Index processing time: " + str(delta.total_seconds()) + "s\n")

  while (True):
    query = input("Type your query below:\n")
    print("\nSignature Index Results:")
    signature_index.test(query)
    print("Inverted Index Results:")
    inverted_index.test(query)