/**
 * 関数を作って1+2+........+n=？
 * しかも再帰を利用すること。
 */

package iHomeWork_Huang;

public class  HomeWork002 {
	public static void main(String arg[]) {

		//加算の上限値
		int num = 10;
		//int num = 100;
		//int num = 1000;


		//結果出力
		String printNum;
		printNum = "1+2+...+";
		System.out.print(printNum + num + " = " + addSeq(num));
	}

	private static int addSeq(int n) {
		//変数初期化
		int plusResult = 0;

		//連続加算と戻り値。
		for (int i =0; i <= n; i++)
			plusResult += i;
		return plusResult;
	}
}
