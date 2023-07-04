import chardet

file_path = 'test.log'

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
encoding = result["encoding"]
confidence = result["confidence"]

print(encoding)  # Windows-1254
print(confidence)
# po zwiększeniu próbki działa
# utf-8
# 0.99
print(raw_data.decode(encoding=encoding))