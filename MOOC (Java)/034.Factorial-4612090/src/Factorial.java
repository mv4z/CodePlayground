import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Type a number: ");
        int number = Integer.parseInt(reader.nextLine());
        
        int prod = 1;
        int i = 1;
         while(i <= number){
             prod *= i;
             i++;
    }
        System.out.println("Factorial is: " + prod);

    }
}
