
import java.util.Scanner;

public class Divider {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // Implement your program here. Remember to ask the input from user.
        System.out.println("Type a number: ");
        int X = Integer.parseInt(reader.nextLine());
        
        System.out.println("Type another number: ");
        int Y = Integer.parseInt(reader.nextLine());
        
        double Z = (double) X / Y;
        
        System.out.println("Division: " + X + "/" + Y + " = " + Z);
    }
}
