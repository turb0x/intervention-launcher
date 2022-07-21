import requests
import sys
import os
import subprocess

def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


if not os.path.exists('C:/ProgramData/InterventioN/'):
    os.makedirs('C:/ProgramData/InterventioN/')

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
f = open("C:/ProgramData/InterventioN/hwid.txt", "w+")
f.write(hwid)
f.close()

print("Downloading data...")
download('https://www.dropbox.com/s/wxumhld6eqpjexf/backclean.png?dl=1', 'C:/ProgramData/InterventioN/backclean.png')
print(" ")
download('https://www.dropbox.com/s/o8o1h6g4maays87/butonhwid.png?dl=1', 'C:/ProgramData/InterventioN/butonhwid.png')
print(" ")
download('https://www.dropbox.com/s/elnb2cijvmjelo0/changelog.png?dl=1', 'C:/ProgramData/InterventioN/changelog.png')
print(" ")
download('https://www.dropbox.com/s/y7i8susoe51duo6/changelogbg.png?dl=1', 'C:/ProgramData/InterventioN/changelogbg.png')
print(" ")
download('https://www.dropbox.com/s/k4oz80za1gx7yb6/contact.png?dl=1', 'C:/ProgramData/InterventioN/contact.png')
print(" ")
download('https://www.dropbox.com/s/g62t2b5smhw6u9k/hwidclean.png?dl=1', 'C:/ProgramData/InterventioN/hwidclean.png')
print(" ")
download('https://www.dropbox.com/s/8ucoq6mjymyzgqs/icon.ico?dl=1', 'C:/ProgramData/InterventioN/icon.ico')
print(" ")
download('https://www.dropbox.com/s/mn8h478liwys2gt/play.png?dl=1', 'C:/ProgramData/InterventioN/play.png')
print(" ")
download('https://www.dropbox.com/s/6w0ki6mucqhb74l/settings.png?dl=1', 'C:/ProgramData/InterventioN/settings.png')
print(" ")
download('https://www.dropbox.com/s/kpgsdl8k5nx1tlx/update.png?dl=1', 'C:/ProgramData/InterventioN/update.png')
os.system("cls")
print("Downloading launcher...")
adminu = os.path.expanduser('~')
download('https://www.dropbox.com/s/rql2tp5asi4b0gy/launcher.exe?dl=1', f'{adminu}/Desktop/InterventioN.exe')
os.startfile(f'{adminu}/Desktop/InterventioN.exe')
