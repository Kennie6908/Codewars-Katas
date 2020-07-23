//Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. 
//Count the numbers of digits d used in the writing of all the k**2. 
//Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

public class CountDig {
    
    public static int nbDig(int n, int d) {
      int count = 0;
      if (d == 0){
        count++;
      }
      
      for (int i = 1; i <= n; i++){
        int squared = i * i;
        while (squared > 0){
            if (squared % 10 == d){
              count++;
            }
          squared = squared/10;
        }
      }
      
      return count;
  }
  
}