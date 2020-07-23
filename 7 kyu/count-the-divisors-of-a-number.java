//Count the number of divisors of a positive integer n.

public class FindDivisor {

  public long numberOfDivisors(int n) {
    // TODO please write your code below this comment
  int count = 0;
    for (int i = 1; i <= n; i++){
    if (n % i == 0){
      count++;
    }
  }
  return count;
  }

}