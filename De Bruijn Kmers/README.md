# **DeBruijn Graph from k-mers Problem**

**Input:** A collection of k-mers Patterns.
     
**Output:** The adjacency list of the de Bruijn graph DeBruijn(Patterns).
     

     DeBruijn(Patterns)
        dB ← graph in which every k-mer in Patterns is isolated edge between its prefix and suffix
        dB ← graph resulting from ﻿gluing all nodes in dB with identical labels
        return dB
