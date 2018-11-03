package HomeWork007;


//Greetingというクラスを作って、mainメソッドに日本人と中国人のインスタンスを作って、お互いに挨拶させて下さい。
public class Greeting {

	public static void main(String...args) {

		Chinese helloCN = new Chinese();
		helloCN.greeting();

		Japanese helloJP = new Japanese();
		helloJP.greeting();

	}

}
