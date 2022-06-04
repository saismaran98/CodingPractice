package collection.framework;

import java.util.LinkedList;
import java.util.Queue;

public class LearnQueue {
	public static void main(String[] args) {
		//implimenting queue as LinkedList
		Queue<String> coffeeLine=new LinkedList();
		coffeeLine.offer("Latte");
		coffeeLine.offer("Instant Coffee");
		coffeeLine.offer("Mocha");
		coffeeLine.offer("Espresso");
		System.out.println(coffeeLine);
		
		coffeeLine.poll(); //remove first order i.e Latte
		System.out.println(coffeeLine);
	}
}
