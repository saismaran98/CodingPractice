package collection.framework;

import java.util.PriorityQueue;
import java.util.Queue;
import java.util.function.Consumer;

public class LearnPriorityQueue {
	//If we need to implement min heap we can use priority queue as it internally implements min heap.
	public static void main(String[] args) {
/*		PriorityQueue<String> team=new PriorityQueue<>(); //or Queue<String> team=new PriorityQueue<>() 
		team.offer("Team Lead");
		team.offer("Delivery Manager");
		team.offer("Senior Developer");
		team.offer("Junior Developer");
		System.out.println(team);*/
		
		Queue<Integer> pq=new PriorityQueue<>();
		//Queue<Integer> pq=new PriorityQueue<>(Comparator.reverseOrder()); works as max heap
		addData.accept(pq);
		System.out.println(pq);
		System.out.println(pq.peek());
		pq.poll(); //remove top element from the min heap
	}
	static Consumer<Queue<Integer>> addData=(pq)->{
		pq.offer(12);
		pq.offer(36);
		pq.offer(24);
		pq.offer(40);
	};
}
