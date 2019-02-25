from ntautology import make_ntautology_parser

print()
parser = make_ntautology_parser(1)
string = "(| 0 ~0)"
print("="*60)
print(string, "<==", parser(string))
print()

# from lrgrammar import LRGrammar

# G = LRGrammar()

# G.add_ternary("TF", "p")
# G.add_ternary("FT", "q")

# G.add_unary("FT","-", "TF")
# G.add_unary("TF","-", "FT")

# [ print(G.check(string)) for string in [
#   "p",
#   "q",
#   "- q"
# ] ]
