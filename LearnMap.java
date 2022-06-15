package collection.framework;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.function.Consumer;

public class LearnMap {

	public static void main(String[] args) {
		Map<Integer, String> employeeID=new HashMap<>();
		employeeID.put(100,"After");
		employeeID.put(3, "Joey"); 				// add Joey to Map : [1=Joey]
		employeeID.putIfAbsent(2, "Monica"); 	//add Monica to key 2 : [1=Joey, 2=Monica]
		System.out.println(employeeID.entrySet());
		employeeID.put(2,"Random");				//add Random to Key 2 : [1=Joey, 2=Random], if key exist it replaces the value	
		employeeID.entrySet();					//.entrySet Prints all entry i.e key and value on the map
		System.out.println(employeeID.values());// values() print all values on the Map [Joey, Random]
		/*
		 * replaceAll can be used to replace all names on the list to a specific value i.e if value for multiple keys need to be changed 
		 * with some logic we can use replace all which accepts a BiFunction
		 */
		employeeID.replaceAll((empNo,empName)-> {if(empName.equals("Joey")) return "Ross";else return empName;});
		System.out.println(employeeID.entrySet());
		System.out.println("Treeset");
		treeMap();		// {1=Monica, 2=Ross, 3=Rachel, 4=Chandler, 5=Joey} sorted the map elements based on keys
		linkedHashMap();// {1=Monica, 4=Chandler, 5=Joey, 2=Ross, 3=Rachel} Maintains the order in which elements are pushed to the map
	}
	private static Consumer<Map<Integer, String>> addElements=(map)->{
		map.put(1, "Monica");
		map.put(4, "Chandler");
		map.put(5, "Joey");
		map.put(2, "Ross");
		map.put(3, "Rachel");
	};
	public static void treeMap(){
		Map<Integer, String> treemap=new TreeMap<>();
		addElements.accept(treemap);//pass by reference , consumer will add element to the ref. passed i.e tree passed 
				System.out.println(treemap);
	}
	public static void linkedHashMap(){
		Map<Integer, String> linkedMap=new LinkedHashMap<>(); 
		addElements.accept(linkedMap);
		System.out.println(linkedMap);
	}
}
