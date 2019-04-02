# Notes

## Items

- document sufficiently to enable others to repeat your experiments
- describe your translation task
- describe how you measure degree of success at the task
- describe your experimental design (how many of what kinds of tests)
- predict and record your results before you do the experiment
- summarize the results of your experiments
- compare your predictions and your actual results
- discuss what conclusions you draw from your experiments

## Experiments

### Experiment 1: Translation Ring

#### Translation task

Given a sequence of languages $L_0, \dots, L_n$ and a transcript in language $L_0$, called the _original transcript_. GT translates the $L_0$-transcript to $L_1$, and then translates the resulting $L_1$-transcript to $L_2$, and so on until the transcript has been translated to $L_n$. At the end, there is left a $L_n$-transcript. Then, GT translates this $L_n$-transcript back to $L_0$, and the resulting transcript is the called _processes transcript_. The differences between the original and processed transcripts are measured to rate GT's success at this task. GT's goal is to preserve the meaning of the original transcript while following grammatical rules.

#### Success measure

I rate GT's success at the task by how close the processed transcript is the the original transcript in meaning and how well-constructed the processed transcript is. I rate in the following enumerated classes:
  (S1)  impossibly-confused grammar with no meaning
  (S2)  impossibly-confused grammar with irrelevant meaning
  (S3)  highly-confused grammar with irrelevant meaning
  (S4)  highly-confused grammar with somewhat-relevant meaning
  (S5)  somewhat-confused grammar with somewhat-relevant meaning
  (S6)  somewhat-confused grammar with relevant meaning
  (S7)  slightly-confused grammar with relevant meaning
  (S8)  slightly-confused grammar with accurate meaning
  (S9)  passing grammar with accurate meaning
  (S10) passing grammar with perfect meaning
  (S11) perfect grammar with perfect meaning

I divide the success metric of the processed transcript into two measures: grammar and meaning.
**Grammar** is how properly-constructed the processed transcript is according to the rules of $L_0$.
  (G1) impossibly-confused
  (G2) highly-confused
  (G3) somewhat-confused
  (G4) slightly-confused
  (G5) passing
  (G6) perfect

**Meaning** is how close the processed transcript is to the original transcript in meaning.
  (M1) no meaning
  (M2) irrelevant
  (M3) somewhat-relevant
  (M4) relevant
  (M5) accurate
  (M6) perfect


#### Experimental design

I performed this experiment in several trials with varying original transcripts and intermediary languages. For languages, I selected from the top 10 languages (without English) by native speakers. I hypothesized that this with correlate with the amount of effort that Google has put into training translations to and from these languages, which should yield more coherent and thus easier-to-score processed texts from this task.

Languages:
1. Mandarin
2. Spanish
3. Hindi
4. Arabic
5. Portuguese
6. Bengali
7. Russian
8. Japanese
9. Punjabi
10. German

Transcripts:
1. 
2.

Moby Dick : Mandarin




#### Predictions

#### Results

#### Analysis

### Experiment 2
#### Translation task
#### Success measure
#### Experimental design
#### Predictions
#### Results
#### Analysis
