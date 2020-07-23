// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
//You can guarantee that input is non-negative.

public class BitCounting {

  public static int countBits(int n){
  int count = 0;
    String result = Integer.toBinaryString(n);
    for (int i = 0; i < result.length(); i++){
      if (result.charAt(i) == '1'){
      count++;
      }
  }
  return count;
  }
}