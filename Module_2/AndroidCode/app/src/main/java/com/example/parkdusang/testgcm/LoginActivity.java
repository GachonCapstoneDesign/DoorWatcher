package com.example.parkdusang.testgcm;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

public class LoginActivity extends AppCompatActivity {
    String result = null;
    String line = null;
    InputStream is = null;

    String url = "http://pesang72.cafe24.com/capstone/compareid.php";

    EditText id,pwd;
    Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        id =(EditText)findViewById(R.id.userid);
        pwd = (EditText)findViewById(R.id.pwd);

        btn = (Button)findViewById(R.id.Loginbtn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            if(id.getText().equals("")){
                Toast.makeText(getApplicationContext(),"입력사항이 없습니다.", Toast.LENGTH_SHORT);
            }
            else
                getData(url, id.getText().toString(), pwd.getText().toString());
            }
        });




    }


    public void getData(String url,String id , String pwd) {
        class GetDataJSON extends AsyncTask<String, Void, String> {
            @Override
            protected String doInBackground(String... params) {
                String uri = params[0];
                String ids = params[1];
                String pwd = params[2];
                ArrayList<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();
                nameValuePairs.add(new BasicNameValuePair("check", "1"));
                nameValuePairs.add(new BasicNameValuePair("_id", ids));
                nameValuePairs.add(new BasicNameValuePair("pwd", pwd));

                try {
                    HttpClient httpclient = new DefaultHttpClient();
                    HttpPost httppost = new HttpPost(uri);
                    httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs, "UTF-8"));
                    HttpResponse response = httpclient.execute(httppost);
                    HttpEntity entity = response.getEntity();
                    is = entity.getContent();
                    Log.i("TAG", ids);
                    Log.e("pass 1", "connection success ");
                } catch (Exception e) {
                    Log.e("Fail 1", e.toString());

                }


                try {
                    BufferedReader reader = new BufferedReader
                            (new InputStreamReader(is, "UTF-8"));
                    StringBuilder sb = new StringBuilder();
                    while ((line = reader.readLine()) != null) {
                        sb.append(line + "\n");
                    }
                    is.close();
                    result = sb.toString();
                    Log.e("1223", result);
                    return sb.toString().trim();
                } catch (Exception e) {
                    Log.e("Fail 2", e.toString());
                    return null;
                }

            }

            @Override
            protected void onPostExecute(String result) {
                Log.e("1234", result);
                if(result.substring(1,result.length()-1).equals("failedID")){
                    Toast.makeText(getApplicationContext(),"아이뒤 실패",Toast.LENGTH_SHORT);
                }
                else if(result.substring(1,result.length()-1).equals("failedpassword")){
                    Toast.makeText(getApplicationContext(),"비밀번 실패",Toast.LENGTH_SHORT);
                }
                else{
                    Intent intent2 = new Intent(getApplicationContext(),StreamingActivity.class);
                    startActivity(intent2);
                }

            }
        }


        GetDataJSON g = new GetDataJSON();
        try {
            g.execute(url, id, pwd).get();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
    }
}
