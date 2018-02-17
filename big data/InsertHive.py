import hiver
from django.core.files.temp import NamedTemporaryFile

def _hql(self, hql):
    client = hiver.connect(settings.HIVE_HOST, settings.HIVE_PORT)
    try:
        client.execute(hql)
    finally:
        client.shutdown()

def insert(self, table_name, rows):
    ''' cannot insert single rows via hive, need to save to a temp file and bulk load that '''
    csv_file = NamedTemporaryFile(delete=True)
    for row in rows:
        map_repr = '|'.join('%s:%s' % (key, value) for key, value in row[1].items())
        csv_file.write(row[0] + "," + map_repr + "\n")
    csv_file.flush()
    try:
        _hql('DROP TABLE IF EXISTS %s' % table_name)
        _hql("""
            CREATE TABLE
                %s (
                    key string,
                    map<string, int>
                )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            COLLECTION ITEMS TERMINATED BY '|'
            MAP KEYS TERMINATED BY ':'
        """ % (table_name))
        _hql("""
            LOAD DATA LOCAL INPATH '%s' INTO TABLE %s
        """ % (csv_file.name, table_name)
    finally:
        csv_file.close()


_hql(10.120.193.3, 10000) ;

insert('test_table', [
  ('c4ca4-0000001-79879483-000000000124', {'comments': 1, 'likes': 2}),
  ('c4ca4-0000001-79879483-000000000124', {'comments': 1, 'likes': 2}),
  ('c4ca4-0000001-79879496-000000000124', {'comments': 1, 'likes': 2}),
  ('b4aed-0000002-79879783-000000000768', {'comments': 1, 'likes': 2}),
  ('b4aed-0000002-79879783-000000000768', {'comments': 1, 'likes': 2}),
])
