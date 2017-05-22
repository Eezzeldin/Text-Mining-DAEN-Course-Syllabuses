#https://blog.nycdatascience.com/student-works/web-scraping/glassdoor-web-scraping/

##############################################################################
def get_match(cv,jDict):
    '''Use the Jaccard similarity measure to choose the best match for a CV'''

    # Parse cv according to predifined categories
    new_cv = skills_info(cv)

    # Flatten, filter and update the dict
#    score =  map(lambda (x,y): [x, jDict[x][2], jDict[x][3], Jaccard(new_cv,y)],
#                 map(lambda (x,y): (x, skills_info([y[0]]+y[5])), jDict.items()))
    score =  map(lambda (x,y): [jDict[x][2], jDict[x][3], jDict[x][1],
                 Jaccard(new_cv,y[5]), jDict[x][4]],jDict.items())


    best = pd.DataFrame(score, columns=['Company','Location','Rating','Similarity','Link'])\
             .sort_values(ascending = False, by='Similarity')

    return best

##############################################################################


def Jaccard(x,y):
    """returns the jaccard similarity between two lists """

    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))

    return intersection_cardinality/float(union_cardinality)
