# OpenTDL
A Training Definition Language (TDL) - Complex Gym Training Routines in a Flexible, Machine-parsable, Shareable format.

## Why OpenTDL

Because no gym apps are flexible enough, because theres too much variability in how gym sessions are structured, no app can seem to handle all the different types of training well.

So lets tackle the complexity of finding a universal structure for defining all the crazy variance in training plans. With a flexible, machine-parsable definition, unlimited apps can be created that help with planning/creating plans, timing and prompting trainees through their workout, logging progress, and charting history. All of those problems can be tackled separately, and by various competing apps, if there is a single definition language they can all share.

## Syntax

```

exercise Open crimp
  notes: keep shoulders engaged
  videoUrl: http://youtube.com/some-instructional-video

exercise Sloper

rotation Dead Hangs
  Open crimp
  Sloper
  exercise Pinch

exercise Push Up
exercise Ring Dips

rotation Push
  Push Up
  Ring Dips

exercise Pull Up
exercise Db Rows

rotation Pull
  Pull Up
  Db Rows

program My program
  2 cycles
    session Strength Training
      3 rounds
        1 sets rotating Push each cycle
          8 reps
            increasing 1 each cycle
            decreasing 3 every 4 cycles
        rest 30 seconds
        1 sets rotating Pull each cycle
          4 reps
            increasing 1 each cycle
            decreasing 3 every 4 cycles
        rest 60 seconds
      3 sets Planks
        perform 30 seconds
        rest 1 minutes
    session Climbing
    session Hangboarding
      1 sets Shoulder Circles
        perform 1 minutes
        rest 1 minutes
      3 rounds
        3 sets rotating Dead Hangs each set
          6 reps
            perform 6 seconds
              increasing 1 each cycle
            rest 3 seconds
              increasing 1 each round
          rest 2 minutes
        rest 5 minutes
    session Biking
```


**Work in Progress, check back soon**

Check out the following parsers:
- https://github.com/evansmd01/OpenTDL-Javascript-Parser
