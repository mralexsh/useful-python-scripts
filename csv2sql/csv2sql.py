import sys
from functools import reduce

def make_correct_header(h):
  return h.strip().replace(" ", "_").lower()

def pg_str(v):
  coma = ', '
  res = '('
  res = reduce(lambda p, c: p + "\'" + c + "\'" + coma, v, res)
  return res.rstrip(coma) + '),\n'

def ora_str(v):
  coma = ', '
  res = ' VALUES('
  res = reduce(lambda p, c: p + "\'" + c + "\'" + coma, v, res)
  return res.rstrip(coma) + ')\n'

def value_str(values, delimiter, make_correct_value_str, preffix_str = ''):
  res = list(filter(lambda i: i != '', values))
  res = list(map(lambda i: make_correct_value_str(i.split(delimiter)), res))
  res = reduce(lambda p, c: p + preffix_str  + c, res, '')
  return res.rstrip(',\n')


def header_str(first_line, delimiter):
  header = list(map(make_correct_header, first_line.split(delimiter)))
  return reduce(lambda p, c: p + c + ', ', header, '(').rstrip(', ') + ')'

def pg_query(csv_content, delimiter, table_name):
  values_content = value_str(csv_content[1:], delimiter, pg_str) + ';'
  return 'INSERT INTO ' + table_name + ' ' + header_str(csv_content[0], delimiter) + '\nVALUES ' + values_content


def ora_query(csv, delimiter, table_name):
  values_content = value_str(csv[1:], delimiter, ora_str, '  INTO ' + table_name + ' ' +  header_str(csv[0], delimiter)) + '\n'
  return 'INSERT ALL\n' + values_content + 'SELECT 1 FROM DUAL;'

def make_insert_query(file_name, sql_dialect = "MY_SQL", delimiter = ";"):
  f = open(file_name, "r", encoding='utf-8-sig')
  csv = f.read()
  f.close()
  table_name = file_name.removesuffix('.csv')
  if sql_dialect == 'ORA':
    return ora_query(csv.split('\n'), delimiter, table_name)
  else:
    return pg_query(csv.split('\n'), delimiter, table_name)
  
def main(argv):
  if len(argv) == 0:
    print("Error: Missing input file")
  else:
    print(make_insert_query(*argv))
    
if (__name__ == '__main__'):
  main(sys.argv[1:])
