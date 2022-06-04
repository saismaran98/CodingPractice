package collection.framework;

import java.util.LinkedList;

public class LearnLinkList {
	/*
	 * offer():return boolean vs add():throw exception, poll vs remove(), peek() vs element()
	 */
	public static void main(String[] args) {
		LinkedList<String> dirStructure=new LinkedList<>();
		
		//offer() = add() but add will throw exception upon invalid operation but offer wont and just return a bolean
		//dirStructure.addFirst("etc");
		
		dirStructure.offerFirst("etc");
		dirStructure.offer("run");
		
		dirStructure.offer("userDir01");
		dirStructure.pollLast();
		dirStructure.poll(); //remove first element of the list. 
		System.out.println(dirStructure);
	}
}
