from ntautology import make_ntautology_parser

print("="*60)
print()
n = int(input("n = "))
print()
print("[*] defining left-right grammar...")
parser = make_ntautology_parser(n)

print()
print("[*] entering REPL...")
print()

while True:
  print("="*60)
  print()
  string = input("expression: ")
  print("-"*50)
  try:
    parsed, result = parser(string)
    print(string, "<==", parsed)
    print()
    print("[$] is tautology:", result)
  except:
    print("[!] not a well-formed formula")
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
