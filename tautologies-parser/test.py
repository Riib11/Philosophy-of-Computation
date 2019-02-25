from ntautology import make_ntautology_parser

print()
parser = make_ntautology_parser(2)
string = "(| 1 ~1)"
print("="*60)
parsed, result = parser(string)
print("-"*50)
print(parsed)

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
