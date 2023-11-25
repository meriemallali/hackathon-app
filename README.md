The application was developed using Python version 3.11.3
To run the application, follow the steps with the commands below: 
1. First install the virtual environment: 
𝑝𝑦 − 𝑚 𝑣𝑒𝑛𝑣 𝑣𝑖𝑟𝑡𝑢𝑎𝑙𝑒𝑛𝑣
2. Activate the virtual environment; Browse into the scripts folder inside the virtualenv 
folder it can be scripts or Scripts.
𝑣𝑖𝑟𝑡𝑢𝑎𝑙𝑒𝑛𝑣\𝑆𝑐𝑟𝑖𝑝𝑡𝑠\𝑎𝑐𝑡𝑖𝑣𝑎𝑡𝑒
3. Install the requirements.txt file 
𝑝𝑖𝑝 𝑖𝑛𝑠𝑡𝑎𝑙𝑙 − 𝑟 𝑟𝑒𝑞𝑢𝑖𝑟𝑒𝑚𝑒𝑛𝑡𝑠.𝑡𝑥𝑡
4. Browse to the Django project folder ‘finalsrc’ (where the manage.py file is located) run to 
start the server, you can also specify the port number:
𝑝𝑦𝑡ℎ𝑜𝑛 𝑚𝑎𝑛𝑎𝑔𝑒. 𝑝𝑦 𝑟𝑢𝑛𝑠𝑒𝑟𝑣𝑒𝑟
5. To run the tests of the application: 
𝑝𝑦𝑡ℎ𝑜𝑛 𝑚𝑎𝑛𝑎𝑔𝑒. 𝑝𝑦 𝑡𝑒𝑠𝑡 𝑎𝑝𝑝.𝑡𝑒𝑠𝑡𝑠

To access the admin site: 
1. create a super-user using the follwoing command:
python manage.py createsuperuser 

Login details: 
Admin Site super user: 
username = user 
password = user 