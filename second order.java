import java.util.Scanner;
import java.lang.Math;

public class fo {

	//for the beginning
	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		s.next();
		float s1 = (float)s.nextInt();
		s.next();
		float s2 = (float)s.nextInt();
		s.next();
		float c1 = (float)s.nextInt();
		s.next();
		float c2 = (float)s.nextInt();

		//math equation -b+-b^-4ac/2
		float r1;
		float r2;
		r1 = (c1 + (float)Math.sqrt((float)Math.pow(c1,2) + 4*c2))/(float)2;
		r2 = (c1 - (float)Math.sqrt((float)Math.pow(c1,2) + 4*c2))/(float)2;
		System.out.printf("r1 = %.1f\n", r1);
		System.out.printf("r2 = %.1f\n", r2);

		if (r1 != r2){
		//calculating p & q
		float p;
		float q;
		p = (s2-(s1*r2))/(r1-r2);
		q = s1 - p;
		System.out.printf("p = %.1f\n", p);
		System.out.printf("q = %.1f\n", q);

		//print out the formula
		System.out.printf("S(n) = (%.1f)(%.1f)^(n-1) + (%.1f)(%.1f^(n-1)) \n",  p, r1, q, r2);

		for (int i = 1; i<11; i++){
			float result;
			result = p * (float)Math.pow(r1, i-1) + q * (float)Math.pow(r2,i-1);
			System.out.printf("S( %d ) = %.1f\n", i, result);
		}
	}else{
		float p;
		float q;
		p = s1;
		q = s2/r1 - p;
		System.out.printf("p = %.1f\n", p);
		System.out.printf("q = %.1f\n", q);

		//print out the formula
		System.out.printf("S(n) = (%.1f)(%.1f)^(n-1) + (%.1f)(n-1)(%.1f^(n-1)) \n",  p, r1, q, r2);

		for (int i = 1; i<11; i++){
			float result;
			result = p * (float)Math.pow(r1, i-1) + q*(float)(i-1) * (float)Math.pow(r2,i-1);
			System.out.printf("S( %d ) = %.1f\n", i, result);
		}
	}

	}

}
