package collection.framework;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class LearnArrayList {

	public static void main(String[] args) {
		/*
		 * Limitations of Arrays:
		 * Arrays cannot be dynamically sized 
		 * If the size of input is not knows we can use arrayList to store data
		 */
		ArrayList<String> studentName=new ArrayList<>();
		//initial size of ArrayList=10, if we enter 10 it will dynamically increase size to 
		// n + n/2 + 1
		studentName.add("studentOne");
		studentName.add("studentThree"); //.add(argOne) adds element to last by default. 
		System.out.println(studentName);
		studentName.add(1, "studentTwo"); //.add(index: 1, element: "studentTwo") to add at specific index. 
		System.out.println(studentName);

		List<Integer> list = new ArrayList();
		List<Integer> list2=new ArrayList();
		list.add(1);list.add(2);
		list2.add(3);list2.add(4);

		// ** addAll() - concatenate multiple lists., also take parameterized argument. 
		list.addAll(list2); // [1,2] + [3,4]
		System.out.println(list); //[1, 2, 3, 4]

		// **get() to get element from specific intex of arraylist i.e arr[index]
		System.out.println(list.get(1)); //2

		//removes value at index 2 time: O(n)
		System.out.println(list.remove(2)); //returns 3 as remove() returns the value it removed from the arraylist kind of like pop()
		System.out.println(list);
		//we can also remove a specific element on the array
		//removes value 2 from list. 
		System.out.println("removing 2:: "+ list.remove(Integer.valueOf(2))); //reads all element with for loop and if found element remove method is called and return true
		System.out.println(list);

		//clear() remove all element 
		//set time: O(1) as elementData[index] = element;
		list.set(1, 2);
		//comtains() time O(n) : check if element present. 

		// iterate as interface Collection<E> extends Iterable<E> {}
		//Basic Iteration with for loop
		/*		for(int i =0;i<list.size();i++){

		}
		 */	
		//Using for:each
		/*	for (Integer element:list){
			System.out.println(element);
		}*/
		
		// ** ITERATOR **
		iterator(list);
	}
	public static void iterator(List<Integer> list){
		Iterator<Integer> it=list.iterator();
		while(it.hasNext()){
			System.out.println(it.next());
		}
		it.remove();//will remove the last element like pop()
		System.out.println(list); //[1]
	}
}
//Internal Working of adding at any index
/*		public void add(int index, E element) {
// rangeCheckForAdd(index); : validate if our index is not out of array bound. 

 ensureCapacityInternal(size + 1);  // Increments modCount!!
 System.arraycopy(elementData, index, elementData, index + 1,
                  size - index);
 elementData[index] = element;
 size++;
}*/
