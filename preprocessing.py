import re
import docx2txt
import textract

filename = 'test.doc'
output = 'test.txt'


if '.doc' in filename:
    text = textract.process(filename)
    text = text.decode("utf-8")
    text = text.replace('|', '')
    text = re.sub(r'\s+$', '', text, flags=re.MULTILINE)  # remove spacing from the right
    text = re.sub(r"^\s{2}(.+)$", '', text, flags=re.MULTILINE)  # remove spacing from the right

if '.docx' in filename:
    text = docx2txt.process(filename)

pattern = r"(?m)^\s*$\n?"  # remove redundant empty lines
text = re.sub(pattern, "", text)

with open(output, 'w') as f:
    f.write(text)

print('Done')
