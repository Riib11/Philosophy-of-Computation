import model
import random
random.seed()

M = model.load_model("bible")

def word_sample(word):
  print("word: " + word)
  print("vector:")
  print(M[word])
  print("similar:")
  print(list(M.wv.most_similar(word)))

# word_sample("god")

def word_walk(word, steps=10):
  print(word, end="")
  most_similar = list(M.wv.most_similar(word))
  word = most_similar[random.randint(0,len(most_similar)-1)][0]
  if steps > 0:
    print(" ", end="")
    word_walk(word, steps-1)
  else:
    print(".")

word_walk("job", steps=10)
