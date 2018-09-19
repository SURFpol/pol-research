from urllib import unquote_plus
from cqlparser import parseString


def get_query(urlstring):
    """ Return query argument from logquery."""
    arglist = urlstring.split("&")
    for arg in arglist:
        if arg[0:6] == "query=":
            return unquote_plus(arg.split("=")[1])


def find_nodes(cql_node, search_type):
	""" Yields all nodes and its children of given type """
	if isinstance(cql_node, str):
		pass
	elif cql_node.name == search_type:
		yield cql_node
	else:
		for child in cql_node.children:
			for node in find_nodes(child, search_type):
				yield node



if __name__ == '__main__':
	
	line = "maximumRecords=50&operation=searchRetrieve&query=%22smaaklessen%22+and+lom.technical.format+exact+%22application%2Fx-Wikiwijs-Arrangement%22&recordPacking=xml&recordSchema=lom&sortKeys=lom.lifecycle.contribute.publisherdate%2C%2C1&startRecord=151&version=1.1&x-recordSchema=smbAggregatedData&x-recordSchema=meta"
	# >>>

	print(get_query(line))
	# >>> "smaaklessen" and lom.technical.format exact "application/x-Wikiwijs-Arrangement"

	cqlquery = parseString(get_query(line))
	# >>> CQL_QUERY(
	#     SCOPED_CLAUSE(
	#         SCOPED_CLAUSE(
	#             SEARCH_CLAUSE(
	#                 SEARCH_TERM(
	#                     TERM('smaaklessen')
	#                 )
	#             )
	#         ),
	#         BOOLEAN('and'),
	#         SEARCH_CLAUSE(
	#             INDEX(
	#                 TERM('lom.technical.format')
	#             ),
	#             RELATION(
	#                 COMPARITOR('exact')
	#             ),
	#             SEARCH_TERM(
	#                 TERM(
	#                     'application/x-Wikiwijs-Arrangement'
	#                 )
	#             )
	#         )
	#     )
	# )
