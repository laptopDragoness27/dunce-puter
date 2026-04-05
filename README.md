# dunce-puter

# about
A cpu with as few transistors as possible, while technically turing-complete it will be a pain to use.

# development
The development of this will probably go in some stages, slowly going from a general idea to an actual project.

Stages:
 -design of architecture of processor
 -make logic diagram (perhaps in something like Logisim Evolution)
 -design PCB for processor
 -Assemble the final design
 -Develop some testing programs

# how I calculate transistor count
There are only some parts of the processor I will define as part of the processor. The main thing of note with this is that the RAM and ROM of the full computer do not count as part of the CPU, just as they would be on your home computer.
Meanwhile, things like the counter register which interact with the ROM are part of the CPU