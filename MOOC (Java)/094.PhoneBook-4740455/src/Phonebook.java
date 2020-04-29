/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author MartinV
 */
import java.util.*;
        
public class Phonebook {
    private ArrayList<Person> phoneBook;
    
    public Phonebook(){
        this.phoneBook = new ArrayList<Person>();
    }
    
    public void add(String name, String number){
        phoneBook.add(new Person(name, number));
    }
    public void printAll(){
        for(Person p : phoneBook){
            System.out.println(p);
        }
    }
    public String searchNumber(String name){
        for(Person p : phoneBook){
            if(p.getName() == name){
                return p.getNumber();
            }
            
        }
        return "number not known";
    }
    
}
