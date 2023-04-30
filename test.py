import re
import docx2txt

# replace 'example.docx' with the actual name of your file
text = docx2txt.process('test.doc')

pattern = r"(?m)^\s*$\n?"  # remove redundant lines
text = re.sub(pattern, "", text)

# write the extracted text to a new file
with open('test.txt', 'w') as f:
    f.write(text)
