# Turing Machine Structure

## Finite State Machine

TODO: Define a FSM

TODO: how parts interact

1. The `SIGNAL DETECTOR` sends the `NEXT STATE` message, part of which sends the `ROW ADDRESS` 1SSS.
2. The `TAPE`'s `OUTPUT COLLATOR` sends the `COLUMN ADDRESS` 1VVV.
3. At the `ROW ADDRESS`, a MWSS is sent eastward. At the `COLUMN ADDRESS`, LWSS is sent northward. They collide, and their collision is formatted to trigger the memory cell selected by `(ROW ADDRESSS, COLUMN ADDRESS)`.
4. The selected memory cell outputs a pattern of gliders to the northeastward.
5. The selected memory cell output is eventually filtered towards a LWSS stream pointing northward. This stream is .
7. The output negates some of the stream, transmitting the memory cell's output.


- ROW ADDRESS is received from NEXT STATE output from SIGNAL DETECTOR
- COLUMN ADDRESS is received from TAPE OUTPUT COLLATOR
- ROW ADDRESS + COLUMNS ADDRESS targets a MEMORY CELL, triggering output

- 

Parts to detail:
- ROW ADDRESS
- NEXT STATE
- SIGNAL DETECTOR
- COLUMN ADDRESS
- TAPE OUTPUT COLLATOR
- MEMORY CELL
- P240 GUN
- 1GAP8
- P30 LWSS GUN

## Tape



## Signal Detector

