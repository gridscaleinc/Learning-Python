package HomeWork008;

@Maxint(maxAge = 130)
public class AnnotationTest {

	public static void main(String[] args) {

		PersonAge person1 = new PersonAge();
		person1.setAge(120);
		Validator("Persion1",person1);

		PersonAge person2 = new PersonAge();
		person2.setAge(131);
		Validator("Persion2",person2);
	}

		private  static void Validator (String personName, PersonAge person) {

			Maxint iAnnotation = (Maxint) AnnotationTest.class.getAnnotation(AnnotationTest.class);
			//Maxint iAnnotation = (Maxint) AnnotationTest.class.getAnnotation(AnnotationTest.class);
			//MyAnnotationTest.class.getAnnotation(MyAnnotation.class);

			if (person.getAge() > iAnnotation.maxAge()){
				System.out.println(personName + ":" + person.getAge() + "is over 130.");
			}
			else {
				System.out.println(personName + ":" + person.getAge() + "is OK.");
			}

		}


}

//@Maxint(maxAge = 130)
class PersonAge {

	int age;

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

}

