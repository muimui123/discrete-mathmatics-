import java.util.Scanner;
import java.lang.Math;

public class first {

	//for the beginning
	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		s.next();
		float s1 = s.nextFloat();
		s.next();
		float c = s.nextFloat();
		s.next();
		float g = s.nextFloat();

    	//print out the formula
		System.out.printf("S(n) = (%.1f)^(n-1)*(%.1f) + sigma(%.1f^(n-i)*(%.1f)) \n",  c, s1, c, g);

        
		for (int i = 1; i<11; i++){
			float result;
			result = s1 * (float)Math.pow(c, i-1) +  sigma(i,c,g);
			System.out.printf("S( %d ) = %.1f\n", i, result);
		}

	}

    public static float sigma(int n, float c, float g){
        float sum = 0;
        for (int i=2;i<=n;i++){
            sum += (float)Math.pow(c, n-i) * g;
        }
        return sum;
    }
}
    
