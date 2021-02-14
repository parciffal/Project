import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class FileManager {
    public String fileAnswear ;
    public String fileQuest ;
    public BufferedReader reader;
    public FileWriter writer;
    public HashMap<String, String> data = new HashMap<>();

    public FileManager(String fileAnswear, String fileQuestions) {
        this.fileAnswear = fileAnswear;
        this.fileQuest = fileQuestions;
    }

    public HashMap<String, String> defoultData() {
        HashMap<String, String> nell = new HashMap<>();
        ArrayList<String> question = readFile(this.fileQuest);
        ArrayList<String> answear = readFile(this.fileAnswear);
        for (int i = 0 ; i<question.size() ; i++){
            nell.put(question.get(i), answear.get(i));
        }
        return nell;
    }

    public void read(String fileName) {
        try {

            reader = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            reader.close();
        } catch (Exception exception) {
            System.out.printf("Can't read file");
        }
    }

    public ArrayList<String> readFile(String fileName) {
        ArrayList<String> red = new ArrayList<>();
        try {

            reader = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = reader.readLine()) != null) {
                red.add(line);
            }

            reader.close();
        } catch (Exception exception) {
            System.out.printf("Can't read file");
        }
        return red;
    }

    public void writeInFile(String fullPath, String text) {
        try {
            writer = new FileWriter(fullPath, true);
            writer.write("\r\n");
            writer.write(text);
            writer.close();
        } catch (Exception exception) {
            System.out.printf("Can't write");
        }
    }
}