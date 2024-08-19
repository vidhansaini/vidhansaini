from plyer import notification
import time  
  
notification_title = 'YOUR DAILY WATER DRINK REMAINDER!'  
notification_message = 'Time for a water break have a drink'  
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )

time.sleep(60 * 60 * 2)   