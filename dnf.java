import java.util.*;

public class dnf {
	public static void main(String[] args){
	    boolean start = true;
		ArrayList<String> for1 = new ArrayList<String>();
		ArrayList<String> for0 = new ArrayList<String>();
	    
		Scanner scanner = new Scanner(System.in); //set up a Scanner for STDIN
		String[] titles = scanner.nextLine().split(" "); //get the top line (the title)
		scanner.nextLine(); //skip "------------------------------------------------------------------------"
		int size = titles.length-1;
		int row_count = (int)Math.pow(2,size);
		
		//setup for1 and for0 ArrayList
		for(int count=0;count<row_count;count++){
			String row = scanner.nextLine();
			if(row.charAt(row.length()-1) == '1'){
				for1.add(row);
			} else if(row.charAt(row.length()-1) == '0'){
				for0.add(row);
			}
		}
		
		//print out result
		String s = "";
		//loop through all rows that have '1' for OUTPUT
		for(int i = 0;i<for1.size();i++){
			if(i != 0){
				s += "+ ";
			}
			//deal with each row
			String[] row = for1.get(i).split(" ");
			for(int j = 0;j<row.length-1;j++){
				if(row[j].equals("0")){
					s += titles[j] + "'";
				} else if(row[j].equals("1")) {
					s += titles[j];
				}
				s += " ";
			}
		}
		System.out.println(s);
		
		//for extra credit, CNF
		s = "";
		for(int i=0;i<for0.size();i++){
			s += "(";
			//deal with each row
			String[] row = for0.get(i).split(" ");
			for(int j = 0;j<row.length-1;j++){
			    if(j != 0){
    				s += " + ";
    			}
				if(row[j].equals("0")){
					s += titles[j];
				} else if(row[j].equals("1")) {
					s += titles[j] + "'";
				}
			}
			s += ")";
		}
		System.out.println(s);
	}
}