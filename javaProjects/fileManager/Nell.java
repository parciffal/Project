import java.util.HashMap;


public class Nell {
    private HashMap<Integer,String> questions=new HashMap<>();
    private HashMap<Integer,String> anwsears=new HashMap<>();

  
    public HashMap<Integer, String> getQuestions() {
        return questions;
    }

    public void setQuestions(HashMap<Integer, String> questions) {
        this.questions = questions;
    }

    public HashMap<Integer, String> getAnwsears() {
        return anwsears;
    }

    public void setAnwsears(HashMap<Integer,String> anwsears) {
        this.anwsears = anwsears;
    }
}