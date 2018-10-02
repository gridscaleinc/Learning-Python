package iHomeWork_Huang;

public class HomeWork001 {
	public static void main(String arg[]) {
		int calc = 0;
		int subtotal =0;
		String pulsResult = "";
		for (int i = 1;i<=1000;i++) {
			subtotal = calc + i;
			pulsResult =  calc + "+" + i + "=" +  subtotal;
			System.out.println(pulsResult);		//ouput the formula of every step;
			calc = subtotal;
		}

		System.out.print("1+2+3+...1000= " + calc);
	}
}
