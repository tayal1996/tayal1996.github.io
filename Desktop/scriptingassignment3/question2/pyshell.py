import os
import re
import fileinput
import difflib
def printpath():
	prwd=os.getcwd()
	print("PythonShell:~"+prwd[11:]+"$ ", end="")
	

def main():
	print("\033c", end="")
	
	while(1):
		printpath()
		command=input()
		cword=command.split(" ")

		if(cword[0]=="cd"):
			try:
				os.chdir(cword[1])
			except IOError:
				print("Invalid path")

		elif(cword[0]=="ls"):
			prwd=os.getcwd()
			dirEle = os.listdir(prwd)
			for filename in dirEle:
				print(filename)

		elif(cword[0]=="pwd"):
			print(os.getcwd())

		elif(cword[0]=="touch"):
			open(cword[1],"x")

		elif(cword[0]=="clear"):
			print("\033c", end="")

		elif(cword[0]=="exit"):
			exit(0)

		elif(cword[0]=="grep"):
			regex = cword[1]
			regex = regex[1:-1]
			if os.path.exists(cword[2]):
				with open(cword[2]) as file:
					for line in file:
						found = re.findall(regex,line)
						if(found):
							print(line, end=" ")
			else:
				print("No such file exists")

		elif(cword[0]=="head"):
			if os.path.exists(cword[1]):
				count = 10
				with open(cword[1]) as file:
					for line in file:
						if(count):
							print(line, end=" ")
							count -= 1
					print()
			else:
				print("No such file exists")

		elif(cword[0]=="tail"):
			if os.path.exists(cword[1]):
				count = 0
				with open(cword[1]) as file:
					for line in file:
						count += 1
				now = 0
				with open(cword[1]) as file:
					for line in file:
						if(count-now <= 10):
							print(line, end=" ")
						now += 1
					print()
			else:
				print("No such file exists")

		elif(cword[0]=="tr"):
			regex1 = cword[1]
			regex1 = regex1[1:-1]
			regex2 = cword[2]
			regex2 = regex2[1:-1]
			if os.path.exists(cword[3]):
				with open(cword[3]) as file:
					for line in file:
						found = re.findall(regex1,line)
						for word in found:
							print(line.translate(line.maketrans(regex1, regex2)), end=" ")
			else:
				print("No such file exists")

		elif(cword[0]=="sed"):
			if os.path.exists(cword[3]):
				for line in fileinput.input(cword[3]):
					print(line.replace(cword[1],cword[2]), end=" ")
			else:
				print("No such file exists")

		elif(cword[0]=="diff"):
			if os.path.exists(cword[1]) and os.path.exists(cword[2]):
				with open(cword[1]) as f1:
					var1=f1.readlines()
				with open(cword[2]) as f2:
					var2=f2.readlines()
				for line in difflib.unified_diff(var1,var2):
					print(line)
			else:
				print("No such file exists")

		else:
			print("Invalid command")

if __name__ == "__main__":
	main()
