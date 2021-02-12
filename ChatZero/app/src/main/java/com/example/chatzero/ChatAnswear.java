package com.example.chatzero;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class ChatAnswear {
    String questionFile = "com/example/chatzero/questions.txt";
    String answearFile = "com/example/chatzero/answear.txt";


    public Data defoultData(Data data){
        data = setQuestions(data);
        return data;
    }


    public Data setQuestions(Data data){
        int count = data.getQuestions().size();

        try {
            String line;
            BufferedReader reader=new BufferedReader(new FileReader(questionFile));
            while((line=reader.readLine()) != null){
                data.getQuestions().put(count,line);
                count++;
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }


    public Data setAnswears(Data data){
        int countAns=data.getAnwsears().size();
        try {
            String line;
            BufferedReader reader=new BufferedReader(new FileReader(answearFile));
            while((line=reader.readLine())!=null){
                data.getAnwsears().put(countAns,line);
                countAns++;
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }

    public String getAnswear(String question, Data data){
        boolean er = false;
        String answear="Chelav @ngers";
        for(Map.Entry<Integer,String> nell:data.getQuestions().entrySet()) {
            if (nell.getValue().equals(question)){
                answear = data.getAnwsears().get(nell.getKey());
                return answear;
            }else{
                er = true;
            }
        }
        return answear;
    }



}
