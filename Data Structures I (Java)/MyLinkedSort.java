package algs13;

import stdlib.*;

// PROBLEM 2.2.17
// No new node created
// Allowed new linked list
public class MyLinkedSort {
    static class Node {
        public Node() { }
        public double item;
        public Node next;
    }

    int N;    Node first;
    
    
    public MyLinkedSort () {
        first = null;
        N = 0;
        checkInvariants ();
    }

    
    private void myassert (String s, boolean b) { if (!b) throw new Error ("Assertion failed: " + s); }
    private void checkInvariants() {
        myassert("Empty <==> first==null", (N == 0) == (first == null));
        Node x = first;
        for (int i = 0; i < N; i++) {
            if (x==null) {
                throw new Error ("List too short!");
            }
            x = x.next;
        }
        myassert("EndOfList == null", x == null);
    }

    public boolean isEmpty () { return first == null; }
    
    public int size () { return N; }
    
    public void add (double item) {
        Node newfirst = new Node ();
        newfirst.item = item;
        newfirst.next = first;
        first = newfirst;
        N++;
    }

    private static void print (String s, MyLinkedSort b) {
        StdOut.print (s + ": ");
        for (Node x = b.first; x != null; x = x.next)
            StdOut.print (x.item + " ");
        StdOut.println ();
    }
    private static void print (String s, MyLinkedSort b, double i) {
        StdOut.print (s + ": ");
        for (Node x = b.first; x != null; x = x.next)
            StdOut.print (x.item + " ");
        StdOut.println (": " + i);
    }

    static public MyLinkedSort sort(MyLinkedSort l ){ // 
    	// base case: list is of size 1. reurn
 	   // otherwise use split to create two lists
 	   // recursively sort each of them
 	   // use merge to combine them, and return the result
    	if (l.size() == 1) {
    		return l;
    	}
    	MyLinkedSort[] splittedNode = split(l);
    	splittedNode[0] = sort(splittedNode[0]);
        splittedNode[1] = sort(splittedNode[1]);
        return merge(splittedNode[0], splittedNode[1]);
	}

	static public MyLinkedSort[] split(MyLinkedSort l){
		 // parameter is a List
		  // it returns an array of size 2
		  // the 0th element is theleft ist
		  // the first element is the right list
        double mid = Math.floor(l.size()) / 2;
        int counter = 0;

        MyLinkedSort[] arrayList = new MyLinkedSort[2];
        arrayList[0] = new MyLinkedSort();
        arrayList[1] = new MyLinkedSort();

        Node tempNode = l.first;
        while (tempNode != null) {
            if (counter < mid){
                // Left list
                arrayList[0].add(tempNode.item);
            } else {
                // Right List
                arrayList[1].add(tempNode.item);
            }
            tempNode = tempNode.next;
            counter++;
        }
        return arrayList;
    }


	static public MyLinkedSort merge(MyLinkedSort lt, MyLinkedSort rt){

        MyLinkedSort temp = new MyLinkedSort();
        Node dummyHead = new Node();
        Node curr = dummyHead;
        Node tempNodeLeft = lt.first;
        Node tempNodeRight = rt.first;


        while ((tempNodeLeft != null) && (tempNodeRight != null)){
            if (tempNodeLeft.item <= tempNodeRight.item) {
                curr.next = tempNodeLeft;
                tempNodeLeft = tempNodeLeft.next;
            } else {
                curr.next = tempNodeRight;
                tempNodeRight = tempNodeRight.next;
            }
            curr = curr.next;
        }

        if (tempNodeLeft == null){
            curr.next = tempNodeRight;
        } else {
            curr.next = tempNodeLeft;
        }

        temp.first = dummyHead.next;

      return temp;
}

    public static void main (String args[]) {
        int[] a1 = new int[20];
		for (int i = 0; i < a1.length; i++)
			a1[i] = i;
		StdRandom.shuffle (a1);
        MyLinkedSort b1 = new MyLinkedSort ();
        for (int i:a1) b1.add(i);
        MyLinkedSort.print("before sort",b1);
        MyLinkedSort res1 = MyLinkedSort.sort(b1);
        MyLinkedSort.print("after sort",res1);

        int[] a2 = new int[200];
		for (int i = 0; i < a2.length; i++)
			a2[i] = i;
		StdRandom.shuffle (a2);
        MyLinkedSort b2 = new MyLinkedSort ();
        for (int i:a1) b2.add(i);
        MyLinkedSort.print("before sort",b2);
        MyLinkedSort res2 = MyLinkedSort.sort(b2);
        MyLinkedSort.print("after sort",res2);
         
    }
}
