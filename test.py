from org.apache.hadoop.hbase import HBaseConfiguration
from org.apache.hadoop.hbase.client import HTable, Get
from org.apache.hadoop.hbase.util import Bytes


conf = HBaseConfiguration.create()
table = HTable(conf, "test")
get = Get(Bytes.toBytes('row1'))
result = table.get(get)
value = result.getValue(Bytes.toBytes('cf'), Bytes.toBytes('col1'))
print Bytes.toString(value, 0, len(value))
