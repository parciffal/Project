package com.example.chatzero;

import java.util.HashMap;

public class Data {
    private String name;
    private HashMap<Integer,String> questions=new HashMap<>();
    private HashMap<Integer,String> anwsears=new HashMap<>();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

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
