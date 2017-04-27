package com.example.parkdusang.testgcm;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.webkit.WebView;

public class StreamingActivity extends AppCompatActivity {
    WebView browser;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_streaming);

        browser = (WebView) findViewById(R.id.webview1);
        browser.getSettings().setJavaScriptEnabled(true);
        browser.loadUrl("http:/192.168.0.12:5000/");
    }
}
