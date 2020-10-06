from flask import Flask

app = Flask(__name__)

@app.route('/<int:num>')
def all(num):
	ret = ""
	for x in range(num):
		ret += str(x+1) + " "
	return ret

@app.route('/<int:num>/odd')
def odd(num):
	ret = ""
	for x in range(num):
		if (x + 1) % 2 == 1:
			ret += str(x+1) + " "
	return ret

@app.route('/<int:num>/even')
def even(num):
	ret = ""
	for x in range(num):
		if (x + 1) % 2 == 0:
			ret += str(x+1) + " "
	return ret

@app.route('/<int:num>/prime')	
def prime(num):
	ret = ""
	arr = [0] * (num+1)
	for x in range(2, num+1):
		if arr[x] == 0:
			ret += str(x) + " "
		for i in range(2, num+1):
			if i * x > num:
				break
			arr[i * x] = 1;
	return ret
