from __future__ import absolute_import, print_function

from pprint import pprint
from collections import Counter
import spacy
from cqlparser import parseString

from readers import get_query, find_nodes



if __name__ == '__main__':

	nlp = spacy.load('nl_core_news_sm')
	searches = []

	with open('../data/edurep/2018-05-03-queries.txt') as query_log:
		for line in query_log.readlines():

			raw_query = get_query(line)
			if not raw_query or raw_query.startswith('meta.upload.id'):
				continue

			query = parseString(raw_query)
			for term in find_nodes(query, 'TERM'):
				words = [word for word in term.children[0].split(' ') if word in nlp.vocab]
				if not len(words):
					continue
				search = u' '.join(words)
				if search.isnumeric():
					continue
				searches.append(search)

		search_counter = Counter(searches)
		for term, freq in search_counter.most_common()[:20]:
			print(term, freq)
