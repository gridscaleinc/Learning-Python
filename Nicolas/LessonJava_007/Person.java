package HomeWork007;

//インタフェース Personを定義、greeting()挨拶というメソッドを定義。
interface Person {
	void greeting();
}

//ChineseクラスはPersonを実装して、さらにgreeting(String meesage)メソッドを実装。
class Chinese implements Person {
    public void greeting () {
           greeting ("你好！");
    }
    protected void greeting ( String msg) {
           System.out.println(msg);
    }

}

//JapaneseクラスはPersonを実装して、同じくgreeting(String message)を実装。
class Japanese implements Person {
    public void greeting () {
           greeting ("こんにちは！");
    }
    protected void greeting ( String msg) {
           System.out.println(msg);
    }

}
