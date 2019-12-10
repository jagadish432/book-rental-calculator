

## steps to run this application

1. cd <your_project_directory_root>

2. python -m virtualenv venv

3. source venv/Scripts/activate

4. python -m pip install -r requirements.txt

5. source envs/dev ("dev" for "development" environment, "prod" for "production" environment)

6. python app.py


## update requirements.txt
If you've installed any other packages apart from requirements.txt then update your requirements.txt file by
```bash
run "python -m pip freeze>requirements.txt"
```


