/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author MartinV
 */
public class BoundedCounter {
    private int value;
    private int upperLimit;

    public BoundedCounter(int upperLimit) {
        // write code here
        this.upperLimit = upperLimit;
    }

    public void next() {
        // write code here
        this.value++;
        if(value > this.upperLimit){
            this.value = 0;
        }
    }

    public String toString() {
        // write code here
        if(this.value < 10){  
            return "0" + this.value;
        }
        return "" + value;
    }
    
    public int getValue(){
        return this.value;
    }
    public void setValue(int newVal){
        if(newVal >=0 && newVal <= this.upperLimit){
            this.value = newVal;
        }
    }
    
    
        
}
    
