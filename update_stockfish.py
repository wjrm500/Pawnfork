import re
import sys

models_filepath = sys.argv[1]

old_code = r'stderr=subprocess.STDOUT,[\n\r\s]*\)'
new_code = r'stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)'

with open(models_filepath, 'r+') as file:
    source_code = file.read()
    new_source_code = re.sub(old_code, new_code, source_code)
    file.seek(0)
    file.write(new_source_code)
    file.truncate()