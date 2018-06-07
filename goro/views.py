from django.shortcuts import render
from articles.models import Article
from goro.models import Page
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def index(request):

	p = Page.objects.get(name__iexact='home')

	all_article_contents = [x["headline"] + " " + x["content"] for x in Article.objects.values("content", "headline")]
	english_stops = set(stopwords.words("english"))
	tokenizer = RegexpTokenizer("[\w]+")
	token_counts = {}
	for article in all_article_contents:
		tokens = tokenizer.tokenize(" ".join(filter(lambda x: reduce(
			lambda x, y: x and y, map(
				lambda x: x,
				[
					x[0:1] != ' ',
					x[0:2] != "..",
					x[0:1] != '+',
					x[0:1] != '-',
					x[0:1] != '~',
					x[0:1] != '=',
					x[0:2] != "::",
					x[0:1] != ''
				])
		), article.split('\r\n'))))
		tokens = [t for t in tokens if t not in english_stops]
		token_counts_map =  map(lambda x: (x, 1), tokens)
		for x in token_counts_map:
			if(token_counts.get(x[0])):
				token_counts[x[0]] = token_counts[x[0]] + x[1]
			else:
				token_counts[x[0]] = 1

	word_counts = sorted(token_counts.iteritems(), key=lambda x: x[1], reverse=True)

	context = {
		"page": p,
        "word_counts": word_counts[:10]
	}

	return render(request, 'goro/index.html', context)
