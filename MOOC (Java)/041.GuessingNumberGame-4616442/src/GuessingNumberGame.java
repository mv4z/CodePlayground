
import java.util.Random;
import java.util.Scanner;

public class GuessingNumberGame {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int numberDrawn = drawNumber();

        // program your solution here. Do not touch the above lines!
        int count = 1;
        while(true){
        System.out.println("Guess a number: ");
        int guess = Integer.parseInt(reader.nextLine());
        if(guess < numberDrawn){
            System.out.println("The number is greater, guesses made: "+ count);
            count++;
        }
        else if(guess > numberDrawn){
            System.out.println("The number is lesser, guesses made: " + count);
            count++;
        }
        else if(guess == numberDrawn){
            break;
        }
        }
        System.out.println("Congratulations, your guess is correct!");
        
    }

    // DO NOT MODIFY THIS!
    private static int drawNumber() {
        return new Random().nextInt(101);
    }
}
