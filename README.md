# CS50AI - Week 4 - Shopping

## Task:

Write an AI to predict whether online shopping customers will complete a purchase, using the Scikit-Learn k-Nearest Neighbours classifier.

```
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```

## Background:

When users are shopping online, not all will end up purchasing something. Most visitors to an online shopping website, in fact, likely don’t end up going through with a purchase during that web browsing session. It might be useful, though, for a shopping website to be able to predict whether a user intends to make a purchase or not: perhaps displaying different content to the user, like showing the user a discount offer if the website believes the user isn’t planning to complete the purchase. How could a website determine a user’s purchasing intent? That’s where machine learning will come in.

Visit [CS50AI Shopping](https://cs50.harvard.edu/ai/2023/projects/4/shopping/) for full specification.
## Usage:

Requires Python and Scikit-Learn to run, which can be done via `pip install scikit-learn`:

```$python shopping.py shopping.csv```


## Acknowledgements:

Data set provided by [Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018)](https://link.springer.com/article/10.1007/s00521-018-3523-0)