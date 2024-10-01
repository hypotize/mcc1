from flask import Flask, render_template, request
import csv
app = Flask(__name__)

items = []

@app.route('/')
def index():
	for item in items:
		item['result'] = 0
		item['selected'] = ''
	return render_template('index.html', items=items)

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		cnt = 0
		for item in items:
			if item['id'] in request.form:
				answer = request.form[item['id']]
				if answer == item['answer']:
					item['result'] = 1
					cnt += 1
				else:
					item['result'] = -1
				item['selected'] = answer
			else:
				item['result'] = -2
				item['selected'] = ''
		return render_template('index.html', items=items, answer=str(len(items))+'問中'+str(cnt)+'問正解')
	else:
		for item in items:
			item['result'] = -2
			item['selected'] = ''
		return render_template('index.html', items=items, answer='解答が入力されていません。')

if __name__=='__main__':
	with open('data.csv', encoding='utf_8') as f:
		reader = csv.reader(f)
		for id, row in enumerate(reader):
			item = dict()
			item['id'] = 'Q'+str(id)
			item['question'] = row[0]
			item['choices'] = row[1:-1]
			item['result'] = 0
			item['answer'] = row[-1]
			item['selected'] = ''
			items.append(item)
	app.debug = False
	app.run(host="0.0.0.0")
