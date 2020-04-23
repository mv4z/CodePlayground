
import java.util.Scanner;

public class TheSumOfSetOfNumbers {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        
        int sum = 0;
        int i = 0;
        
        System.out.println("Until what? ");
        int num = Integer.parseInt(reader.nextLine());
        
        while(i <= num){
            sum += i;
            i++;
        }
        System.out.println("Sum is " + sum);
    }
}
