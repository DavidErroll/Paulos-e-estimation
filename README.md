# Paulos-e-estimation

This version moves main() into its own function, which is called by main().

***

Paulos tweeted a method of estimating e that reminded me of our 
discussion regarding expected wait time and the interval [0 - 1]:

Select a random number between 0 and 1.
Select another random number in the same interval and add it to the first.
Repeat this process until the sum exceeds 1.
The average number of picks will converge to e.

The process does appear to converge toward e.
However, it does so either slowly or with wide enough dispersion around the 
expected value that differences in sample sizes that I would have
thought would offer significant improvement in the estimate
commonly return worse estimates than smaller samples.

For example, my script was originally written to show estimates for
sample sizes from 10 million to 100 million incremented by 10 million.
But the estimates at the 100 million sample size were generally not the best,
with estimates in the 20 to 40 million size range performing best on occasion. 
