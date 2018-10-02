//20181002 modify source format

package iHomeWork_Huang;

public class HomeWork001 {
	public static void main(String arg[]) {
		int calc = 0;
		int subtotal = 0;
		String plusResult = "";
		for (int i = 1; i <= 1000; i++) {
			subtotal = calc + i;
			plusResult = calc + "+" + i + "=" + subtotal;
			System.out.println(plusResult);		//ouput the formula of every step;
			calc = subtotal;
		}
		System.out.print("1+2+3+...+1000 = " + calc);
	}
}
