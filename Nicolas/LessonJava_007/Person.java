package iHomeWork_Huang;

public interface Person {
	//メソッド(型のみ宣言)
	void greeting();
}

class Chinese implements Person{
    // メソッドの実装
    public void greeting() {
        System.out.println("Chinese said : 你好。");
    }

}

class Japanese implements Person{
    // メソッドの実装
    public void greeting() {
        System.out.println("Japanese said : こんにちは。");
    }

}



