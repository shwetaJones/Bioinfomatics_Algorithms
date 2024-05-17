# **Pattern Count**

**Input:** Strings Text and Pattern.
     
**Output:** Count(Text, Pattern).
     

     PatternCount(Text, Pattern)
       count ← 0
       for i ← 0 to |Text| − |Pattern|
         if Text(i, |Pattern|) = Pattern
           count ← count + 1
       return count
