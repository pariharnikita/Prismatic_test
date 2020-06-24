import sys
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/api')
def read_file_content():
	try:
		filename = request.args.get('filename','file1')+".txt"
		start_line_no = int(request.args.get('start_line_no', 0))
		end_line_no = int(request.args.get('end_line_no', 0))
		
		with open(filename, encoding='cp437') as f:
			results = f.readlines()
			if start_line_no and end_line_no:
				results = results[start_line_no:end_line_no+1]
		return render_template('template.html', results=results)
	except OSError as e:
		return jsonify({'Error message':str(e)})




app.run(debug=True)

#http://127.0.0.1:5000/api?filename=file2&start_line_no=11&end_line_no=20
