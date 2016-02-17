# pybench

Quick multiplication benchmark in Python

## Notice

This is not an accurate benchmark. Don't use this to determine the processing power of a computer. It can't even use more than one CPU core.

It was just a little thing that was born out of boredom. Also the code is pretty messy, so good luck with that

## Using it

* Clone it
* `python3 bench.py`
* ???

There are no requirements to install. Well, other than a Python3 interpreter.

# Scores

Scores are based on the time taken by each section. This is then averaged out,
boosted and rounded to make the numbers look less intimidating.
The formula isn't hard at all:

```
scores = 2 / (100 * ((time_multiplication * time_squares) / 2))
```

This number is then rounded off, and you get your score. The lower the score, the better.
