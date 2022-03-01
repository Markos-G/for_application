World-Cup

In soccer’s World Cup, the knockout round consists of 16 teams. In each round, each team plays another team and the losing teams are eliminated. When only two teams remain, the winner of the final match is the champion.

In soccer, teams are given FIFA Ratings, which are numerical values representing each team’s relative skill level. Higher FIFA ratings indicate better previous game results, and given two teams’ FIFA ratings, it’s possible to estimate the probability that either team wins a game based on their current ratings. The FIFA Ratings from two previous World Cups are available as the May 2018 Men’s FIFA Ratings and March 2019 Women’s FIFA Ratings.
Using this information, we can simulate the entire tournament by repeatedly simulating rounds until we’re left with just one team. And if we want to estimate how likely it is that any given team wins the tournament, we might simulate the tournament many times and count how many times each team wins a simulated tournament.

We implement a function that accept as input a list of teams and repeatedly simulate rounds until we’re left with one team. We also keep track and sort the teams in descending order of how many times they won simulations and the estimated probability that each team wins the World Cup.
We run tournament simulations, and keep track of how many times each team wins.
