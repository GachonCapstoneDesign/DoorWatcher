package com.example.parkdusang.testgcm;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.support.v4.app.NotificationCompat;
import android.support.v4.content.WakefulBroadcastReceiver;
import android.util.Log;

/**
 * Created by parkdusang on 16. 5. 15..
 */
public class GCMBroadcastReceiver  extends WakefulBroadcastReceiver {

    private  Context mContext;

    @Override
    public void onReceive(Context context, Intent intent) {

        mContext = context;
        Log.e("Test", "got message");
        Log.e("Test", "intent " + intent.getDataString());

        String title = intent.getStringExtra("title");
        String message = intent.getStringExtra("message");
        String pushType = intent.getStringExtra("push_type");

        if(pushType.equals("my")) {

        }

        Log.e("Test", "title " + title);
        Log.e("Test", "message " + message);

        sendNotification(title, message);
    }

    private void sendNotification(String title, String message) {

        Intent intent = new Intent(mContext, StreamingActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        PendingIntent pendingIntent = PendingIntent.getActivity(mContext, 0, intent,
                PendingIntent.FLAG_ONE_SHOT);

        //capstonedesign push test
        NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder(mContext)
                 .setSmallIcon(R.drawable.photo2)
                    .setLargeIcon(BitmapFactory.decodeResource(mContext.getResources(), R.drawable.photo2))
                .setContentTitle(title)
                .setContentText(message)
                .setAutoCancel(true)
                .setContentIntent(pendingIntent);



        NotificationManager notificationManager = (NotificationManager) mContext.getSystemService(Context.NOTIFICATION_SERVICE);
        notificationManager.notify(0, notificationBuilder.build());
    }
}
