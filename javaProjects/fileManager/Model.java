import java.util.HashMap;
import java.util.Map;

class Model{
    final String fileAnswear = "/home/parciffal/GitRepo/Project/javaProjects/fileManager/answear.txt";
    final String fileQuest = "/home/parciffal/GitRepo/Project/javaProjects/fileManager/question.txt";
    public FileManager data  = new FileManager(fileAnswear, fileQuest);
    HashMap<String,String> nell = data.defoultData();
    
    public void run(String question){
       if(nell.containsKey(question)){
            System.out.println(nell.get(question));
       } else{
           if(nell.containsValue(question)){
               System.out.println(getKeyFromValue(nell, question));
           }
       }
           
    }
    public static Object getKeyFromValue(Map hm, Object value) {
            for (Object o : hm.keySet()) {
              if (hm.get(o).equals(value)) {
                return o;
              }
            }
            return null;
          }

}