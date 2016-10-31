import crowdlib as cl
import crowdlib_settings
import sqlite3
import json


class incentivePayment(object):
	"""docstring for multiPayment"""
	def __init__(self, hit_id, bonus):
		super(incentivePayment, self).__init__()
		self.hit_id = hit_id
		self.bonus = bonus
		self.gold_standard = gold_standard
	
	def answerRight(self):
		pass 
	def answerWrong(self):
		pass 
	def payWorker(assignment_id): 
		pass

def list_to_dict(list):
	return_dict = {}
	for i, v in enumerate(list):
		return_dict[i] = v
	return return_dict

def strip_text(string):
	string = str(string)
	return string.strip("task")

def main():
	gold_standard = ['B', 'C', 'A', 'C', 'A', 'D', 'D', 'B', 'B', 'C', 'B', 'D', 'B', 'B', 'D', 'C', 'C', 'D', 'A', 'B']
	gold_dict = list_to_dict(gold_standard)
	bonus = 0.05
	gold_question = [1, 3, 4]
	hit_id = "3UYRNV2KITEILMJVJ6IQ5XK57048N7"
	hit = cl.get_hit(hit_id)
	asgs = hit.assignments
	for asg in asgs:
		answer_result = {}
		answers = asg.answers	
		for answer in answers:
			question_id = int(strip_text(answer.question_id))
			free_text = answer.free_text
			if str(free_text) == gold_dict[question_id]:
				answer_result[question_id] = True
			else:
				answer_result[question_id] = False			
		right = 0
		wrong = 0
		for gold in gold_question:
			if answer_result[gold] == True:
				right += 1
			elif answer_result[gold] == False:
				wrong +=1
		if wrong > 0:
			pass
		else:
			g_bonus = pow(2, right) * bonus
#			asg.grant_bonus(g_bonus, "Great job")
		
		conn = sqlite3.connect("data.db")
		db = conn.cursor()
		answer_result = json.dumps(answer_result)
		db.execute("insert into result(results, time_spent, task_type) values(?,?,?)", (answer_result,str(asg.time_spent), 'con'))
		conn.commit()
		conn.close()

if __name__ == "__main__":
	main()	
