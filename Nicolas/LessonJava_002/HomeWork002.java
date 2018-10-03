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

		//加算の上限値
		 num = 10;
		// num = 100;
		// num = 1000;

		//連続加算の出力
		String printNum;
		printNum = "1+2+...+";
		//System.out.println(printNum + num + " = " + addSeq(num));
		//System.out.println();
		System.out.println(printNum + num + " = " + fib(num));

	}

	//連続加算と戻り値。
	private static int addSeq(int n) {
		int plusResult = 0;
		for (int i = 0; i <= n; i++) {
			plusResult += i;
		}
		return plusResult;
	}

	//再帰化
	private static int fib(int m) {
		int fibResult = 0;
		fibResult = addSeq(num - 1) + num;
		return fibResult;
	}


}
