Ecommerce website using django-oscar
------------------------------------

This is an ecommerce website for monitors made with bootstrap and the django-oscar framework in python.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License in the LICENSE.md file for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Features:
1. Has about a hundred items listed for sale.
1. Users can create account/login using their email IDs or using Google oauth.
1. Users can edit their information from an edit profile page.
1. Users can view their ordered items.
1. Has modules like cart and wish-list where users can add/remove items.
1. Users can search for items using the search bar (with autocomplete). 
1. Users can see/add reviews to products.
1. Transactions are mocked using Cash on Delivery as a payment option.


#### HOW TO USE THIS PROGRAM

######	I	PURPOSE
######	II	SYSTEM REQUIREMENTS
######	III	INSTALLATION
######	IV	EXECUTION 
######	V	SUPPORT

####	I	PURPOSE

This program aims to mimic an ecommerce website which can be deployed and scaled with ease. 

####	II	SYSTEM REQUIREMENTS
   
   This program was made and tested on Ubuntu 18.04 and 19.04 virtual machines on windows 10 hosts (Build 1903) with the following specifications:

	Atleast an Intel Core i5 or Ryzen 5
	At least 8 GB RAM (of which at least 4 GB alotted to virtual machine)
	VBoxSVGA or similar graphics controller with at least 128 MB memory for the virtual machines.

   Any system that can run Ubuntu 16.04 either natively or in a virtual machine should be able to run this website just fine.

####	III	INSTALLATION
	
This website does not require any installation as it comes with its own virtual environment with all packages installed.
However, if you are running a windows machine, we recommend that you you install Ubuntu in a virtual machine by using either VirtualBox or Windows Hyper-V.
Functionality should be consistent for any Posix-based system, although prior testing has only been done on Ubuntu.
	
####	IV	EXECUTION
	
To avoid any compatibility issues, we recommend that this website be executed in a Posix-based system.

First, download the zip archive from github. Extract it and navigate to the folder it was extracted to. Navigate to the "ecommerce" folder within it. You should be able to see a manage.py file. Open a terminal window in that folder. Then run the following lines of code:

###### Prerequisites:

- Python 3
- virtualenv
- Java (OpenJDK or Oracle)

If you do not have the above prerequisites installed, run the following commands.

```
sudo apt install python3
sudo apt install virtualenv 
sudo apt install default-jre
sudo apt install default-jdk
```

###### Setting up the environment

Step 1 -

Navigate to your home directory (root) and enter the following commands to create the virtual environment.

```
virtualenv oscar
cd ~/oscar
```
Then activate the environment using:

```
source ./bin/activate
```
Once the environment is activated, create a copy of requirements.txt in the 'oscar' directory and run:

```
pip install -r requirements.txt
```

Once the 'oscar' directory is populated with the required libraries, create a local copy of the folders in this repository. This can be done through either git or downloading a zipped version. 

Then, replace the contents of your local 'oscar' directory with the contents of this repo. This replacement is required because some libraries were edited at the source during the project's creation phase, and so must be shipped separately.

Step 2 - 

Deactivate your virtual environment using the `deactivate`. Then install Apache Solr using the following code:

```
wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz	#Downloads the Solr package
tar xzf solr-4.7.2.tgz		#Creates a local directory containing the Solr package
```
Once Solr is installed, the search schema must be defined. 

Build the schema for solr using `python manage.py build_solr_schema > solr-4.7.2/example/solr/collection1/conf/schema.xml`.

Since the latest version(s) of django-oscar create an unusable schema, this must be manually replaced with a working file.

Download the `schema.xml` file in this repo and use it to replace the file located in:
```./solr-4.7.2/example/solr/collection1/conf/schema.xml```

Then navigate to the solr directory using `cd solr-4.7.2/example` and start the java app using `java -jar start.jar`

Once the Apache Solr server is running, use another terminal window or tab and run the following commands to run the django server:

```
source ~/oscar/bin/activate
python ~/oscar/ecommerce/manage.py runserver
```
Finally, navigate to either 127.0.0.1:8000 or localhost:8000 on your web browser and the website should be up and running.


####	V	SUPPORT
	
If you have issues with running the code or need technical support in general with
issues relating to running the program, you can get in touch with the developers at:

adhiraj.srivastava_asp20@ashoka.edu.in, 
daksh.baheti_asp20@ashoka.edu.in, 
devvrat.raghav_asp20@ashoka.edu.in, 
skzafar.ali_asp20@ashoka.edu.in

