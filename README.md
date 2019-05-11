# Intrusion-Prevention-System
KNOW YOUR ENEMY<br>
By,<br>
  Animesh ND & Abhishek S

<br>
Instructions:
      
      >Repace IPs and port wherever required
      >Run all 3 containers, mapped to correct ports
      >Traffic Route : traffic_gen conatiner -> ml_model container -> localhost container
      >start traffic by sending a GET request to traffic_gen contaienr at route /start_traffic
      >stop  traffic by sending a GET request to traffic_gen contaienr at route /stop_traffic
      >Bad traffic is dropped, remaining reach 3rd container
