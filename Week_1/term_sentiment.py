import sys
import json

sentiments ={} 
Gword ={}
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
        	        calculate_sentiments(tweetsJson)
	        

def calculate_sentiments(tweet):
	text = tweet['text'].encode('utf-8')
	words = text.split()
	score = 0
	count_words = 0
	tweet_words = {}
	for word in words:
		if(word in sentiments):
			score = score + sentiments[word]
		else:
			count_words += 1
                	if word not in tweet_words:
				tweet_words[word] = 1
			else:
				tweet_words[word] += 1
	sentiment_word = score / count_words;
	for tword in tweet_words:
		if tword in Gword:
			Gword[tword] += sentiment_word
		else:
			Gword[tword] = sentiment_word		
	
def main():
	load_sentiment(sys.argv[1])
	process_file(sys.argv[2])
	for key in Gword.keys():
		print key +' '+ str(Gword[key])
if __name__ == '__main__':
	main()
