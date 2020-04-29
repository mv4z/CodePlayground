
import java.util.Scanner;

public class GradesAndPoints {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.println("Type the points [0-60]: ");
        int score = Integer.parseInt(reader.nextLine());
        
        if (score <= 29){
            System.out.println("failed");
        }
        
        else if(score <= 34){
            System.out.println("Grade: 1");
        }
        
        else if(score <= 39){
            System.out.println("Grade: 2");
        }
        
        else if(score <= 44){
            System.out.println("Grade: 3");
        }
        
        else if(score <= 49){
            System.out.println("Grade: 4");
        }
        
        else if(score <= 60){
            System.out.println("Grade: 5");
        }
    }
}
