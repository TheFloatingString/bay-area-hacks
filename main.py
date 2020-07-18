import hug

@hug.get("/job_search")
def search(employee_id, hours):
	"""Get endpoint to search for jobs"""
	return f"{id:{employee_id}, hours:{hours}}"

@hug.post("/employee_register")
def employee_register(body):
	"""Post endpoint for employee registration"""
	# return f"name:{name}, email:{email}, skills:{skills}"
	# print(body)
	return body

@hug.post("/job_post")
def job_post(employer_id, skills, pay_rate, hours):
	return f"employer_id:{employer_id}, skills:{skills}, pay_rate:{pay_rate}, hours:{hours}"

@hug.get("/", output=hug.output_format.html)
def employee_form():
	f = open("templates/employee-form.html")
	html_content = f.read()
	return html_content
