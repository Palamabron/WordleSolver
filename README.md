# Wordle Solver

Program calculating the most effective current guessing word in game Wordle.

# Source for idea
Video "Solving Wordle using information theory" from 3b1b channel:

[![https://www.youtube.com/watch?v=v68zYyaEmEA](http://img.youtube.com/vi/v68zYyaEmEA/0.jpg)](http://www.youtube.com/watch?v=v68zYyaEmEA)

# How program works
First, program iterate through all possible [five-letter words](possible_words.txt) where every letter is different to evaluate number of bits (how many times on average chosen word halves total number of possible words).
It is done by generating all combinations of letters' states and assigning for each word a value based on formula below:

<p align="center">
<a href="https://en.wikipedia.org/wiki/Entropy_(information_theory)"><img src="https://latex.codecogs.com/png.image?\dpi{120}&space;\bg_white&space;H(X)&space;=&space;-\sum_{i=1}^{n}P(x_{i})\log_b&space;P(x_{i})" title="click on image to enter wikipedia page" /></a>
</p>

