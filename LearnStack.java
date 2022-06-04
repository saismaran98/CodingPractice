package collection.framework;

import java.util.Collection;
import java.util.Stack;
import java.util.function.Consumer;

public class LearnStack {
	
	public static void main(String[] args) {
		Stack<String> bookShelf=new Stack<>();
		//<LIFO> add()
		bookShelf.push("CrackingTheCodingInterview");
		bookShelf.push("Great Expectations");
		bookShelf.push("Algorithms");
		bookShelf.add("Java for Dummies");
		printStack.accept(bookShelf);
		//remove element from top of list <LIFO>
		bookShelf.pop();	//removed last element i.e [Java for dummies]
		//remove specific element from stack, its implementation is same as collection remove i.e O(n)
		//If(found_book)remove object(book) with O(n)
		bookShelf.remove("Great Expectations"); //removed book Great Expectations, also not ideally a feature of stack but since its a part of collection framework you can use this. 
		printStack.accept(bookShelf);
		
		//peek()which element is at the top of stack i.e last element.
		System.out.println(bookShelf.peek());
		
	}
	//printStack
	public static Consumer<Stack<String>> printStack=(stack)->{System.out.println(stack);};
}
