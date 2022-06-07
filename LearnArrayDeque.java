package collection.framework;

import java.util.ArrayDeque;
import java.util.function.Consumer;
import java.util.function.Supplier;

//Array double ended queue
public class LearnArrayDeque {
	private static Consumer<ArrayDeque<Integer>> printQueue=(queue)->{
		System.out.println("Queue:"+queue);
		System.out.println("First Element: "+queue.getFirst()); // or queue.peek()
		System.out.println("Last Element: "+queue.getLast());
		System.out.println();
	};
	private static Supplier<ArrayDeque<Integer>> doubleEndedQueue=()->{
		ArrayDeque<Integer> adq=new ArrayDeque<Integer>();
		adq.addFirst(1); 	//add element to the first of the queue
		adq.offer(22); 		//add element to the last of the queue by default.
		adq.offerLast(23);  //add element to the last of the queue
		printQueue.accept(adq); //print queue
		adq.removeFirst();
		System.out.println("After removeFirst:");
		printQueue.accept(adq);		
		return adq;
	};
	public static void main(String[] args) {
		doubleEndedQueue.get();
 		
	}
	
}
