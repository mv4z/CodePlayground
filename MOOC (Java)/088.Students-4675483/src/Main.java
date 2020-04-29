
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // write here the main program
        ArrayList<Student> list = new ArrayList<Student>();
        Scanner reader = new Scanner(System.in);
        while(true){
            
            
            System.out.println("name: ");
            String name = reader.nextLine();
            if(name.isEmpty()){
                break;
            }
        
            System.out.println("studentnumber: ");
            String num = reader.nextLine();
        
            list.add(new Student(name, num));
        }    
        for(Student s: list){
            System.out.println(s);
        }
        System.out.println("Give search term: ");
        String searchTerm = reader.nextLine();
        System.out.println("Result: ");
        for(Student s : list){
            String name = s.getName();
            if(name.contains(searchTerm)){
                System.out.println(s);
            }
        }
       
    }
}
