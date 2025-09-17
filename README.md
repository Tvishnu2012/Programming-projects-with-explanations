# Programming-projects-with-explanations

Hi all! I made this repository in the hope that others you want to start programming can have some source code to copy and understand the basics before they dive deep. <br>
There will be comments after each line explaining what part that line plays in the final result.
There will Python, HTML, CSS, JavaScript and a .sh file which you can use to install python and the needed modules etc. 

---------------------------------------------------------------------------------------------------------------------------------

To compile and run C code:
Use bash and go to the directory with the c file.

bash  <br>
gcc example.c -o example

Now you will have a new file with the c file with the name example.Now you use:

bash <br>
./example

This will run the example file and get you the result of your c code .If you want to run the programme again then compile from start.

----------------------------------------------------------------------------------------------------------------------------------
To run python using bash :
Go to the directory with the python programme using cd and check wheather you are there by using ls or dir.If the file exists then

bash <br>
python3 example.py               #or <br>
python example.py

Now the result will be dislpayed on the bash terminal.

----------------------------------------------------------------------------------------------------------------------------------
To run HTML CSS and JS run

bash <br>
python3 -m http.server 8080

this will open a port and host a local server.Then you will get a popup on the down right side of your display.Click the button that says "Open in Browser" or similar.This will take you to your browser and you can select you folder comtaining your html or directly open the html if it is not in a folder.

If you are using ubuntu on a vm or desktop you also have to go to your browser and give in the link (http://localhost:8080).
You can also use another port if the port 8080 is already in use but make sure to change the port in the URL and in the bash command above. 

----------------------------------------------------------------------------------------------------------------------------------
This is mainly for running  the code in Github Codespacs but will work on Ubuntu if python3/python and gcc are installed.  

To install gcc or update it:

bash <br>
sudo apt update  <br>
sudo apt install build-essential         #This will install gcc as well as some developer-tools

To check weather you already have gcc

bash  <br>
gcc --version

----------------------------------------------------------------------------------------------------------------------------------
install python(3) or update it:

sudo apt install python3         #or <br>
sudo apt install python

To check the version :

bash <br>
python --version

----------------------------------------------------------------------------------------------------------------------------------
Or install it by going to the root TaVis and by typing 

bash  <br>
bash setup.sh

----------------------------------------------------------------------------------------------------------------------------------