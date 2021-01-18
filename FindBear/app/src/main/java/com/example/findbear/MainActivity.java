package com.example.findbear;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void findbearJava(View view){
        TextView brands = (TextView) findViewById(R.id.brands);
        brands.setText("Got a bear");
        Spinner color = (Spinner) findViewById(R.id.color);
        String selected = String.valueOf(color.getSelectedItem());
        List<String> types = getType(selected);
        StringBuilder nell = new StringBuilder();
        for (String a: types){
            nell.append(a).append("\n");
        }
        brands.setText(nell);
    }
    public List<String> getType(String selected){
        List<String> types = new ArrayList<>();
        switch (selected){
            case "Light" :
                types.add("Corona");
                types.add("Gyumri");
                break;
            case "Dark" :
                types.add("Kotayq");
                types.add("Erebuni");
                break;
            default:
                types.add("Nothing Slected");
        }
        return types;
    }
}