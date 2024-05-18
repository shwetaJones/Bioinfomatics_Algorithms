Implement RandomizedMotifSearch
     Input: Integers k and t, followed by a collection of strings Dna.
     Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!

   RandomizedMotifSearch(Dna, k, t)
       randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
       BestMotifs ← Motifs
       while forever
           Profile ← Profile(Motifs)
           Motifs ← Motifs(Profile, Dna)
           if Score(Motifs) < Score(BestMotifs)
               BestMotifs ← Motifs
           else
               return BestMotifs