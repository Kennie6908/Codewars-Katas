//Complete the solution so that the function will break up camel casing, using a space between words.

class Solution {
  public static String camelCase(String input) {
    String returned = "";
  int lastcap = 0;
    for (int i = 0; i < input.length(); i++){
    if (Character.isUpperCase(input.charAt(i))){
      returned = returned + input.substring(lastcap, i) + " ";
      lastcap = i;
    }
  }
  returned = returned + input.substring(lastcap);
  return returned;

  }
}