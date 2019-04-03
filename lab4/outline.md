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

### Transcript Setup

I selected transcript sections that reflect a variety of writing styles.

Transcripts:
T1. The Bible, Genesis
T2. Bedau's patentsample.txt
T3. Shakespeare's Henry IV, Part 1
T4. Melville's Moby Dick, Chapter 1
T5. Mariam-Webster English Dictionary, definition of Abdicate

### Translation Success Measure

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

### Translation task

Given a sequence of languages $L_0, \dots, L_n$ and a transcript in language $L_0$, called the _original transcript_. GT translates the $L_0$-transcript to $L_1$, and then translates the resulting $L_1$-transcript to $L_2$, and so on until the transcript has been translated to $L_n$. At the end, there is left a $L_n$-transcript. Then, GT translates this $L_n$-transcript back to $L_0$, and the resulting transcript is the called _processes transcript_. The differences between the original and processed transcripts are measured to rate GT's success at this task. GT's goal is to preserve the meaning of the original transcript while following grammatical rules.

### Experiment 1: Well-Documented Language Translation Ring

#### Language Setup

I selected from the top 10 languages (without English) by native speakers. I hypothesized that this would correlate with the amount of effort that Google has put into training translations to and from these languages, which should yield more coherent and thus easier-to-score processed texts from this task.

Languages:
L1. Chinese (simplified)
L2. Spanish
L3. Hindi
L4. Arabic
L5. Portuguese
L6. Bengali
L7. Russian
L8. Japanese
L9. Punjabi
L10. German

#### Experimental design

I ran each transcript through the following trials, where the selected languages and their order was chose randomly:

Trial 1: Chinese -> Hindi -> Japanese -> Punjabi -> Bengali -> German -> Spanish -> Russian -> Portuguese -> Arabic
Trial 2: German -> Spanish -> Portuguese -> Russian -> Hindi -> Chinese -> Punjabi -> Bengali -> Arabic -> Japanese
Trial 3: Punjabi -> Hindi -> German -> Portuguese -> Arabic -> Japanese -> Chinese -> Russian -> Spanish -> Bengali
Trial 4: Bengali -> Japanese -> German -> Hindi -> Russian -> Chinese -> Punjabi -> Spanish -> Portuguese -> Arabic
Trial 5: Russian -> Punjabi -> Hindi -> Arabic -> Spanish -> Japanese -> Chinese -> Portuguese -> German -> Bengali

#### Predictions

#### Results

#### Analysis

### Experiment 2: Under-Documented Language Translation Ring

### Language Setup

I selected from the bottom 5 languages by native speakers that Google Translate supports.

Languages:
L1. 
L2. 
L3. 
L4. 
L5. 

#### Success measure

#### Experimental design

#### Predictions

#### Results

#### Analysis
