package iHomeWork_Huang;

public class HomeWork003 {


	public static void main(String arg[]) {

		//月の表示
		System.out.println("10月");

		//曜日の表示
		String[] dayName = new String[] { "月","火","水","木","金","土","日" };
		for (int i = 0; i < 7; i++) {
			//System.out.print(dayName[i] + "　");
			System.out.print(String.format("%2s", dayName[i]));
		}

		System.out.println();

		//日付の表示、週ごとに改行。
		int[] monthlyDay = new int[31];
		for (int i = 0; i <31; i++) {
			monthlyDay[i] = i+1;
		}

        for (int i = 0; i < 31; i++){
        	if (i == 0) {
        		//System.out.print( monthlyDay[0] + "　");
        		System.out.print(String.format("%3s",monthlyDay[0]));
        	}
        	else if ( monthlyDay[i] % 7 == 0) {
            	System.out.println(String.format("%3s",monthlyDay[i]));
        	}
        	else {
        		System.out.print(String.format("%3s",monthlyDay[i]));
        	}

        }

	}

}
