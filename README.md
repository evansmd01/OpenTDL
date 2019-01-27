# OpenTDL
A Training Definition Language (TDL) - Complex Gym Training Routines in a Flexible, Machine-parsable, Shareable format.

## Why OpenTDL

Because no gym apps are flexible enough, because theres too much variability in how gym sessions are structured, no app can seem to handle all the different types of training well.

So lets tackle the complexity of finding a universal structure for defining all the crazy variance in training plans. With a flexible, machine-parsable definition, unlimited apps can be created that help with planning/creating plans, timing and prompting trainees through their workout, logging progress, and charting history. All of those problems can be tackled separately, and by various competing apps, if there is a single definition language they can all share.

## Syntax

```
program My Custom Program
  session My Day 1 Morning Session
    1 sets Foam Roller
      10 minutes
    rest 2 minutes
    3 rounds My Circuit
      1 sets Push Up
        8 reps
      rest 30 seconds
      1 sets Pull Up
        4 reps
      rest 5 minutes
  rest 8 hours
  session My Day 1 Evening Session
  rest 1 days
```


**Work in Progress, check back soon**

Check out the following parsers:
- https://github.com/evansmd01/OpenTDL-Javascript-Parser
