package collection.framework;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Consumer;

public class LearnHashSet {
	/*
	 * The Primary objective of set is members/elements does not store duplicates. 
	 */
	public static void main(String[] args) {
		//Class HashSet Implements<E> Set Interface
		Set<Integer> uniqueInt=new HashSet<Integer>();
		addElements.accept(uniqueInt); //uniqueInt.add() to add element and uniqueInt.remove() to remove/pop 
		//removeIf()
		uniqueInt.removeIf((value)->{return value==25;}); //predicate if(value)==25 remove 25
		System.out.println("HashSet:: "+uniqueInt); //[22, 23, 25] 
		
		/*Set<Student> studentHashSet=new HashSet<Student>();
		addStudent.accept(studentHashSet);
		
		//only nonduplicate students are added to the list. 
		System.out.println(studentHashSet);*/
		
		//Linked HashSet: LinkedHashSet maintains the order in which items are pushed onto the set.
		Set<Integer> linkedHS=new LinkedHashSet();
		addElements.accept(linkedHS);
		System.out.println("LinkedHash Set:: "+linkedHS); 
		
		//Tree HashSet: It sorts the collection of element on the set. O(logn) : as it implements binary tree internally. 
		Set<Integer> treeHashSet=new TreeSet<>();
		addElements.accept(treeHashSet);
		System.out.println(treeHashSet);
		
	}
	private static Consumer<Set<Integer>> addElements=(set)->{
		set.add(23);
		set.add(22);
		set.add(25);
		set.add(23);
	};
	private static Consumer<Set<Student>> addStudent=(studentSet)->{
		Student student1=new Student("student1",01);
		Student student2=new Student("student1",01);
		Student student3=new Student("student1",01);
		Student student4=new Student("student4",04);
		studentSet.add(student1);
		studentSet.add(student2);
		studentSet.add(student3);
		studentSet.add(student4);
	};

	private static class Student{
		private int roll;
		private String name;
		
		public Student(String name, int roll){
			this.name=name;
			this.roll=roll;
		}

		public int getRoll() {
			return roll;
		}

		public void setRoll(int roll) {
			this.roll = roll;
		}

		public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}
		
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + ((name == null) ? 0 : name.hashCode());
			result = prime * result + roll;
			return result;
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Student other = (Student) obj;
			if (name == null) {
				if (other.name != null)
					return false;
			} else if (!name.equals(other.name))
				return false;
			if (roll != other.roll)
				return false;
			return true;
		}

		@Override
		public String toString() {
			return "Student [roll=" + roll + ", name=" + name + "]";
		}
		
	}
}
