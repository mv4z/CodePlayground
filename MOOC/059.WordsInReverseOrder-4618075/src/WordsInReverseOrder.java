import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class WordsInReverseOrder {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        // create here an ArrayList
        ArrayList<String> words = new ArrayList<String>();
        while(true){
            System.out.print("Type a word: ");
            String word = reader.nextLine();
            
            if(word.isEmpty()){
                Collections.reverse(words);
                for(String i : words){
                    System.out.println(i);
                }
                break;
            }
            words.add(word);
            
        }
    }
}
