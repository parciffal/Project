package com.example.controller;

import java.io.*;

public class Main{

    public static void main(String[] args) throws IOException {
        String fileAnswear = "/ChatZero/app/src/main/java/com/example/controller/answear.txt";
        String fileQuest = "/ChatZero/app/src/main/java/com/example/controller/answear.txt";
    
        FileManager file = new FileManager(fileAnswear, fileQuest);
        file.read(fileAnswear);

        }
}