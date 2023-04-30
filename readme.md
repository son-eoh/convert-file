# Convert-file

### Description
.doc, .docx to text

### Quick start
```
docker build -t convert .
docker run -it -v /Users/macbookpro/app/convert-file/:/app convert bash
python preprocessing.py
```

NOTE:
- docker run -it -v /absolute-path/convert-file/:/app convert bash
- Change the `end` variable to `doc` or `docx`

