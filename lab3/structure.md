# Turing Machine Structure

## Abstract Turing Machine

TODO: Define a FSM
TODO: Define a tape
TODO: Define a TM

## Logic in the Game of Life

### Spaceships:

- **glider**: The smallest spaceship; travels diagonally by wagging its tail.

- **LWSS**: A light-weight spaceship; travels horizontally.

- **MWSS**: A mid-weight spaceship; it travels horizontally.

#### Spaceship Guns:

- **P`X`**: Classifies a constant spaceship stream that contains a spaceship at `X`-generation intervals.

- **P`X` `S` GUN**: A gun that emits a P`X` `S` stream.

### Signals

**Stream**: a constant, repeated output of spaceships in a line.
**Signal**: a stream contains signals, which is the encoding of a stream of bits. A single signal is some section of the stream that is present over some number of generations.
  - **0** is encoded by an absent spaceship in the repetition of the stream.
  - **1** is encoded by a present spaceship in the repetition of the stream

### Signal Logic

- **AND gate**: When two signals are inputted to a **AND** gate, a resulting signal is produced that contains the **AND** of each input's encoded bit.
- **OR gate**: When two signals are inputted to an **OR** gate, a resulting signal is produced that contains the **OR** of each input's encoded bits.
- **NOT gate**: When a signal is inputted to a **NOT** gate, a resulting signal is produced that contains the **NOT** of the input's encoded bits.

- **Reflectors**: A reflector receives an input signal and then outputs a copy of that signal in some direction. The output signal may be modified in some way e.g. inverted or of a different spaceship type.

- **Eaters**: TODO

- **Inversion**: An inverted signal is the **NOT** of a signal. Composing guns, reflectors, and gates often makes use of signal inversion. For example, many reflector implementations also invert their input signal, so referring to the inverted signal's state is useful.

## A Turing Machine in the Game of Life

This description is of all the modules required to build a generic Turing Machine in the Game of Life. However, the construction differs based on how many states are needed, how many letters are in the alphabet, and how much tape space is needed for the entire run of the machine. Notably, this last requirement is undecidable for Turing machines in general.

<!-- TODO: keep this or use the pictures from the website? -->
The easiest example to first examine is a very simple 3-stated, 2-lettered Turing machine. The presented diagrams in this section will almost all be subsections of this simple example machine, to show the context of their operation within the entire machine.

However, arbitrarily complex machines can be constructed using the same method as was used to construct this toy example. For example, a Universal Turing Machine has been successfully constructed and I will exhibit it in all of its glory at the end of this paper.

### FINITE STATE MACHINE (FSM)

#### Operation

1. The SIGNAL DETECTOR sends the NEXT STATE message, part of which sends the ROW ADDRESS 1SSS.

2. The TAPE's OUTPUT COLLATOR sends the COLUMN ADDRESS 1VVV.

3. At the ROW ADDRESS, a MWSS is sent eastward. At the COLUMN ADDRESS, LWSS is sent northward. They collide, and their collision is formatted to trigger the memory cell selected by (ROW ADDRESSS, COLUMN ADDRESS).

4. The selected memory cell outputs a pattern of gliders to the northeastward.

5. A P30 MWSS GUN firing eastward is intercepted by the memory cell's output. The resulting MWSS stream heading eastward is the inverse of the memory cell's output.

6. The inverted memory cell output stream is intercepted by a northward MWSS stream, which inverts to yield the original memory cell output in the northward stream.

7. This final output stream is collected by the SIGNAL DETECTOR.

#### Components

- **ROW ADDRESS**
- **NEXT STATE**
- **COLUMN ADDRESS**
- **MEMORY CELL**

### TAPE

The TAPE is implemented as two stacks. In this way the finite state machine changes the position of the FSM's TAPE's read head by scrolling the TAPE's information left and right. The side of each stack closest to the TAPE's read head is called the CONTROL END.

There is no TAPE directly under the Read Head. A symbol extracted from the TAPE  into the FSM to be used as a state address during the Pop of one Cycle and then a symbol is inserted into the TAPE during the Push of the next Cycle.



#### Operation

1. The output from the SIGNAL DETECTOR is copied once.

2. One output copy is sent to each STACK's CONTROL CONVERSION.

3. One of the STACK's OUTGATE is sent to the OUTPUT COLATOR.

4. The OUTPUT COLATOR sends this information to the FSM

#### Components

- **STACK**: Is composed of some number of STACK CELLs in sequence. There are two cycles for updating the TAPE: PUSH and POP. Control signals are passed up each side of the STACK. At each cell, a FANOUT copies the signal - one signal is inputted to the cell and the other is forwarded further along the STACK. The signal inputted into the cell is used to contain any VALUE that is contained in the cell, creating a sort of cell wall. The PUSH CONTROL and POP CONTROL interfere with this signal, nullifying 4 bits in this cell wall, allowing the VALUE GLIDER to be transfered from to an adjacent cell.
  - **PUSH**: All VALUE GLIDERs in the STACK are moved one cell away from the CONTROL END, freeing up a cell at the CONTROL END.
  - **POP**: The VALUE GLIDER at the CONTROL END is removed and all VALUE GLIDERs in the STACK are moved one cell towards the CONTROL END, filling up the empty cell left by the removal.

