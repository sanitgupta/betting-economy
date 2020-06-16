# BettingEconomy

### Introduction

On this fictional planet, life is a series of bets. One accumulates wealth in life depending on the outcomes of the bets one makes. Some people are open to taking risks, while others are risk averse and want to play it safe. Everyone is allowed to make two kinds of bets: a high risk high reward bet and a much safer bet. Some people are born poor while others are born rich. 

We wish to see how well different groups of people do. The motivation is to answer a few questions:

* What strategy should one employ if they wish to become extremely wealthy?
* Is the strategy the same if they are not as ambitious and just want to have a reasonable amount of wealth?
* Does it make more sense to be risk-tolerant as a rich person than as a poor person?

This simulation was created using [Mesa](https://github.com/projectmesa/mesa/), a library to design Agent-Based Models in Python.

### Experimental Details

The poor people start with $100 while the rich people start with 10 times as much money i.e. $1000. The poverty line is placed at $80.

There are two bets a person can make:

* The Risky bet - Given current wealth $ x, one has a 50% chance of winning $ 3x/5 and a 50% chance of losing $ x/2.
                  Note that in this bet, in expectation one would win $ x/20.

* The Safe bet - Given current wealth $ x, one has a 80% chance of winning $ x/20 and a 20% chance of losing $ x/10.
                  Note that in this bet, in expectation one would win $ x/50.

For the sake of this simulation, every person has equal probability of being born poor or rich, risk averse or risk tolerant. There are a total of 100000 people in this population and each demographic ends up having ~25% of the total population.

A Risk-Averse person always makes the safe bet.
A Risk-Tolerant person always makes the risky bet but becomes risk-averse if they lose enough money to be left with only one-fourth of what they started with.

Every person makes a series of 20 bets. We look at the wealth accumulated by the people at the end.

### Results and Discussion

Here's a summary of the results i.e. the wealth of the people after 20 bets:

 Demographic  | Max Wealth (in $)| Mean Wealth (in $)| Median Wealth (in $) 
------------ | ------------- | ------------- | -------------
Risk-Tolerant and Rich | 3777893 | 2774 | 235
Risk-Averse and Rich | 2653 | 1482 | 1432
Risk-Tolerant and Poor |  377789 | 252 | 23
Risk-Averse and Poor | 265 | 148 | 143


If one just looked at the expected values, one would have concluded that the risky bet was the obvious choice. The results are much more complex though.

While the the risk-tolerant people have a higher mean wealth than the risk-averse people for both the rich and the poor demographics, the mean wealth might not be the right metric to look at because it gets inflated because of the few people who strike gold, in this case because of sheer luck. The median, which is considered to be a fairer metric in general because of its robustness to anomalies, paints a completely different picture. For both the rich and the poor group, the median wealth of the risk-tolerant people ends up being just one-fifth of the median welath of the risk-averse people.

There's also a huge disparity between the people born rich and poor. The fact that they started with 10 times as much money shows up in their final wealth too. Also, while median wealth for all risk-averse people is lower than the corresponding risk-tolerant people for both groups, choosing to be risk-averse can be especially devastating for the poor people as their final median wealth is not even one-third of the poverty line. A whopping ~81% of them end up below the poverty line while among the risk-tolerant ones only ~3% end up below the poverty line. These numbers are incredibly small for the people who started rich, practically none of them ends up below the poverty line.

In conclusion, the safe strategy seems to be the more sensible one. On the other hand, only with the risk-tolerant strategy does one have a shot at becoming extremely rich (which is near-impossible if one is risk-averse). This chance comes with a lot of risk though. This risk is much more acceptable for the people who started rich because if things go wrong, most of them still end up with a reasonable amount of wealth. On the other hand, a large percentage of risk-tolerant people who started poor wind up in a terrible situation.

### How to Run

If you wish to tinker with the model and run it yourself, follow the following steps:


* To clone the repository and enter its working directory:

```bash
>> git clone https://github.com/sanitgupta/BettingEconomy.git
>> cd BettingEconomy
```

* To modify the model or the parameters, make the corresponding changes to model.py.

* To run the model:

```bash
>> python model.py
```
