from pathlib import Path
from intelhex import IntelHex

#ISA definitions
instructions = {"NOP":int('00000',2),"INV":int('00001',2),"LDA":int('00010',2),"STR":int('00100',2),"JNZ":int('01000',2),"RST":int('10000',2)}

#defined functions

#cuts the raw text by line into the opcode and operand
def codeSplit(codefile):
	output = codefile.split("\n")
	for x in range(len(output)):
		output[x] = output[x].split()
	return output

#turns the text opcodes and turns them into binary form.
def replaceOpcodesBinary(separatedInstructions,isa):
	for opcode in range(len(separatedInstructions)):
		separatedInstructions[opcode][0] = isa[separatedInstructions[opcode][0]]
		if len(separatedInstructions[opcode]) == 2:
			separatedInstructions[opcode][1]=int(separatedInstructions[opcode][1])
	return separatedInstructions

#turns each instruction into just one number
def convToSingleNumInstr(incode):
	for x in range(len(incode)):
		if len(incode[x])==1:
			incode[x]='{0:04x}'.format((incode[x][0]))
		else:
			incode[x]='{0:04x}'.format((incode[x][0])+(incode[x][1]<<5))
	return incode


inputfilename = Path(input("Type in the path to the code you would like to assemble."))

if inputfilename.exists():
	inputfile = open(inputfilename,"r").read()
	print("This File exists!")
	outputName = input("What would you like to call the output file (the '.hex' extention will be added automatically)")
	print("compiling code...")
	outputCode = codeSplit(inputfile)
	outputCode = replaceOpcodesBinary(outputCode,instructions)
	outputCode = convToSingleNumInstr(outputCode)
	outputFile = open(outputName+".hex","w")
	outputCode = str(outputCode).replace("[","")
	outputCode = outputCode.replace("]","")
	outputCode = outputCode.replace(",","")
	outputCode = outputCode.replace("'","")
	outputFile.write(outputCode)
	outputFile.close()
	print("process complete! Have a great day!")
else:
	print("ERROR the path you input leads to a file that does not exist. Please run this program again.")