- **VALUE GLIDER**: Each stack cell has an interior that is capable of holding a VALUE GLIDER. The cell's walls, streams of gliders, reflect the VALUE GLIDER back and forth so that it is contained inside the stack cell. When one of the cell's walls is disrupted (a gap created by the PUSH CONTROL or POP CONTROL), the VALUE GLIDER is allowed to move in one direction along the TAPE into another stack cell. The only case when the VALUE GLIDER would exit the TAPE (the TAPE is finite) is when it is being popped (as part of POP) or when it goes off the non-CONTROL END, in which case it is released into the ether to be forgotten (include a larger tape if you need more space).

- **OUTGATE**: A P120 GLIDER GUN tests for a 4-glider gap in the STACK's control stream, which is put there by POP CONTROL. On the occurrence of such a gap, the output of the gun gets through and triggers a 1GAP4 gate that samples for the 4 bits in an inverted copy of the cell wall. The gun additionally expands the gap by 1 bit, and includes this n the output of the OUTGATE. The output is of the form 1VVV - an address for the FSM.

- **OUTPUT COLATOR**: Inverts each STACK OUTGATE output and feeds it to the COLUMN ADDRESS of the FSM.

- **POP CONTROL**: Is a signal with a single glider (indicating that a POP should be initiated). It is sent along the TAPE and creates a gap in the control-side cell wall of each cell, allowing the contained VALUE GLIDERS to translate one cell towards the CONTROL END of the TAPE. At the CONTROL END of the tape, the bit in the CONTROL CELL is released and tested by the INGATE, which indicates if the CONTROL CELL's value was a 0 or 1.

- **PUSH CONTROL**: Is a signal with a single glider (indicating that a PUSH should be initiated). It is sent along the TAPE and creates a gap in the control-opposite-side cell wall of each cell, allowing the contained VALUE GLIDERS to translate one cell away from the CONTROL END of the TAPE. This leaves empty the CONTROL CELL.

- **CONTROL CELL**: The stack cell furthest to the control end (right next to the STACK read head section).


### SIGNAL DETECTOR

The SIGNAL DETECTOR joins the FSM to the TAPE.
- Detects output from the FSM and generates the input for the CONTROL CONVERSION. 
- Sends NEXT STATE from OUTPUT COLLATOR to FSM

#### Operation

1. Receives an input glider signal. The signal has two 1s on its ends, with some number of 0s between them. In gliders, this looks like two gliders that are some variable distance apart (the distance is divisible by the time-set of and within a certain specific to the SIGNAL DETECTOR).

2. Inverts the signal and uses a FANOUT to split it into two signals heading in opposite directions.

3. Each inverted copy of the signal interacts with some gates and reflectors to un-invert in the form of two output signals. The two output signals differ depending on the input signal.

4. One output is sent to the CONTROL CONVERSION

5. The other output is combined with a copy of the original input to convert the DVVVSSSS signal to DVV1SSSS so that 1SSS can be used to address the FSM. This output is sent to NEXT STATE DELAY.

#### Components

- **SET RESET LATCH (B)**: Receives glider input signals from two sources: on and off. When a signal is received from the on-input and the LATCH is in state OFF, the LATCH begins emitting a stream of constant 1s. When a signal is received from the off-input and LATCH is in state ON, the LATCH stops emitting a stream of 1s (i.e. begins emitting a stream of 0s instead).

- **FANOUT**: Receives a glider input signal from one source. After receiving a signal, FANOUT emits two glider signals perpendicular to the input signal. FANOUT has a tunable leg to adjust the input step-time.

- **CONTROL CONVERSION**:
  Each STACK has a different implementation of this; one performs a PUSH and the other performs a POP. Receives two input from SIGNAL DETECTOR: One input is a glider stream with 9 gliders with the form DVVVSSSS where D is the direction for POP/PUSH, VVV is the symbol to POP/PUSH and SSSS is the NEXT STATE for the FSM. The other input is is a glider indicating that a signal has been received.

  A P240 GLIDER GUN receives a NOT D glider from the inverted DVVVSSSS signal to produce an output but only when D is nonzero. This is passed on to a FANOUT, which outputs two copies of the signal - one two the PUSH/POP CONTROL of the STACK and the other (a single glider) towards the other input from the SIGNAL DETECTOR to delete it. This SIGNAL DETECTOR is either for the PUSH CONTROL or POP CONTROL of the STACK.

- **NEXT STATE DELAY**: A long loop that delays the NEXT STATE signal so that the address signal to is received by the FSM in parallel with the TAPE's output. The TAPE's output is originally DVV1SSSS, but along its way to the FSM, it is modified by a 1GAP3 powered by a P240 GLIDER GUN which removes the DVV from the signal, leaving 1SSSS for input into the ROW ADDRESS.

## Miscellaneous Components

- **1GAPX**: The collision of a glider with a P30 glider stream that leaves a mass that blocks altogether X gliders before disappearing. This process yields a X-glider gap in the stream.

- **PENTADECATHLON**: An oscillator of period 15. It can be used to reflect 90-degree reflect gliders from several different angles.
