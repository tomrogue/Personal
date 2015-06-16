import time
import praw

r = praw.Reddit('PRAW related-question monitor by /u/_Daimon_ v 1.0. ',
				'Url: https://praw.readthedocs.org/en/latest/',
				'pages/writing_a_bot.html')
r.login()
already_done = []

while True:
	subreddit = r.get_subreddit('learnpython')

	for submission in subreddit.get_hot(limit=10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text)
	
	if submission.id not in already_done and has_praw:
		msg = '[PRAW related thread](%s)' % submission.short_link
		r.send_message('_Daimon_', 'PRAW thread', msg)
		already_done.append(submission.id)
	
	time.sleep(1800)