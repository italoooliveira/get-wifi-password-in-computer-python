import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', 'ignore').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Todos os Perfis de Usurios:" in i]
wifi_list = []
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', 'ignore').split('\n')
    wifi_list = [b.split(":")[1][1:-1] for b in results if "Contedo da Chave" in b]
    try:
        print ("{:<30}|  {:<}".format(i, wifi_list[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))        
