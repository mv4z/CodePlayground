package algs24;

import stdlib.StdIn;
import stdlib.StdOut;
import java.util.NoSuchElementException;
import java.util.LinkedList;
import java.util.Queue;
import stdlib.StdOut;


/**
 *  The <tt>PtrHeap</tt> class is the priorityQ class from Question 2.4.24.
 *  It represents a priority queue of generic keys.
 *  
 *  It supports the usual <em>insert</em> and <em>delete-the-maximum</em>
 *  operations, along with methods for peeking at the maximum key,
 *  testing if the priority queue is empty, and iterating through
 *  the keys.
 *  For additional documentation, see <a href="http://algs4.cs.princeton.edu/24pq">Section 2.4</a> of
 *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 */

public class PtrHeap<K extends Comparable<? super K>> {
	
	static class Node<K> {
		K value;
		Node<K> parent;
		Node<K> lchild;
		Node<K> rchild;
		int size;
		
		public Node(K value, int size) {
			this.value = value;
			this.size = size;
		}
	}
	
	private int size;
	private Node<K> root;
	private Node<K> lastInserted;
	
    boolean isRoot(Node<K> n){ return n == root; }
    
    Node<K> find(int n){ 
    	return null; } 
	
	void exch(Node<K> n1, Node<K> n2) { 
	K temp = n1.value;
	n1.value = n2.value;
	n2.value = temp;
	}
	
	@SuppressWarnings("unchecked")
	/** Create an empty priority queue  */
	public PtrHeap() {
		root = null;
		
	}
    
	/** Is the priority queue empty? */
	public boolean isEmpty() { 
		return size == 0;}
	

	/** Return the number of items on the priority queue. */
	public int size() { 
		return size(root); }

	/**
	 * Return the largest key on the priority queue.
	 * Throw an exception if the priority queue is empty.
	 */
	public K max() {
		if(root == null) { throw new NoSuchElementException();}
		return root.value;
		
	}

	/** Add a new key to the priority queue. */
	public void insert(K x) { 
		root = insert(root, x);
		swim(lastInserted);
	}



	/**
	 * Delete and return the largest key on the priority queue.
	 * Throw an exception if the priority queue is empty.
	 */
	public K delMax() {
if(size() == 0) { throw new NoSuchElementException(); }
		
		if(size() == 1){
			K result = root.value;
			root = null;
			size--;
			return result;
		}

		exch(root, lastInserted);
		Node<K> recentPar = lastInserted.parent;
		K lastInsData = lastInserted.value;
		if(lastInserted == recentPar.lchild){
			recentPar.lchild = null;
		} else{
			recentPar.rchild = null;
		}

		Node<K> traverser = lastInserted;

		while(traverser != null){
			traverser.size--;
			traverser = traverser.parent;
		}

		lastInserted = lastReset(root);

		sink(root);
		size--;
		return lastInsData;
	}
	//HELPER METHODS

		private Node<K> lastReset(Node<K> x){
			if(x == null) return null;
			if(x.lchild == null && x.rchild == null) return x;
			if(size(x.rchild) < size(x.lchild))
				return lastReset(x.lchild);
			else 
				return lastReset(x.rchild);
		}

		private Node<K> insert(Node<K> x, K data){
			if(x == null){
				lastInserted = new Node<K>(data, 1);
				return lastInserted;
			}
			// compare left and right sizes see where to go
			int leftSize = size(x.lchild);
			int rightSize = size(x.rchild);

			if(leftSize <= rightSize){
				// go to left
				Node<K> inserted = insert(x.lchild, data);
				x.lchild = inserted;
				inserted.parent = x;
			} else{
				// go to right
				Node<K> inserted = insert(x.rchild, data);
				x.rchild = inserted;
				inserted.parent = x;
			}
			x.size = size(x.lchild) + size(x.rchild) + 1;
			size++;
			return x;
		}

		private int size(Node<K> x){
			if(x == null) 
				return 0;
			else
				return size;
		}

		public void swim(Node<K> x) {

			if(x == null) return;
			if(x.parent == null) 
			{
				root = x;
				return; 
			}
			int compare = x.value.compareTo(x.parent.value);
			if(compare > 0){
				exch(x, x.parent);
				swim(x.parent);
			}

		}

		private void sink(Node<K> x)
		{
			if(x == null) return;
			Node<K> swaap;
			if(x.lchild == null && x.rchild == null){
				return;
			}
			else if(x.lchild == null){
				swaap = x.rchild;
				int compare = x.value.compareTo(swaap.value);
				if(compare < 0)
					exch(swaap, x);
			} else if(x.rchild == null){
				swaap = x.lchild;
				int compare = x.value.compareTo(swaap.value);
				if(compare < 0)
					exch(swaap, x);
			} else{
				int compare = x.lchild.value.compareTo(x.rchild.value);
				if(compare >= 0){
					swaap = x.lchild;
				} else{
					swaap = x.rchild;
				}
				int finalComp = x.value.compareTo(swaap.value);
				if(finalComp < 0) {
					exch(swaap, x);
					sink(swaap);
				}

			}
		}

	private void showHeap() { 
	    // a method to print out the heap
		// useful for debugging
		if (root == null)
		{
			return;
		}

		Queue<Node<K>> q =new LinkedList<Node<K>>(); 
		q.add(root); 


		while(true) 
		{
			int Count = q.size(); 
			if(Count == 0) 
				break; 
			while(Count > 0) 
			{ 
				Node<K> node = q.peek(); 
				System.out.print("         " + node.value + " "); 
				q.remove(); 
				if(node.lchild != null) 
					q.add(node.lchild); 
				if(node.rchild != null) 
					q.add(node.rchild); 
				Count--; 
			} 
			System.out.println(); 
		}
		System.out.println(); 
		System.out.println(); 
		System.out.println(); 
	}

	

	public static void main(String[] args) {
		PtrHeap<String> pq = new PtrHeap<>();
		StdIn.fromString("10 20 30 40 50 - - - 05 25 35 - - - 70 80 05 - - - - ");
		while (!StdIn.isEmpty()) {
			StdOut.print ("pq:  "); pq.showHeap();
			String item = StdIn.readString();
			if (item.equals("-")) StdOut.println("max: " + pq.delMax());
			else pq.insert(item);
		}
		StdOut.println("(" + pq.size() + " left on pq)");

	}

}

