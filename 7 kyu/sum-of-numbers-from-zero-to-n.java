//We want to generate a function that computes the series starting from 0 and ending until the given number.

public class SequenceSum{

  public static String showSequence(int value){
  int sum = 0;
  String returned = "0+";
    if (value < 0){
      return value + "<0";
    }
    else if (value == 0){
      return "0=0";
    }
    else {
      for (int i = 1; i <= value; i++){
        if (i != value){
          sum += i;
          returned = returned + Integer.toString(i) + "+";
        }
        else {
          sum += i;
          returned = returned + Integer.toString(i);
        }
      }
  }
  returned = returned + " = " + sum;
  return returned;
}

}