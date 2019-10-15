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
*Has about a hundred items listed for sale.
*Users can create account/login using their email IDs or using Google oauth.
*Users can edit their information from an edit profile page.
*Users can view their ordered items.
*Has modules like cart and wish-list where users can add/remove items.
*Users can search for items using the search bar (with autocomplete). 
*Users can see/add reviews to products.
*Transactions are mocked using Cash on Delivery as a payment option.


#### HOW TO USE THIS PROGRAM

######	I	PURPOSE
######	II	SYSTEM REQUIREMENTS
######	III	INSTALLATION
######	IV	EXECUTION 
######	V	SAMPLES
######	VI	SUPPORT

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
We are not sure how this will behave for macOS but believe that the steps should be the same as for Ubuntu since both use bash in terminal.
	
####	IV	EXECUTION
	
To avoid any compatibility issues, we recommend that this website be executed in Ubuntu.

First, download the zip archive from github. Extract it and navigate to the folder it was extracted to. Open a terminal window in that folder. Then run the following lines of code:

Prerequisites:
This website requires Java and solr to be installed for the autocomplete search backend to work. To install Java, run the following lines of code:

```
sudo apt install default-jre
sudo apt install default-jdk
```

Then install solr using the following lines of code:

```
wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz
tar xzf solr-4.7.2.tgz
```

Build the schema for solr using `python manage.py build_solr_schema > schema.xml` and then navigate to the solr directory using `cd solr-4.7.2/example` and start the java app using `java -jar start.jar`

Then in a different terminal window run the python environment and then start the server.

```
source ./bin/activate
python manage.py runserver
```

Finally, navigate to localhost:8000 on your web browser and the website should be up and running.

####	V	SAMPLES
	
Download and deploy the project and use the following ID for ordering as well as accessing the dashboard:


####	VI	SUPPORT
	
If you have issues with running the code or need technical support in general with
issues relating to running the program, you can get in touch with the developers at

adhiraj.srivastava_asp20@ashoka.edu.in
daksh.baheti_asp20@ashoka.edu.in
devvrat.raghav_asp20@ashoka.edu.in
skzafar.ali_asp20@ashoka.edu.in

