import crowdlib as cl
import crowdlib_settings


class incentivePayment(object):
	"""docstring for multiPayment"""
	def __init__(self, hit_id, bonus):
		super(incentivePayment, self).__init__()
		self.hit_id = hit_id
		self.bonus = bonus
		self.gold_standard = gold_standard
	
	def answerRight(self):
		return 
	def answerWrong(self):
		return 
	def payWorker(assignment_id) 
		return


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
	bonus = 0.1
	gold_question = [1, 3, 4]
	hit_id = ""
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
			# no bonus
		else:
			g_bonus = pow(2, right) * bonus
			asg.grant_bonus(g_bonus, "Great job")


if __name__ == "__main__":
	main()	