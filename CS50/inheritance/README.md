### Inheritance

A person’s blood type is determined by two alleles (i.e., different forms of a gene). The three possible alleles are A, B, and O, of which each person has two (possibly the same, possibly different). Each of a child’s parents randomly passes one of their two blood type alleles to their child. The possible blood type combinations, then, are: OO, OA, OB, AO, AA, AB, BO, BA, and BB.

We use structs types called person. Each person has an array of two parents, each of which is a pointer to another person struct. Each person also has an array of two alleles, each of which is a char (either 'A', 'B', or 'O').
We create a family of a specified generation size and assigns blood type alleles to each family member. The oldest generation will have alleles assigned randomly to them and younger generations inherit one allele (chosen at random) from each parent.

We use recursive functions to generate the people and for allocating and freeing memory.
