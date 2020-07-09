# Project: Data Modeling with Postgres


## Prerequisite:
**Download and Install** Python 3.8.3: https://www.python.org/downloads/release/python-383/
**Add Python to Environment Variables:**
  Step 1: Right click on computer or PC and go to "Properties"
  Step 2: Click "Environment Variables"
  Step 3: Under "System Variables" click on "Path"
  Step 4: Define you Python path by clicking "Add" (Ex: 
  C:\Users\Garav Soni\AppData\Local\Programs\Python\Python38\Scripts
  C:\Users\Garav Soni\AppData\Local\Programs\Python\Python38\)
  Step5: Your Python will now be accessible by IDE
**Download and install Visual Code Studio:** https://code.visualstudio.com/download
**Download and install PIP:** Go to "https://pip.pypa.io/en/stable/installing/" to look at the full documentation on the installation process
**Download and install Postgressql :** https://www.postgresql.org/download/

**Use the command to "pip install pycodestyle" to install Pycodestyle which checks for PIP guidelines.**
## How to run:
**Remember to use the repective username and password for the Localhost (edit that to the etl.py file)**

```sh
$ python sql_queries.py
```
```sh
$ python etl.py
```


![Untitled](https://user-images.githubusercontent.com/33581900/86535701-23a8ad80-beb0-11ea-95cb-6d51fb901132.png)

## Summary of Project:
**This is the first project for the Udacity Data Engineering NanoDegree. In this project, you have to use your knowledge of
on data modeling with Postgres and build an EFL Pipeline using Python. We have to define face and dimension tables for a star schema. In addition,
we have ETF pipeline that transfers data from the Song and Log files into Postgres using Python and Postgres. The first project handles data from the app Sparkify. The data is JSON format**

## Steps to do the Project:
1. The first step to this project is to create the Fact table and dimension tables with the respective properties for each using the "Create" query in the sql_queries.py file.
2. The next step is to "Insert", so that we can prepare to insert the data from the log data file and song data file in the sql_queries.py file. 
3. The final step is to create a "SELECT" query to select the accurate song.
4. After we have finished creating the queries in the sql_queries.py, then we have to go to the etl.py. (Note: Use the 
5. In the etl.py file, we have to extract the data from the log and song files. The etl.py file is used for for processing the data and add it to the repective tables in the schema with the queries inside of sql_queries.py

