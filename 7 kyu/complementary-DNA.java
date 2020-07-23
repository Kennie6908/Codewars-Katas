/* 
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
*/ 

public class DnaStrand {
  public static String makeComplement(String dna) {
    String result = "";
    for (int i = 0; i < dna.length(); i++){
      if (dna.charAt(i) == 'A'){
        result = result + "T";
      }
      else if (dna.charAt(i) == 'T'){
       result = result + "A";
       }
       else if (dna.charAt(i) == 'C'){
       result = result + "G";
       }
       else {
       result = result + 'C';
       }
  }
  return result;
  }
}