import java.util.Scanner;

public class TheEndPart {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Type a word: ");
        String word = reader.nextLine();
        System.out.println("Length of the word end part: ");
        int length = Integer.parseInt(reader.nextLine());
        
        int spliceLen = word.length() - length;
        
        System.out.println("Result: " + word.substring(spliceLen));
    }
}
