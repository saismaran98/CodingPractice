import java.util.Arrays;
import java.util.HashSet;
import java.util.function.Function;

public class IsUnique {
    //use array to determine if a string has all unique character.
    //Using other data stricture
    static Function<String, Boolean> isUniqueUsingHashSet=(str)->
    {
        HashSet<Character> hashSet=new HashSet<>();
        for(int i=0;i<str.length();i++){
            hashSet.add(str.charAt(i));
        }
        return hashSet.size() == str.length();
    };
    static Function<String, Boolean> isUniqueUsingArray=(str)->
    {
        //Saving space, using sort to increase time complexity.
        int i;int length=str.length();
        i=0;
        int[] memory =new int[str.length()];
        while(i<length){
            memory[i]=str.charAt(i);
             i++;
        }
        Arrays.sort(memory);
        i=0;
        while(i<str.length()-1){
            if(memory[i]-memory[i+1]==0)return false;
            i++;
        }
        return true;
    };
    static Function<String, Boolean> isUniqueUsingArraySavingTime=(str)->
    {
        if(str.length()>128)return false; //ASCII will allow unique characters till 128.

        boolean[] char_set =new boolean[128];
        for(int i=0;i<str.length();i++){
            int value=str.charAt(i);
           if(char_set[value]) {
                return false;
            }
            char_set[value]=true;
        }

      return true;
    };
    public static void main(String[] args) {
        System.out.println(isUniqueUsingHashSet.apply("test01"));
        System.out.println(isUniqueUsingArray.apply("test01"));
        System.out.println(isUniqueUsingArraySavingTime.apply("test01"));
    }
}
