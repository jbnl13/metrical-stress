# metrical-stress

Experimental code at the beginning of my thesis. Meant to generate all possible candidates for a word of certain syllable length, with however many levels of stress want to be explored.

Metrical stress is commonly thought of as a grid, with each column representing a syllable and the height of that column representing how heavily that syllable is stressed. (see https://en.wikipedia.org/wiki/Metrical_phonology#Metrical_grids for more discussion and examples)

Note: any "X" on the metrical grid is considered a "grid entry"

Here a word is turned into a vector, with each element representing the height of the metrical grid at that syllable.

This program can create a set of all possible candidates (for that length and possible height), and can also create sets of candidates without clash or anti-clash. Clash occurs when any two adjacent grid entries e and f of level x (assuming x != 0) do not have an intervening entry of level x – 1. Anti-clash occurs when any two non-adjacent grid entries e and f of level x are the greatest entries in their respective columns and do not have an intervening entry on level x + 1.

(Adjacency is with respect to level. In the "Doctors use penicillin" example on Wiki, there are grid entries on level 1 for "doc", "pe", and "ci". The entries on "doc" and "pe", and "pe" and "ci" are adjacent. The entries on "doc" and "ci" are non-adjacent. This example does not contain clash or anti-clash.)
