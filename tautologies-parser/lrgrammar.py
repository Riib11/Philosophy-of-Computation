from symbols import SYMBOLS

def check_WWF(condition, message):
  if not condition:
    print("[!]", message)
    raise Exception("not a valid WWF")

def extract(xs):
  x = xs[0]
  return x, xs[1:]

def add_dict_list(dict, key, value):
  if not key in dict: dict[key] = []
  dict[key].append(value)

class LRGrammar:
  def __init__(self):
    self.binaries  = {}
    self.unaries   = {}
    self.ternaries = {}

  # e.g. TT -> (TT + TT)
  #      TT -> (TT * TT)
  def add_binary(self, source, symbol, target):
    self.binaries[(symbol, target)] = source

  # e.g. TT -> - FF
  #      FF -> ~ TT
  def add_unary(self, source, symbol, target):
    self.unaries[(symbol, target)] = source

  # e.g. TF -> p
  def add_ternary(self, source, symbol):
    self.ternaries[symbol] = source

  def parse(self, string):
    unary_symbols = [ x[0] for x in self.unaries.keys() ]

    def rec(xs):

      # binary
      if xs[0] == SYMBOLS["ass-l"]:
        _, xs = extract(xs)           # extract '('
        check_WWF(len(xs) >= 3, "not enough arguments to binary")
        symbol, xs  = extract(xs)     # extract rule symbol
        parsed1, xs = rec(xs)         # parse first argument
        parsed2, xs = rec(xs)         # parse second argument
        check_WWF(xs[0] == SYMBOLS["ass-r"],
          "missing closing '"+SYMBOLS["ass-r"]+"'")
        _, xs = extract(xs)           # extract ')'
        
        # pattern match with rule source
        if (symbol, (parsed1, parsed2)) in self.binaries:
          return self.binaries[(symbol, (parsed1, parsed2))], xs
        else:
          check_WWF(False,"no binary pattern found for '"
            +symbol+" "+parsed1+" "+parsed2+"'")

      # unary
      elif xs[0] in unary_symbols:
        check_WWF(len(xs) >= 2, "not enough arguments to unary")
        symbol, xs = extract(xs)      # extract rule symbol
        parsed, xs = rec(xs)          # parse argument
        
        # pattern match with rule source
        if (symbol, parsed) in self.unaries:
          return self.unaries[(symbol, parsed)], xs
        else:
          check_WWF(False, "no unary pattern found for '"
            +symbol+" "+parsed+"'")

      # ternary
      else:
        check_WWF(len(xs) >= 1, "unexpected end of string")
        symbol, xs = extract(xs)
        
        # pattern match with rule source
        if symbol in self.ternaries:
          return self.ternaries[symbol], xs
        else:
          check_WWF(False, "no ternary found for '"+symbol+"'")

    xs = self.lex(string)
    parsed, xs = rec(xs)
    check_WWF(len(xs) == 0, "unexpected rest of string")
    return parsed

  def lex(self, string):
    xs = []
    s = ""

    for c in string:

      if c == " ":
        if s != "":
          xs.append(s)
          s = ""

      elif c in SYMBOLS.values():
        if s != "":
          xs.append(s)
          s = ""
        xs.append(c)

      else:
        s += c

    if s != "":
      xs.append(s)
      s = ""

    return xs
