package JUnitTesting;

	import static org.junit.Assert.assertEquals;
	import static org.junit.Assert.assertFalse;

	import org.junit.Test;

public class App {
		
		@Test
		public void addIntsTest() {		
			Main Test = new Main();
			int x = 2;
			int y = 2;
			int expected = 4;
			int add = Test.addInts(x, y);
			assertEquals(expected, add);		
			
		}
		
		@Test
		public void addStringsLengthTest() {
			Main JTest = new Main();
			String x = "Hello";
			String y = "Kerwin";
			Long expected = (long) 16;
			Long greeting = (long) JTest.addStrings(x, y).length();
			assertEquals(expected, greeting);			
			
		}
		
		@Test
		public void findLenTest() {
			Main JTest = new Main();
			String x = "Hello";
			Long expected = (long) 8;
			Long greeting = (long) JTest.findLen(x).length();
			assertEquals(expected, greeting);		
			
		}
		
		@Test
		public void divXbyYTest() {
			Main JTest = new Main();
			int x = 2;
			int y = 1;
			int expected = 2;
			int div = JTest.divXbyY(x, y);
			assertEquals(expected, div);		
			
		}
		
		@Test
		public void reverseIntArrayTest() {
			Main JTest = new Main();
			int[] x = {1, 2, 3, 4, 5, 6, 7, 8};
			int expected = 7;
			int[] array = JTest.reverseIntArray(x);
		
			System.out.println(array);
			assertEquals(expected, array);	
		
			
		}
		
		@Test
		public void Test1() {
			Main JTest = new Main();
			int[] x = {8};
			int[] expected = {8};
			int[] range = JTest.Test1(x);
			assertEquals(expected, range);				
			
		}
		
		@Test
		public void Test2() {
			Main JTest = new Main();
			int[] x = {8, 9};
			int[] expected = {8, 9};
			int[] range = JTest.Test2(x);
			assertEquals(expected, range);		
			
		}
		
	
			
		}
		
		
		
		


