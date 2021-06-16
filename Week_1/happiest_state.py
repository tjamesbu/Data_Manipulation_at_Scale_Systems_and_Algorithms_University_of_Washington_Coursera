import sys
import json

sentiments ={}
state_sentiments={}
state_tweets={} 
def load_sentiment(fl):
	afinnfile = open(fl)
	for line in afinnfile:
		term, score  = line.split("\t")
		sentiments[term] = int(score)
	

def process_file(fl):
	tweets = open(fl);
	for line in tweets:
     		tweetsJson = json.loads(line)
		value = 0
		if 'text' in tweetsJson and 'place' in tweetsJson:
        	        calculate_sentiments(tweetsJson)
	state_avg = {}        
	for state in state_sentiments.keys():
		state_avg[state] = state_sentiments[state]/float(state_tweets[state])
	for key, value in sorted(state_avg.iteritems(), key=lambda (k,v): (v,k),reverse=True):
   		print key
		break
def calculate_sentiments(tweet):
	
	try:
		text = tweet['text'].encode('utf-8')
		country = tweet['place']['country_code']
		state = tweet['place']['full_name']
		state = state.split(', ')[1]

	except (KeyError, IndexError, TypeError):
		return None
	if country != 'US' or len(state) != 2:
		return None

	words = text.split()
	score = 0
	for word in words:
		if(word in sentiments):
			score = score + sentiments[word]
	if state in state_sentiments:
		state_sentiments[state]+= score
		state_tweets[state]+= 1
	else:
		state_sentiments[state]= score
		state_tweets[state] = 1	

	  
def main():
	load_sentiment(sys.argv[1])
	process_file(sys.argv[2])
	
if __name__ == '__main__':
	main()
