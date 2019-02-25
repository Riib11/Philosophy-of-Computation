import itertools as it
import lrgrammar as lrg
from symbols import SYMBOLS

VERBOSE = True
def log(*msgs):
  if VERBOSE: print("  " + " ".join(msgs))
  else: pass

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
    
    log(source, "->", symbol)
    G.add_ternary(source, symbol)

  # make negation rules
  for m in range(0, n):
    symbol = SYMBOLS["neg"]
    for assign_target in all_assignments:
      target = to_literal(assign_target)
      assign_source = tuple(( not a for a in assign_target ))
      source = to_literal(assign_source)
      
      log(source, "->", symbol, target)
      G.add_unary(source, symbol, target)

  def make_binary_rules(symbol, combine):
    for (assign_source, assign_target1, assign_target2) \
      in it.product(all_assignments, repeat=3) \
    :
      if all([
        assign_source[i] == combine(assign_target1[i], assign_target2[i])
        for i in range(0, 2*n)
      ]):
        target1 = to_literal(assign_target1)
        target2 = to_literal(assign_target2)
        source  = to_literal(assign_source)
        log(source, "->",
          SYMBOLS["ass-l"], symbol, target1, target2, SYMBOLS["ass-r"])
        G.add_binary(source, symbol, (target1, target2))

  make_binary_rules(SYMBOLS["or"], lambda a, b: a or b)
  make_binary_rules(SYMBOLS["and"], lambda a, b: a and b)

  def check(string):
    parsed = G.parse(string)
    return parsed, parsed == tautology
  return check
