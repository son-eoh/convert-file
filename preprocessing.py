import re
import docx2txt
import textract

# Change this to test different files
end = 'doc'

filename = f'sample.{end}'
output = f'result-{end}.txt'


if '.doc' in filename:
    text = textract.process(filename)
    text = text.decode("utf-8")
    text = text.replace('|', '')
    text = re.sub(r'\s+$', '', text, flags=re.MULTILINE)  # remove spacing from right
    text = re.sub(r' {2,}', ' ', text)  # replace all space > 2 with 1 space


if '.docx' in filename:
    text = docx2txt.process(filename)

text = re.sub(r"(?m)^\s*$\n?", "", text)  # remove redundant empty lines
text = "\n".join([line.lstrip() for line in text.split("\n")])  # remove spacing from left

with open(output, 'w') as f:
    f.write(text)

print(f'Done, check file: {output}')
