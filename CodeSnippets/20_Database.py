'''
Why we need database?

Short answer: Not everything can be stored in-memory/RAM
    - larger data needs to be stored in disk
    - RAM is volatile memory but we need data 24x7 doesn't matter if machine crashes
    
https://en.wikipedia.org/wiki/Database

What is a database?
A database is an organized collection  data, typically stored electronically in a computer system. 
A database is usually controlled by a database management system (DBMS).


How is index stored in DBMS?
Few commonly used datastructure to store index in database 
    1. B+ tree
    2. Skip list
    3. Inverted index

Types of database ?
1. Relational database(SQL) e.g mySQL, Oracle, PostgreSQL, etc..
2. No-SQL (Preferred unstructured and semistructured data)
    - Key-value pair (dynamo DB, redis, memcached, etc)
    - Graph database(neo4j, etc)
    - Document (MongoDB, CouchDB, etc..)
    - Columnar database (Cassandra, Apache HBase, etc)
    - FTS engine (Lucene based Solr, elastic/open search, etc)

3. OLAP system
    - Don't bother about redundancy, care just about performance
    - Multi-dimensional table



SQL vs NoSql:

SQL: Database is preferred over NoSql when ACID is mandatory,
where ACID = Atomicity, Consistency, Isolation, Durability


SQL database insights:

                    SQL commands
                         |
    ----------------------------------------------
    |           |           |          |          |
    DDL.       DML         DCL.       TCL.       DQL
    

##############################
Data Definition Language (DDL)
##############################

    CREATE: used to create a new table in the database.
        syntax: CREATE TABLE TABLE_NAME (COLUMN_NAME DATATYPES[,....]);  
        e.g) CREATE TABLE Employee(Name VARCHAR2(20), Email VARCHAR2(100), DOB DATE);  
    
    DROP: delete both the structure and record stored in the table
        syntax: DROP TABLE table_name
        e.g) DROP TABLE Employee;  
        
    ALTER: used to alter the structure of the database.
        syntax: 
        To add new column: 
            ALTER TABLE table_name ADD column_name COLUMN-definition;    
    
        To modify existing column:
            ALTER TABLE table_name MODIFY(column_definitions....);  
    
    
        e.g) 
        ALTER TABLE student ADD(ADDRESS VARCHAR2(20));  
        ALTER TABLE student MODIFY (NAME VARCHAR2(30));  
    
    
    TRUNCATE: delete all the rows from the table and free the space containing the table
    
        Syntax:
            TRUNCATE TABLE table_name;  

        Example:
            TRUNCATE TABLE EMPLOYEE;  

    
###############################
Data Manipulation Language(DML)
###############################

    INSERT: It is used to insert data into the row of a table
    
    Syntax:
            
            INSERT INTO TABLE_NAME    
            (col1, col2, col3,.... col N)  
            VALUES (value1, value2, value3, .... valueN); 
            
            (Or)
            
            INSERT INTO TABLE_NAME    
                VALUES (value1, value2, value3, .... valueN);     
    

            e.g) 
            INSERT INTO EMPLOYEE (Name, Dept) VALUES ("foo", "IT");  
    
    
    UPDATE: It is used to update or modify the value of a column in the table
        Syntax:
            UPDATE table_name SET [column_name1= value1,...column_nameN = valueN] [WHERE CONDITION]   
    
        e.g
            UPDATE students    
            SET name = 'foo'    
            WHERE Student_Id = '3'  
    
    DELETE: It is used to remove one or more row from a table.
        Syntax:
            DELETE FROM table_name [WHERE condition];  
    
############################
Data Control language(DCL)
#############################

    DCL commands are used to grant and take back authority from any database us

    Grant: It is used to give user access privileges to a database.

    e.g)
        GRANT SELECT, UPDATE ON MY_TABLE TO SOME_USER, ANOTHER_USER;  
    
    
    Revoke: It is used to take back permissions from the user.

    e.g)
        REVOKE SELECT, UPDATE ON MY_TABLE FROM USER1, USER2;  
        
#################################
Transaction Control Language(TCL)
#################################

    Commit: Commit command is used to save all the transactions to the database.

    Syntax: COMMIT;  
    Example:

        DELETE FROM CUSTOMERS  
        WHERE AGE = 25;  
        COMMIT;  


    Rollback: Rollback command is used to undo transactions that have not already been saved to the database.

    Syntax:ROLLBACK;  
        
    Example:
        DELETE FROM CUSTOMERS  
        WHERE AGE = 25;  
        ROLLBACK;  

    SAVEPOINT: It is used to roll the transaction back to a certain point without rolling back the entire transaction.

    Syntax: SAVEPOINT SAVEPOINT_NAME; 


##########################   
Data Query Language (DQL)
##########################

DQL is used to fetch the data from the database

    SELECT: This is the same as the projection operation of relational algebra. It is used to select the attribute based on the condition described by WHERE clause.

    Syntax:
        SELECT expressions    
        FROM TABLES    
        WHERE conditions;  
    
    E.g)
        SELECT name  
        FROM Student  
        WHERE cgpa > 7.5;  
        
        
-----------------------------------------        
Pre-requisite aka setting up environment:
----------------------------------------- 

step1. Install PostgreSQL from https://www.postgresql.org/download/

step2: Add postgresql install location to system environment variable "PATH"
in mac export PATH=$PATH:<pathToPostgreSQLOnMachine> 

e.g) export PATH=$PATH:/Users/foo/Documents/Postgresql/bin
  
step3:
    Run below commands one after other
    
    pip3 install --upgrade wheel
    pip3 install --upgrade setuptools
    pip3 install psycopg2 


step4: Initialize postgres
    Create a folder where 'postgres' user has read, write permission.This can be done by running 
    
    chown -R <yourusername> <path>
    e.g) chown -R vigneshv /Users/vigneshv/Documents/KnowledgeBase/Data
    
    now run
    pg_ctl -D /Users/vigneshv/Documents/KnowledgeBase/Data -U vigneshv initdb


step5: start postgres server by running below command inside terminal/command prompt
    syntax: pg_ctl -D <pathToPostgresDatabase> start
    
        /opt/homebrew/Cellar/postgresql/14.2_1/bin/pg_ctl -D /Users/vigneshv/Documents/KnowledgeBase/Data -l /Users/vigneshv/Documents/logfile start

    Note: 
        1. you may also use "which postgres" command to get the path to Postgres exectuable
        2. similarly to stop postgre server : pg_ctl -D /Users/vigneshv/Documents/Postgres/data/ stop 

    or
    
    In mac
        brew services restart postgresql

step6: launch postgresql command line terminal to create a database
    Run
        psql -d template1 

    Here "template1" is the default database in every installation
    
    now run
        CREATE DATABASE mock WITH OWNER vigneshv ENCODING 'UTF8';
    
    Here 'mock' is the name of the new database and 'vigneshv' is the owner
    
        To set password
            ALTER USER vigneshv PASSWORD 'newpwd'
    
    
step7: Create a schema and set it on the database we created
    1. switch to 'mock' database
        To connect a DB: \c <DB name> 
        i.e., \c mock
        
        Here semicolon indicates end of the command and it's mandatory
    
    2. Create a schema

        To get available schema
            SELECT nspname FROM pg_catalog.pg_namespace;
            
            or 
            
            \dn
            
        Either work with default schema 'public' or create one of your choice by using
        
        CREATE SCHEMA myschema;SET SCHEMA 'myschema'; \i mockDBSchema.sql 
            or
        \i mockDBSchema.sql   
    
'''

