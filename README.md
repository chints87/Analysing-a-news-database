# News Reporting tool
This project sets up a fictional news database on a PostgreSQL database. The provided python script uses a psycopg2 library to
send queries to the PostgreSQL database to produce a report that generates:

1. The top 3 most read articles by readers.
2. The list of authors from the highest to lowest readership
3. The days when request errors is more than 1%. 

## Install
1. In order to run a virtual machine on your host, download and install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). 
2. Download and install [Vagrant](https://www.vagrantup.com/) that will enable sharing of files between the host and virtual machine. 
3. Clone the repository to your localhost from here[https://github.com/chints87/newsdata.git] and give it the folder a name, for example in this case **newsdata**.
4. The Vagrantfile is the configuration file to setup the VM. 

In the git bash, locate the *vagrant* directory and use _vagrant up_ to configure the VM that will install all requirements, found in the Vagrantfile, needed for this project. Log into the Linux OS using *vagrant ssh* and it would contain *Python, PostgresSQL and pyscopg2* components. The **newsdata** database can be downloaded from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Extract and move the **newsdata.sql** file into the folder **newsdata** created eralier. 

To create the database, go to the vagrant directory, and on the command line type 
```
psql -d news -f newsdata.sql
```

## Command Line 
Create views in PostgreSQL from tables provided in the newsdata.sql. Then write a python script that will connect to the newsdata database to access and fetch views that were created. The data fetched from the database is generated as a list in python. From this list, the reports are generated. 

Views created shown below are availabe in the __create_view.sql__ file in the folder.

To add views, on the command line type 
```
psql -d news -f create_views.sql*
```

Over here to connect to the database four arguments are required. They are the 
name of the database, which is news, then user is default as vagrant as set by the configuration. These can be changed to change or add more users. The password is set in psql
And host in this case would be the localhost as the database is on the host VM. 

To set the password for the user 'vagrant', 

```
psql news
````

```sql
ALTER ROLE vagrant WITH PASSWORD 'vagrant';
```

```python
    conn = psycopg2.connect(database="news", user="vagrant", \
           password="vagrant", host="localhost")  
```


To generate the report on the command line type call the python file in the same(?) directory.
To avoid file ending errors .py file, install dos2unix

```
sudo apt-get install dos2unix 
```
Convert .py file to a unix compatible file
```
dos2unix reportgen.py
```
Run the file by typing this on the command line
```
./reportgen.py
```

## Attribution

1. The code for the three python files and SQL queries were sourced , modified, and developed with guidance from the Udacity FNSD course.

2. The _main_ function in the three python modules were obtained and modified from [here](https://stackoverflow.com/questions/6133107/extract-date-yyyy-mm-dd-from-a-timestamp-in-postgresql/6133144) 
 
3. The code for calculating percentage was obtained and modified from [here](https://stackoverflow.com/questions/36531361/calculate-percentage-between-two-columns-in-sql-query-as-another-column) 

4. The code for obtaining date from timestamp was obtained and modified from [here](https://stackoverflow.com/questions/2354717/how-to-write-a-postgresql-query-for-getting-only-the-date-part-of-timestamp-fiel)

5. The code for the view _logarticleid_ was taken and modified a bit by the feedback provided by the Udacity mentor. 

6. The code 'for' loop was applied and modified to the mostreadauthor that was provided from feedback by the Udacity mentor that was suggested for mostarticles.

7. The content for the **News Reporting Tool** was provided by the Udacity mentor and modified. 

8. To make a create_view.sql file was provided by the Udacity mentor.

9. The '/articles/' || articles.slug = log.path was provided by the Udacity mentor.

10. The for loop in the most read articles was provided by the Udacity mentor.

11. The print statement in the most error was provided vy the Udacity mentor.
