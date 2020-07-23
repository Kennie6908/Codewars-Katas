//Simple, given a string of words, return the length of the shortest word(s).

//String will never be empty and you do not need to account for different data types.

import java.util.Arrays;
import java.util.ArrayList;

public class Kata {
    public static int findShort(String s) {
        String [] words = s.split(" ");
        int length = words[0].length();
        for (int i = 1; i < words.length; i++){
          if (words[i].length() < length){
            length = words[i].length();
          }
        }
        return length;
    }
}