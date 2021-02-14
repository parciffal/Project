import java.io.*;

public class Main{

    public static void main(String[] args) throws IOException {
        String fileAnswear = "/home/parciffal/GitRepo/Project/javaProjects/fileManager/answear.txt";
        String fileQuest = "/home/parciffal/GitRepo/Project/javaProjects/fileManager/question.txt";
    
        FileManager file = new FileManager(fileAnswear, fileQuest);
        file.read(fileAnswear);   

        }
}