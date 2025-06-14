# data-engg-projects
Contains Data Engineering related projects
Skills to demonstrate:
1) Python
2) Airflow
3) Snowflake
4) DBT
5) PySpark
6) S3 bucket
7) API
8) EC2
9) Docker

To Run python script as a Github Action, you need to define an actions.yml file
You can create an action in github with the following yaml configuration
1) Checkout Repo content
2) setup python
3) install python packages
4) execute main.py
   
- Python scripts can be run using Github
  1) So if you want to run a python program in github, you can setup and use a github workflow

- DAG needs to run on a cloud
  1) So if you want to run a DAG, you need a cloud.
  2) If you want to refer to any particular python code/script, you need to pass the script file in the same cloud as that of DAG. Then you can use a PythonOperator
  3) Another method is to create a container image using docker. Now this globally unique container image can be referred inside the DAG with the help of a kubernetes_pod_operator
