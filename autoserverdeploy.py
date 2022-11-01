import os

os.system("sudo apt-get install apache2 -y ")
indexdata='Hi my automatic pythonserver'
os.system(f"sudo echo {indexdata} > /var/www/html/index.html ")
os.system("sudo service apache2 start")

