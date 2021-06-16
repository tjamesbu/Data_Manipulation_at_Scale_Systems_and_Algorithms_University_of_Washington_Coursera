import sys
import json

sentiments ={} 
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
		if 'text' in tweetsJson:
        	        value = calculate_sentiments(tweetsJson)
	        print value

def calculate_sentiments(tweet):
	text = tweet['text'].encode('utf-8')
	words = text.split()
	score = 0
	for word in words:
		if(word in sentiments):
			score = score + sentiments[word]
	return score  
def main():
	load_sentiment(sys.argv[1])
	process_file(sys.argv[2])
if __name__ == '__main__':
	main()
