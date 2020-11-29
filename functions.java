import java.util.Scanner;
import java.util.*;

public class function {

	//read files
	public static void main (String[] args) {
		

		Scanner s = new Scanner(System.in);
		String line1 = s.nextLine();
		String line2 = s.nextLine();
		String line3 = s.nextLine();

		//split
		String[] domain = line1.split(" ");
		String[] codomain = line2.split(" ");
		String[] relation = line3.split(" ");
	 	String[] addd = new String[relation.length/2];


		//join array
		String joined1 = join(",",domain);
		String joined2 = join(",", codomain);


		for (int i=0;i<relation.length; i+=2){
				String a = relation[i];
				String b = relation[i+1];
				addd[i/2]= "(" +a+ "," +b+ ")";
		}

		String joined3 = join(",", addd);

		//print out
		System.out.printf("Domain:{%s}\n", joined1);
		System.out.printf("Codomain:{%s}\n",joined2);
		System.out.printf("Relation:{%s}\n", joined3);
		
		//determination
		boolean isFunction = function(relation,domain);
		if(isFunction){
			System.out.printf("This is a function.\n");
			
			boolean isOnto = onto(relation,codomain);
			if(isOnto){
				System.out.printf("It a onto.\n");
			}
			else{
				System.out.printf("It a *not* onto.\n");
			}
			
			boolean isOne2one = one2one(relation,codomain);
			if(isOne2one){
				System.out.printf("It a one to one.\n");
			}
			else{
				System.out.printf("It a *not* one to one.\n");
			}
			//Bijection 
			if (isOnto && isOne2one){
			System.out.printf("It is a bijection\n");
			}else{
			System.out.printf("It is *not* a bijection\n");
			}
		} else {
			System.out.printf("This is *not* a function.\n");
		}
		
	}
	//join method
	public static String join(String separator, String[] array){
			String result = "";
			for(int i=0;i<array.length;i++){
				result += array[i];
				if(i != array.length-1){
					result += separator;
				}
			}
			return result;
	}
	
	//indexOf
	public static int indexOf(String[] array, String target){
		int counter = 0;
		for(String element: array){
			if(element.equals(target)){
				return counter;
			}
			counter++;
		}
		return -1;
	}	


	//function
	public static boolean function(String[] relation, String[] domain){
		int [] function_check = new int[domain.length];
		for (int i = 0; i<relation.length; i+=2) {
			int index = indexOf(domain,relation[i]);
			if (index != -1){
				function_check[index]++;
			}
		}
		
		for (int num: function_check){
			if (num !=1){
				return false;
			}
		}
		return true;
	}

	//onto
	public static boolean onto(String[] relation, String[] codomain){
		int [] onto_check = new int[codomain.length];
		for (int i = 1; i<relation.length; i+=2) {
			int index = indexOf(codomain,relation[i]);
			if (index != -1){
				onto_check[index]++;
			}
		}
		
		for (int num: onto_check){
			if (num == 0){
				return false;
			}
		}
		return true;
	}

	
	//One to one
	public static boolean one2one(String[] relation, String[] codomain){
		int [] one_check = new int[codomain.length];
		for (int i = 1; i<relation.length; i+=2) {
			int index = indexOf(codomain,relation[i]);
			if (index != -1){
				one_check[index]++;
			}
		}
		
		for (int num: one_check){
			if (num > 1){
				return false;
			}
		}
		return true;
	}
	
	





}
