//Trolls are attacking your comment section!

//A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

//Your task is to write a function that takes a string and return a new string with all vowels removed.

//For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

public class Troll {
    public static String disemvowel(String str) {
       String returned = ""; 
       for (int i = 0; i < str.length(); i++){
         char a = Character.toLowerCase(str.charAt(i));
         switch(a){
           case 'a': case 'e': case 'i': case 'o': case 'u':
             break;
           default: 
             returned = returned + str.charAt(i);
             break;
         }
      }
      return returned; 
    }
}