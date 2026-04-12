# dunce-puter

# about
A cpu with as few transistors as possible, while technically turing-complete it will be a pain to use.

# development
The development of this will probably go in some stages, slowly going from a general idea to an actual project.

Stages:
 -design of architecture of processor

 -make logic diagram (perhaps in something like Logisim Evolution)

 -make schematic for the future processor

 -design PCB for processor

 -Assemble the final design (or some other way to prove it works, this is where I'll "ship" the project as it is in a working state)

 -Develop some testing programs

# how I calculate transistor count
There are only some parts of the processor I will define as part of the processor. The main thing of note with this is that the RAM and ROM of the full computer do not count as part of the CPU, just as they would be on your home computer.
Meanwhile, things like the counter register which interact with the ROM are part of the CPU

# architecture
Firstly, this computer will use the Harvard architecture for RAM and ROM, where they are completely separate and are only connected by the CPU.

Bit Width: this processor will use a 1-bit data width, making it a 1-bit processor, to help minimize the amount of transistors used.

Opcodes and Operands: because I plan to use 5 (technically 6) different instructions, I will use 5 bits for an opcode. In the instructions, each bit of the opcode will represent one instruction to prevent the need for a multiplexer to decode the opcode. The opcode will be 8 bits wide, to allow for programs as long as 256 instructions, as well as allowing for 256 bits (32 bytes; 0.000032 MB, to show off my system's lack of ability) of RAM.

Speed: the speed of this computer is not really that relevant, it will function the same if it's at 1hz or 1ghz, but the hope is to perhaps have it be adjustable for the sake of testing and just plain being able to play with it.

Instructions and their specifications (finally the good part):

1. NOP (opcode: 00000): no operation. That's it... what else do I explain?

2. INV (opcode: 10000): inverts the bit in the accumulator.

3. LDA [adr] (opcode: 01000): sets the accumulator to the bit at the address specified by the operand. This value will be used by other instructions.

4. STR [adr] (opcode: 00100): sets the bit at the address specified by the operand to the value in the accumulator.

5. JNZ [ins] (opcode: 00010): jumps to the instruction specified by the operand if the accumulator is equal to zero. Otherwise, nothing will happen.

6. RST (opcode: 00001): resets the values in RAM as well as acc. Can be used with a JNZ instruction to fully reset the program and computer.

# construction

The final product I will make will be on a pcb, most likely using individual transistors. However, the design could be made in pretty much anything. It could be made of vacuum tubes, relays, TTL chips, or even Minecraft redstone. The pcb will be a single or double-sided pcb, depending on which is a better fit for the project (cost, size, etc.).

# optimization

This project qualifies for the "optimization" sidequest of the Flavourtown event as its explicit goal is to optimize for as few transistors needed to make a functioning, turing-complete, CPU