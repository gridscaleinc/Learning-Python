/*
 * string.format 練習
 */

package iHomeWork_Huang;

public class HomeWork004 {

	public static void main(String...arg) {

		/*
		 * Sample
		 */
		for (int i =0; i<200; i++) {
			System.out.println(String.format("%3s",i));
		}

		//切り分け
		System.out.println("*************************");


		/*
		 * 9桁の 文字列を作成して、Intに変更
		 * 3桁分け出力
		 */
		String m = "";
		for (int i = 1; i < 10; i++) {
			m += i;
		}
		int n = Integer.parseInt(m);
		System.out.println(String.format("%,d",n));
	}

}
