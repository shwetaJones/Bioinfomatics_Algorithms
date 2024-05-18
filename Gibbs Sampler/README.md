# Gibbs Sampler

Input: Integers k, t, and N, followed by a collection of strings Dna.
Output: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts. Remember to use pseudocounts!


  GibbsSampler(Dna, k, t, N)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    BestMotifs ← Motifs
    for j ← 1 to N
      i ← Random(t)
      Profile ← profile matrix constructed from all strings in Motifs except for Motifi
      Motifi ← Profile-randomly generated k-mer in the i-th sequence
      if Score(Motifs) < Score(BestMotifs)
        BestMotifs ← Motifs
    return BestMotifs
