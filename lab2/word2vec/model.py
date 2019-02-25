import pickle

def load_model(model_name):
  with open("data/"+model_name+".txt.model", "rb") as model_file:
    return pickle.load(model_file)
