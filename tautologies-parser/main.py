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
  string = input()
  try:
    parsed, result = parser(string)
    print("-"*50)
    print(parsed)
    print()
    print("[$] is tautology:", result)
  except:
    print("[!] not a well-formed formula")
  print()
