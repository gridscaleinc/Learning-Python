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

		System.out.println("**********************************");

		//1234567をlongとして、右へ4bit shift、同時に最高位に1を補充することで、どういう整数になるかを示す。
		long m_Long = 1234567;
		m_Long = m_Long >> 4;
		System.out.println("1234567[long]の右４シフト： " + m_Long);

		double mLength = String.valueOf(m_Long).length();
		Long lastNum = m_Long + (long)Math.pow(10.0,mLength-1 );
		System.out.println("最高位に1を補充 : " + lastNum);

		/*
		//int型の試し
		int l_Int = 1234567;
		l_Int = l_Int >> 4;
		System.out.println("1234567[int]の右４シフト： " + l_Int);
		double lLength = String.valueOf(l_Int).length();
		Long l_lastNum = l_Int + (long)Math.pow(10.0,lLength-1 );
		System.out.println("最高位に1を補充 : " + l_lastNum);
		 */

		System.out.println("**********************************");
		long abc = 1234567l;
		System.out.println(abc);
		abc = abc | 0x8000000000000000l;
		System.out.print("Long型 : " + Long.toBinaryString(abc));

	}

}
