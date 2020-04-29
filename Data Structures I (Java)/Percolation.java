package algs15.perc;

import stdlib.*;
import algs15.*;

// Uncomment the import statements above.

// You can test this using InteractivePercolationVisualizer and PercolationVisualizer
// All methods should make at most a constant number of calls to the UF data structure,
// except percolates(), which may make up to N calls to the UF data structure.
public class Percolation {
	int N;
	boolean[] open;
	private UF uf;
	
	
	public Percolation(int N) {
		this.N = N;
		this.open = new boolean[N*N];
		this.uf = new WeightedUF(N*N + 2);
		
		for(int i = 0; i < N*N; i++) {
			this.open[i] = false;
		}
	}
	// open site (row i, column j) if it is not already
	public void open(int i, int j) {
		int position = (i * N) + j;
		open[i*N+j] = true;
		if (!isOpen(i, j)) {
		       open[position] = true;
		}
		
		if (i > 0) { 
	         if (isOpen(i-1, j)) {
	           uf.union(position + 1, position-N + 1);
	         }
		}
		
		else { 
	        uf.union(0, position + 1);
	       }
		
		if (i < N-1) { 
	         if (isOpen(i+1, j)) {
	           uf.union(position + 1, position+N + 1);
	         }
	       }
		
		else { 
	        uf.union(N*N+1, position+1);
	       }
		
		if (j > 0 && isOpen(i, j-1)) { 
	         uf.union(position + 1, position-1 + 1);
	       }
	       
	       if (j < N-1 && isOpen(i, j+1)) { 
	         uf.union(position + 1, position+1 + 1);
	       }

		
	}
	// is site (row i, column j) open?
	public boolean isOpen(int i, int j) {
		return open[i*N+j];
	}
	// is site (row i, column j) full?
	public boolean isFull(int i, int j) {
		// TODO
		return !open[i*N+j];
	}
	// does the system percolate?
	public boolean percolates() {
		// TODO
		return uf.connected(0,N*N+1);
	}
}