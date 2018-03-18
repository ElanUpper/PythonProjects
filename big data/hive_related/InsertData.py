from sqlalchemy.engine import create_engine
from pyhive import hive
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

sql = "select * from log where concat_ws('-',year,month,day) between 2017-09-13 and 2017-09-19"

db = create_engine(
    'hive://p64_u500_wangyang37:Share@power@10.120.193.3:10000/cdl',
    connect_args={
        'auth': 'LDAP',
        'configuration': {
            'mapreduce.job.queuename': 'queue'
        }
    },
    echo=True
)
resultProxy=db.execute(sql)
data = resultProxy.fetchall()