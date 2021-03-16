# For the benefit of all beings.

from datauri import DataURI
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os
import time
from urllib.parse import urlparse
import threading


app = Flask(__name__)
cors = CORS(app)

someoneDrawing = False
drawingIndexFile = 'drawingIndex.txt'
timeLeft = 30.0

@cross_origin()
@app.route('/register')
def register():
	name = request.args.get('name')
	email = request.args.get('email')
	if someoneDrawing:
		return {
			'error': 'Sorry! Someone is drawing right now. Please wait a bit.',
		}
	else:
		index = getIndex()
		saveUser(name, email, index)
		return {
			'index': index,
			'drawNumber': userMapping[index],
			'timeLeft': timeLeft,
			# acgtual time left
		}


# store images as hash to store all (index_hash)

# reset counter when it hits the end
def getIndex():
	if someoneDrawing:
		return None
	try:
		with open(drawingIndexFile, 'r') as f:
			index = int(f.read().strip())
			return index
	except Exception:
		return 1


def saveUser(name, email, index=None):
	global someoneDrawing
	if index:
		someoneDrawing = True
		threading.Timer(timeLeft, timeout).start()
	else:
		index = 'busy'
	with open('drawers.txt', 'a')as f:
		# Add other index
		# strip out commas
		f.write(f'{name},{email},{index},{time.ctime()}\n')
	return ''


def timeout():
	global someoneDrawing
	someoneDrawing = False


@cross_origin()
@app.route('/submit', methods=['POST'])
def submit():
	global someoneDrawing
	someoneDrawing = False
	json = request.get_json()
	index = json['index']
	print(index)
	pngUri = DataURI(json['pngData'])
	print(pngUri.is_base64)
	pngContent = pngUri.data
	writeImage(pngContent, index)
	nextDrawer(index)
	return 'Success'

def nextDrawer(index):
	nextIndex = int(index) + 1
	with open(drawingIndexFile, 'w') as f:
		f.write(f'{nextIndex}')

def writeImage(pngContent, userIndex):
	imageIndex = userMapping[int(userIndex)]
	filename = f'static/image{imageIndex}.png'
	with open(filename, 'wb') as png:
		png.write(pngContent)

# @cross_origin()
# @app.route('/login', methods=['POST'])
# def login():
# 	userData = urlparse(request.get_json())
# 	print(userData)
# 	return 'Success'
# 	#with open('static/1.png', wb) as pngWrite:


userMapping = {
	1: 120,
2: 121,
3: 137,
4: 136,
5: 135,
6: 119,
7: 103,
8: 104,
9: 105,
10: 106,
11: 122,
12: 138,
13: 154,
14: 153,
15: 152,
16: 151,
17: 150,
18: 134,
19: 118,
20: 102,
21: 86,
22: 87,
23: 88,
24: 89,
25: 90,
26: 91,
27: 107,
28: 123,
29: 139,
30: 155,
31: 171,
32: 170,
33: 169,
34: 168,
35: 167,
36: 166,
37: 165,
38: 149,
39: 133,
40: 117,
41: 101,
42: 85,
43: 69,
44: 70,
45: 71,
46: 72,
47: 73,
48: 74,
49: 75,
50: 76,
51: 92,
52: 108,
53: 124,
54: 140,
55: 156,
56: 172,
57: 188,
58: 187,
59: 186,
60: 185,
61: 184,
62: 183,
63: 182,
64: 181,
65: 180,
66: 164,
67: 148,
68: 132,
69: 116,
70: 100,
71: 84,
72: 68,
73: 52,
74: 53,
75: 54,
76: 55,
77: 56,
78: 57,
79: 58,
80: 59,
81: 60,
82: 61,
83: 77,
84: 93,
85: 109,
86: 125,
87: 141,
88: 157,
89: 173,
90: 189,
91: 205,
92: 204,
93: 203,
94: 202,
95: 201,
96: 200,
97: 199,
98: 198,
99: 197,
100: 196,
101: 195,
102: 179,
103: 163,
104: 147,
105: 131,
106: 115,
107: 99,
108: 83,
109: 67,
110: 51,
111: 35,
112: 36,
113: 37,
114: 38,
115: 39,
116: 40,
117: 41,
118: 42,
119: 43,
120: 44,
121: 45,
122: 46,
123: 62,
124: 78,
125: 94,
126: 110,
127: 126,
128: 142,
129: 158,
130: 174,
131: 190,
132: 206,
133: 222,
134: 221,
135: 220,
136: 219,
137: 218,
138: 217,
139: 216,
140: 215,
141: 214,
142: 213,
143: 212,
144: 211,
145: 210,
146: 194,
147: 178,
148: 162,
149: 146,
150: 130,
151: 114,
152: 98,
153: 82,
154: 66,
155: 50,
156: 34,
157: 18,
158: 19,
159: 20,
160: 21,
161: 22,
162: 23,
163: 24,
164: 25,
165: 26,
166: 27,
167: 28,
168: 29,
169: 30,
170: 31,
171: 47,
172: 63,
173: 79,
174: 95,
175: 111,
176: 127,
177: 143,
178: 159,
179: 175,
180: 191,
181: 207,
182: 223,
183: 239,
184: 238,
185: 237,
186: 236,
187: 235,
188: 234,
189: 233,
190: 232,
191: 231,
192: 230,
193: 229,
194: 228,
195: 227,
196: 226,
197: 225,
198: 209,
199: 193,
200: 177,
201: 161,
202: 145,
203: 129,
204: 113,
205: 97,
206: 81,
207: 65,
208: 49,
209: 33,
210: 17,
211: 1,
212: 2,
213: 3,
214: 4,
215: 5,
216: 6,
217: 7,
218: 8,
219: 9,
220: 10,
221: 11,
222: 12,
223: 13,
224: 14,
225: 15,
226: 16,
227: 32,
228: 48,
229: 64,
230: 80,
231: 96,
232: 112,
233: 128,
234: 144,
235: 160,
236: 176,
237: 192,
238: 208,
239: 224,
240: 240,
241: 256,
242: 255,
243: 254,
244: 253,
245: 252,
246: 251,
247: 250,
248: 249,
249: 248,
250: 247,
251: 246,
252: 245,
253: 244,
254: 243,
255: 242,
256: 241,
}