from airflow.sdk import dag, task
from pendulum import datetime
import subprocess

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="5 9 * * *",
    catchup=False,
)
def extracao_api():

    @task
    def run_script():
        subprocess.run(
            ["python", "/usr/local/airflow/include/extracao_api/main.py"],
            check=True
        )

    run_script()

dag = extracao_api()