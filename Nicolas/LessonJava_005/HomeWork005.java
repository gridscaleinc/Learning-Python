package iHomeWork_Huang;

public class HomeWork005 {

	public static void main(String...args) {

		int i = 1234567;
		//char 型の最小値、最大値
		System.out.println("char Max : " + (int)Character.MAX_VALUE);
		System.out.println("char Max : " + (int)Character.MIN_VALUE);
		//int 型の最大値、最小値
		System.out.println("int  Max : " + Integer.MAX_VALUE);
		System.out.println("int  Max : " + Integer.MIN_VALUE);
		//long 型の最小値、最大値
		System.out.println("long Max : " + Long.MAX_VALUE);
		System.out.println("long Max : " + Long.MIN_VALUE);
		//1234567という数値の2進数,8進数,16進数表現
		System.out.println("1234567の2進数表現 ： " + Integer.toBinaryString(i));
		System.out.println("1234567の8進数表現 ： " + Integer.toOctalString(i));
		System.out.println("1234567の16進数表現： " + Integer.toHexString(i));

		//1234567をlongとして、右へ4bit shift、同時に最高位に1を補充することで、どういう整数になるかを示す。
		long m = 1234567;
		System.out.println("1234567の右４シフト： " + (m >> 4));


	}

}
