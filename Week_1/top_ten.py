import sys
import json


hashtags={}

def process_file(fl):
	tweets = open(fl);
	for line in tweets:
     		tweetsJson = json.loads(line)
		calculate_sentiments(tweetsJson)
	count = 0
	for key, value in sorted(hashtags.iteritems(), key=lambda (k,v): (v,k),reverse=True):
   		print "%s %s" % (key, value)
		count+=1
		if count == 10:
			break

def calculate_sentiments(tweet):

	try:
		hashtag = tweet['entities']['hashtags']

	except (KeyError, IndexError, TypeError):
		return None


	for tag in hashtag:
		text = tag['text'].encode("utf-8")
		if text in hashtags:
			hashtags[text] += 1
		else:
			hashtags[text] = 1


def main():
	process_file(sys.argv[1])

if __name__ == '__main__':
	main()
