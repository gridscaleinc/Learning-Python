/**
 * クラス名：HomeWork002
 * 機能説明：
 * 　①関数を作って1+2+........+n=？
 * 　②しかも再帰を利用すること。
 */

package iHomeWork_Huang;

public class  HomeWork002 {
	private static int num;

	public static void main(String arg[]) {

		//加算値
		//num = -1;
		//num = 10;
		 num = 100;

		//結果出力
		int sum = fib(num);
		//fib(-1);

		String printNum;
		printNum = "1+2+...+";
		System.out.println(printNum + num + " = " + sum);
		fib(-1);
	}


	//再帰化
	private static int fib(int m) {

		if (m < 0) {
			throw new RuntimeException();
		}

        if (m == 0) {
            return 0;
        }
        if (m == 1) {
            return 1;
        }

		return fib(m - 1) + m;
	}


}
