
s = '''
Binary(M)	M	类似Char的二进制存储，特点是插入定长不足补0
VarBinary(M)	M	类似VarChar的变长二进制存储，特点是定长不补0
Tiny Text	Max:255	大小写不敏感
Text	Max:64K	大小写不敏感
Medium Text	Max:16M	大小写不敏感
Long Text	Max:4G	大小写不敏感
TinyBlob	Max:255	大小写敏感
Blob	Max:64K	大小写敏感
MediumBlob	Max:16M	大小写敏感
LongBlob	Max:4G	大小写敏感
Enum	1或2	最大可达65535个不同的枚举值
Set	可达8	最大可达64个不同的值
Geometry	 	 
Point	 	 
LineString	 	 
Polygon	 	 
MultiPoint	 	 
MultiLineString	 	 
MultiPolygon	 	 
GeometryCollection
'''

lines = s.split("\n")
for line in lines:
	print("<p>{}</p>".format(line))