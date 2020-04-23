
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        // write here code to ensure that BoundedCounter works as expected
        // before starting 78.3 remove the extra code and use the skeleton shown
        // in the assignment
        BoundedCounter seconds = new BoundedCounter(59);
        BoundedCounter minutes = new BoundedCounter(59);
        BoundedCounter hours = new BoundedCounter(23);
        
        System.out.print("seconds: ");
        int s = Integer.parseInt(reader.nextLine());
        System.out.print("minutes: ");
        int m = Integer.parseInt(reader.nextLine());
        System.out.print("hours: ");
        int h = Integer.parseInt(reader.nextLine());

        seconds.setValue(s);
        minutes.setValue(m);
        hours.setValue(h);
        
        
        int i = 0;
        while( i<121){
            System.out.println(hours + ":" + minutes + ":" + seconds);
            if(seconds.getValue() == 59){
             
            if(minutes.getValue() == 59) {
                hours.next();
                
                //if(hours.getValue() == 23 && minutes.getValue() == 59 && seconds.getValue() == 59){
                    
                    //hours.next();
               //     hours.setValue(0);
                    
                //} else {
                   // hours.next();
               // }
            }
             minutes.next();
             seconds.next();
         } else {
             seconds.next();
         }
            i++;
         
        }

    }
}
