from datetime import datetime
from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
import uuid
from airflow.operators.postgres_operator import PostgresOperator
from airflow import settings
from airflow.models import Connection


dag_params = {
    'dag_id': 'PostgresOperator_dag',
    'start_date': datetime(2019, 10, 7),
    'schedule_interval': None
}

with DAG(**dag_params) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgresql',
        sql='''CREATE TABLE IF NOT EXISTS user_table(
            id integer NOT NULL, email VARCHAR, active BOOLEAN
            );''',
    )
    insert_row = PostgresOperator(
        task_id='insert_row',
        postgres_conn_id='postgresql',
        sql='INSERT INTO user_table VALUES(%s, %s, %s)',
        trigger_rule=TriggerRule.ALL_DONE,
        parameters=(uuid.uuid4().int % 123456789,
                    'felix_airflow@works.com', True)
    )

