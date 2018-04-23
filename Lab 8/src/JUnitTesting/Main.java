package JUnitTesting;

import org.junit.Test;

public class Main {

		public int addInts(int x, int y) {			
			return  x + y;		
		}
		public String addStrings(String x, String y) {	
			return "String x" + "String y";	
		}
		public String findLen(String x) {	
			return "String x";	
		}
		public int divXbyY(int x, int y) {	
			return x / y;			
		}
		public int[] reverseIntArray(int[] x) {
			return x;		
		}
		public int[] Test1(int[] x) {		
			int[] range = {7};
			return range;
		}		
		public int[] Test2(int[] x) {
			int [] range = {7, 8};
			return range;
		}
	
	}

