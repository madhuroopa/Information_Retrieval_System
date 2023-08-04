import boto3
import termify

#  Lambda-specific code for search engine
#  Convention is the handler is named lambda_handler and the file is named lambda_function.py


###############################################
#  Entry point is a function search(line) where line is the 
#    input query.  Output is a sequence of the form (docname, relevance) of 
#    length at most 5, and sorted in descending order of relevance


#  Step 1 -- Make connections to the two dynamodb tables
dynamodb = boto3.resource('dynamodb')
tfidf_table = dynamodb.Table('tfidf')
docid_table = dynamodb.Table('doctitles')
###################################################
#  These three functions do the dynamodb lookups.  
#  There is code missing for all three.

# get_docids_for_terms
# Input is a sequence of terms.  Output is a set of docids -- the set of 
#  all docids that contain one or more of the terms

def get_docids_for_terms(terms):
    docids = set()
    for term in terms:
        #  Make dynamodb call to get all docids for that term, and add them to the set
        response = tfidf_table.query(
            KeyConditionExpression='term = :term',
            ExpressionAttributeValues={
                ':term': term
            },
            ProjectionExpression='docid'
        )
        # Add the docids to the set
        for item in response['Items']:
            docids.add(item['docid'])
    return docids
# get_tfidf
#  Input is a term and docid, output is the stored TF-IDF value for
#  that pair, or 0.0 if there is no stored value

def get_tfidf(term, docid):
    response = tfidf_table.get_item(
        Key={
            'term': term,
            'docid': docid
        },
        ProjectionExpression='tfidf'
    )
    # If there is no stored value, return 0.0
    if 'Item' not in response:
        return 0.0
    return response['Item']['tfidf']
    
# get_doc_title
#   Input is a docid, output is the stored name (title) for the document as stored in Dynamodb, or None if 
#     there is no such entry

def get_doc_title(docid):
   response = docid_table.get_item(
        Key={
            'docid': docid
        },
        ProjectionExpression='title'
    )
   # If there is no such entry, return None
   if 'Item' not in response:
        return None
   return response['Item']['title']
##########################################################

def search(line):
    terms = termify.termify(line)
    docids = get_docids_for_terms(terms)
    return sort_and_limit([(docid, compute_doc_relevance(docid, terms)) for docid in docids])

##  Implements the formula for relevance specified in the assignment -- output is a float.
##    Should return 0.0 if the terms list is empty or none of the terms appear in the document   

def compute_doc_relevance(docid, terms):
    relevance = 0.0
    for term in terms:
        tfidf = get_tfidf(term, docid)
        tfidf_val=float(tfidf)
        if tfidf_val > 0:
            relevance += tfidf_val
    if len(terms) > 0:
        relevance /= len(terms)
    return relevance
## Input pairs are (docid, tfidf)
##    Sort in descending order of tfidf, choose the top five, 
##    retrieve the doc title, and truncate tfidf to an integer
##    Output is a list of at most 5 pairs of the form (docname, int-tfidf)
def sort_and_limit(pairs):
    pairs.sort(key=lambda x: x[1], reverse=True)
    pairs = pairs[:5]
    result = []
    for pair in pairs:
        docid, relevance = pair
        docname = get_doc_title(docid)
        if docname is not None:
            relevance = int(relevance)
            result.append((docname, relevance))
    return result

def lambda_handler(event, context):
    query = event['queryStringParameters']['query']
    items = search(query)
    print(items)
    return format_html_query_results(query, items)

# format_html_query_response -- format output from the fcall to search to pretty HTML.
#   Inputs are
#   * the original query string, unedited
#   * a sequence of pairs of the form (docname, int-relevance) in proper order to be rendered


def format_html_query_results(query, items):
    html = f"<html><body><h1>{format_banner_html(query,items)}{format_item_html(items)}</body></html>"    
    return {'statusCode': 200, 'headers': {'Content-Type': 'text/html'},'body': html}

# Produce HTML with banner information, like the query string
def format_banner_html(query, items):
    banner_html = f"<h3>Relevant books for the query : {query} <br/></h3><p/>"
    return banner_html

# Produce HTML with formatted version of the items    
def format_item_html(items): 
    item_html = '<ol>'
    for item in items:
        item_html += f"<li>{item[0]} -- {item[1]}</li>"
    item_html += '</ol>'
    return item_html
    



