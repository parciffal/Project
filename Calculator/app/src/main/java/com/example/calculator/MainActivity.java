package com.example.calculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.mariuszgromada.math.mxparser.Expression;

public class MainActivity extends AppCompatActivity {

    Button butt0,butt1,butt2,butt3,butt4,butt5,butt6,butt7,butt8,butt9,buttH,buttSt,buttPM,buttPl,buttMi,buttBaz,buttBa,buttT,buttC,buttSc,back;
    TextView tvInput,tvOutput;
    String process;
    Boolean plusMin = false;
    Boolean scope = false;

    static String remChar(String str, Integer n) {
        String front = str.substring(0, n);
        String back = str.substring(n+1, str.length());
        return front + back;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        butt0 = findViewById(R.id.butt0);
        butt1 = findViewById(R.id.butt1);
        butt2 = findViewById(R.id.butt2);
        butt3 = findViewById(R.id.butt3);
        butt4 = findViewById(R.id.butt4);
        butt5 = findViewById(R.id.butt5);
        butt6 = findViewById(R.id.butt6);
        butt7 = findViewById(R.id.butt7);
        butt8 = findViewById(R.id.butt8);
        butt9 = findViewById(R.id.butt9);

        buttH = findViewById(R.id.buttH);
        back = findViewById(R.id.back);

        buttSt = findViewById(R.id.buttSt);
        buttPM = findViewById(R.id.buttPM);
        buttPl = findViewById(R.id.buttPl);
        buttMi = findViewById(R.id.buttMi);
        buttBaz = findViewById(R.id.buttBaz);
        buttBa = findViewById(R.id.buttBa);
        buttT = findViewById(R.id.buttT);
        buttC = findViewById(R.id.buttC);


        buttSc = findViewById(R.id.buttSc);

        tvInput = findViewById(R.id.tvInput);
        tvOutput = findViewById(R.id.tvOutput);

        buttC.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvInput.setText("");
                tvOutput.setText("");
                scope = false;
                plusMin = false;
            }
        });
        butt0.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();

                tvInput.setText(process+"0");
            }
        });
        butt1.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "1");
            }
        });
        butt2.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "2");
            }
        });
        butt3.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "3");
            }
        });
        butt4.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "4");
            }
        });
        butt5.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "5");
            }
        });
        butt6.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "6");
            }
        });
        butt7.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "7");
            }
        });
        butt8.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "8");
            }
        });
        butt9.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "9");
            }
        });
        buttSt.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                if (process.charAt(process.length() - 1) != ',') {
                    tvInput.setText(process + ".");
                }
            }
        });
        buttPM.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+"^");
            }
        });
        buttPl.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "+");
            }
        });
        buttMi.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "-");
            }
        });
        buttBaz.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "*");
            }
        });
        buttBa.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "/");
            }
        });
        buttT.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                process = tvInput.getText().toString();
                tvInput.setText(process+ "/100*");
            }
        });
        buttSc.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                if (scope == false) {
                    process = tvInput.getText().toString();
                    tvInput.setText(process + "(");
                    scope = true;
                }else{
                    process = tvInput.getText().toString();
                    tvInput.setText(process + ")");
                    scope = false;
                    if (process.substring(0,2).equals("(-")){
                        plusMin = false;
                    }
                }

            }
        });
        back.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                if (process != "") {
                    process = tvInput.getText().toString();
                    process = remChar(process, process.length() - 1);
                    tvInput.setText(process);
                }
            }
        });
        buttH.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String userExp = tvInput.getText().toString();
                Expression exp = new Expression(userExp);

                String result = String.valueOf(exp.calculate());
                tvOutput.setText(result);
                tvInput.setText(result);
            }
        });
    }


}