#psycopg2 is the driver for communicating to postgres from Python
import psycopg2
import time
import random
import string

dbname = "mock"
username = "vigneshv"
dbPassword = "password"
dbServerAddress = "127.0.0.1"
dbServerPort = 5432


def AddRecordsToDB():
    con = psycopg2.connect(database=dbname, user=username, password=dbPassword, host=dbServerAddress, port=dbServerPort)
    cursor = con.cursor()
    
    #numOfClass = 10
    #numOfStudentsPerClass = 20
    
    numOfClass = 2
    numOfStudentsPerClass = 2
    
    try:
        start_time = time.time()
        
        batch = ("2010-2013", "2010-2014", "2011-2014", "2011-2015", "2012-2015", "2012-2016")
        # Add records to 'Class' table
        for i in range(numOfClass):
            s = "INSERT INTO Class (id, batch) VALUES (" + str(i) + "," + "\'" + random.choice(batch) + "\'" + ");"
            # s= INSERT INTO Class (id, batch) VALUES (100, '2022-2025');
            cursor.execute(s)
        
        # Add students records
        numOfStudents = 0
        for i in range(numOfStudentsPerClass):
            for j in range(numOfStudentsPerClass):
                studentName = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = random.randint(4 , 15)))
                s = "INSERT INTO Student(id, name, age, classId) VALUES (" + str(numOfStudents) + "," + "\'" + studentName + "\'" + "," +  str(random.randint(18 , 25)) + "," + str(i) + ");"
                numOfStudents += 1
                cursor.execute(s)
                 
        con.commit()
    except psycopg2.DatabaseError as error:
        print(error)
    finally:
        print("Time elapsed in sec: %s" % (time.time() - start_time))
        cursor.close()
        if con:
            con.close()



def ReadFromDB():
    
    con = psycopg2.connect(database=dbname, user=username, password=dbPassword, host=dbServerAddress, port=dbServerPort)
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM Student JOIN Class ON Class.id=Student.classid WHERE Student.id=1")
        print("Records matched = ", cursor.rowcount)
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
            

AddRecordsToDB()
ReadFromDB()


 	