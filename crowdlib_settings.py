from crowdlib import settings as cls

from secret import AWS_KEY, AWS_ID

cls.aws_account_id = AWS_ID
cls.aws_account_key = AWS_KEY

cls.service_type="production"

cls.default_autopay_delay   = 60*60*24
cls.default_reward          = 0.01
cls.default_lifetime        = 60*60*24*7
cls.default_max_assignments = 1
cls.default_time_limit      = 60*30
cls.default_qualification_requirements = ()
cls.default_requester_annotation = ""
