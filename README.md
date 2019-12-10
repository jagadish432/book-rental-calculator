# Python-Flask Book Rental Calculator
This is a simple book rental calculator app

### To install the dependencies and run the application
For steps to run the application, please refer to [this file](steps.md)

### Initial DB creation
As this project is using a sqlite database, we need to create a file which can be used as storage for our database

1 Create a file for database with the environment specific database name
```bash
source envs/dev
touch db/$DATABASE_NAME
``` 

2 

a. Initialize the migrations folder for database related changes and information.

b. run the migrate command to generate the migration script contains DB schema(for First time) and changes in schema(from Second time onwards)

```bash
python migrate.py db init
python migrate.py db migrate
```
c. Make any required changes in the generated migration script and run the following command
```bash
python migrate.py db upgrade
```


### Unittests

The **tests** folder contains unittest files.

Run the following command to run all the files in this **test** folder
```bash
coverage run -m unittest discover -s tests/ -p 'test_*.py'
```

To see the report generated over the run command, run the following command
```bash
coverage report
```
