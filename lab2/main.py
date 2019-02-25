################################################################################
################################################################################
# CONSTANTS

VERSION = 0.00

################################################################################
################################################################################
# CHATBOT

def process_input(in_string):
	if "hello" in in_string: return (True, "hi there!")

	return (True, "")

################################################################################
################################################################################
# COMMANDS

def handle_command(command):
	case = lambda patterns: command in patterns

	if case(["quit", "q"]): return ("exit",)
	if case(["version", "v"]): return ("log", "version: " + str(VERSION))

	else: return ("error", "unrecognized command: " + command)

################################################################################
################################################################################
# LOOP

def loop():
	state = ("error", "no input")
	in_string = input("user> ")

	# handle command
	if in_string.startswith("/"):
		state = handle_command(in_string[1:])
	# handle normal input
	else:
		success, reply = process_input(in_string)
		if success:
			print("bot>", reply)
			print()
			state = ("success",)
		else:
			state = ("error", "error in processing input")

	if state[0] == "error":
		print("[!]" + str(state[1]))
		print()
		return True

	if state[0] == "log":
		print("[*] " + str(state[1]))
		print()
		return True

	if state[0] == "success":
		return True

	if state[0] == "exit":
		return False

def main():
	print("====BotChat-V"+str(VERSION)+"====================")
	print()
	while loop(): pass
	print()
	print("=====================================")

main()
