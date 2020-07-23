/* 
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
*/

public class isogram {
    public static boolean  isIsogram(String str) {
        if (str.length() == 0){
          return true;
        }
        else {
          for (int i = 0; i < str.length(); i++){
            for (int k = i + 1; k < str.length(); k++){
                if (Character.toLowerCase(str.charAt(i)) == Character.toLowerCase(str.charAt(k))){
                  return false;
              }
          }   
        }
    }
    return true;
  }
}