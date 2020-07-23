/* 
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.
*/

public class DRoot {
  public static int digital_root(int n) {
    while (n >= 10){
      n = sumofDigits(n);
    }
    return n;
  }
  
  
  public static int sumofDigits(int n){
    int sum = 0;
    while (n != 0){
    int a = n % 10;
    sum += a;
    n = n / 10;
    }
    return sum;
  }
  
  
  
}