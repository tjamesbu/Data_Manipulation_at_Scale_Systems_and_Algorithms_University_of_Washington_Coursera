import sys
import json

count_words=0 
Gword ={}
def process_file(fl):
	tweets = open(fl);
	for line in tweets:
     		tweetsJson = json.loads(line)
		if 'text' in tweetsJson:
        	        calculate_sentiments(tweetsJson)
	        

def calculate_sentiments(tweet):
	text = tweet['text'].encode('utf-8')
	words = text.split()
	global count_words
	for word in words:
		count_words += 1
                if word not in Gword:
			Gword[word] = 1
		else:
			Gword[word] += 1
def main():
	process_file(sys.argv[1])
	for key in Gword.keys():
		value = Gword[key]/float(count_words)
		tr = "%.9f" % value
		print key +' '+ str(tr)
if __name__ == '__main__':
	main()
