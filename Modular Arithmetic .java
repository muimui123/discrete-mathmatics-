import java.util.Scanner;
import java.util.*;

public class mod {

	//read files
	public static void main (String[] args) {

		Scanner s = new Scanner(System.in);
		String message = s.nextLine();
		//int key = s.nextInt();
		
		//part 1 output
		//System.out.println(encrypt(message,key));
		//System.out.println(key);
		
		//part 2 output
		//System.out.println(decrypt(message,key));
		//System.out.println(key);
		
		//part 3 output
		System.out.println("ciphertext:" +message);
		for (int key = 0; key < 26; key++){
			System.out.printf("key:{%s} decodes to: {%s}\n", key,decrypt(message, key));
		}
	}
	

	//encrypt method
	public static String encrypt(String message, int key){
		String s = "";
		int length = message.length();
		for (int x = 0; x < length;x++){
			char c = message.charAt(x);
			if ( c >= 'A' && c <= 'Z'){
				int pos = c-'A';
				char new_c = (char)((pos+key)%26 + 'A');
				s += new_c;
			}else{
				s += c;
			}
		}
		return s;
	}
	
	//decrypt method
	public static String decrypt(String message, int key){
		String s = "";
		int length = message.length();
		for (int x = 0; x < length;x++){
			char c = message.charAt(x);
			if ( c >= 'A' && c <= 'Z'){
				int pos = c-'A';
				char new_c = (char)((pos-key+26)%26 + 'A');
				s += new_c;
			}else{
				s += c;
			}
		}
		return s;
	}
}
