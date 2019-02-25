import itertools as it
import lrgrammar as lrg
from symbols import SYMBOLS

VERBOSE = True
LOADING = True
def log(*msgs):
  if VERBOSE: print("  " + " ".join(msgs))

def load(percent, *msgs):
  if VERBOSE and LOADING:
    x_max = 20
    x = int(percent*x_max)
    load_str = x*"#" + (x_max-x)*" "
    print("["+load_str+"]", " ".join(msgs))
  elif VERBOSE and not LOADING:
    print("    "+" ".join(msgs))

def to_literal(assign):
  return "".join( "T" if a else "F" for a in assign )

def make_ntautology_parser(n):
  G = lrg.LRGrammar()

  # all possible assignments
  all_assignments = list(it.product([True, False], repeat=2*n))

  # the tautology assignment
  tautology_assignment = tuple(( True for i in range(2*n) ))
  tautology = to_literal(tautology_assignment)

  # make ternary rules
  for i in range(n):
    symbol = SYMBOLS["var"](i)
    assign_source = tuple(( True if j == 2*i else False for j in range(2*n) ))
    source = to_literal(assign_source)
    
    load(i/n, source, "->", symbol)
    G.add_ternary(source, symbol)

  # make negation rules
  for m in range(0, n):
    symbol = SYMBOLS["neg"]
    P = all_assignments
    P_len = len(P)
    for P_i in range(P_len):
      assign_target = P[P_i]
      target = to_literal(assign_target)
      assign_source = tuple(( not a for a in assign_target ))
      source = to_literal(assign_source)
      
      load(P_i/P_len, source, "->", symbol, target)
      G.add_unary(source, symbol, target)

  def make_binary_rules(symbol, combine):
    P = list(it.product(all_assignments, repeat=3))
    P_len = len(P)
    for P_i in range(P_len):
      assign_source, assign_target1, assign_target2 = P[P_i]
      if all([
        assign_source[i] == combine(assign_target1[i], assign_target2[i])
        for i in range(0, 2*n)
      ]):
        target1 = to_literal(assign_target1)
        target2 = to_literal(assign_target2)
        source  = to_literal(assign_source)
        load(P_i/P_len,
          source,  "->",
          SYMBOLS["ass-l"], symbol, target1, target2, SYMBOLS["ass-r"])
        G.add_binary(source, symbol, (target1, target2))

  make_binary_rules(SYMBOLS["or"]  , lambda a, b: a or b)
  make_binary_rules(SYMBOLS["and"] , lambda a, b: a and b)
  make_binary_rules(SYMBOLS["imp"] , lambda a, b: (not a) or b)

  def check(string):
    parsed = G.parse(string)
    return parsed, parsed == tautology
  return check
