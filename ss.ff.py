import pywhatkit
phone_numer = '+573132035893'
group_id = ''
message = 'Hola profe, Prueba de Python'
time_hour = 11
time_minute = 36
waiting_time_to_send = 30
close_tab = True
waiting_time_to_close = 2
mode = "contact"
if mode == "contact":
 pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab,
waiting_time_to_close)
elif mode == "group":
 pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab,
waiting_time_to_close)
else:
 print("Error code: 97654")
 print("Error Message: Please select a mode to send your message.")