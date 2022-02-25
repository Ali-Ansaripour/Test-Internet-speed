import os
import time
from tqdm import tqdm 
from speedtest import speedtest
from colorama import Fore, init

print(Fore.LIGHTRED_EX+"Just wait a minute..."+Fore.RESET)

x = speedtest.Speedtest()

for i in tqdm(range(100),desc="Just wait...", colour="green") :
    time.sleep(0.10)
    pass

time.sleep(5)
os.system('cls')

print(Fore.LIGHTMAGENTA_EX+f"My Download speed is : {Fore.GREEN}{x.download()/pow(10,6)} Mbps")
print(Fore.LIGHTMAGENTA_EX+f"My Upload speed is : {Fore.GREEN}{x.upload()/pow(10,6)} Mbps")
best_server = x.get_best_server()
for key , value in best_server.items() :
    print(Fore.LIGHTRED_EX+f"The best server is : \n {Fore.LIGHTBLUE_EX} {key} : {value} ")
    pass

print(Fore.LIGHTGREEN_EX+"************************")

closest_server = x.get_closest_servers()
for key , value in closest_server[0].items() :
    print(Fore.LIGHTRED_EX+f"The closest server is : \n{Fore.LIGHTBLUE_EX} {key} : {value}")
    pass
    
    #Ali Ansaripour
