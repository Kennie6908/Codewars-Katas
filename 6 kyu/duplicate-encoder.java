//The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" 
//if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.


public class DuplicateEncoder {
  static String encode(String word){
    String returned = ""; 
    boolean added = false;
    for (int i = 0; i < word.length(); i++){
      for (int k = 0; k < word.length(); k++){
        if (i != k && Character.toLowerCase(word.charAt(i)) == Character.toLowerCase(word.charAt(k)) && added == false){
          returned = returned + ")";
          added = true;
        }
      }
      
      if (added == false){
        returned = returned + "("; 
      }
      added = false; 
    }
  return returned; 
  }
}