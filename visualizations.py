import csvreader
import plotly.plotly as py
import plotly.graph_objs as go
import squarify
import csv

def makePlotPost(xlist, ylist):


	data = [go.Bar(
	            x=xlist,
	            y=ylist
	    )]

	layout = go.Layout(
         title='Popularity vs. Number of Posts',
         xaxis = dict(
            title = 'Popularity Rank'
            ),
        yaxis=dict(
            title = 'Number of Posts'
            ),
        )

	fig = go.Figure(data=data, layout=layout)
	plot_url = py.plot(fig, filename='numPosts')

def makePlotVote(xlist,ylist):
	data = [go.Bar(
	            x=xlist,
	            y=ylist,
	    )]

	layout = go.Layout(
         title='Popularity vs. Number of Votes',
         xaxis = dict(
            title = 'Popularity Rank'
            ),
        yaxis=dict(
            title = 'Number of Votes'
            ),
        )

	fig = go.Figure(data=data, layout=layout)
	plot_url = py.plot(fig, filename='numVotes')

def stackedBarPlot(xlist, y_post, y_vote):
	trace1 = go.Bar(
   		x=xlist,
    	y=y_post,
	    name='Posts'
	)

	trace2 = go.Bar(
	    x=xlist,
	    y=y_vote,
	    name='Votes'
	)

	data = [trace1, trace2]
	layout = go.Layout(
		title = 'Posts and Votes for Top 25 Users',
		xaxis = dict(
			title = 'Popularity Rank'
			),
	    barmode='stack'
	)

	fig = go.Figure(data=data, layout=layout)
	py.plot(fig, filename='posts-votes-stacked')

def getRealPopulars(userfile):
	#{userID: followers+posts+votes}

    userDict = {} #Format is user: followerCount
    with open(userfile,'rb') as csvfile:
        userReader = csv.reader(csvfile)
        firstline = True 
        for row in userReader:
            if firstline:    #skip first line
                firstline = False
                continue
                
            if row[7] != '' and row[7][0] != '_' and row[9] != '' and row[9][0] != '_' and row[10] != '' and row[10][0] != '_' : #ignore null entries
                if 'http' not in row[7] and 'http' not in row[9] and 'http' not in row[10]:
                	#print row[7]
                	userDict[(row[0])] = (int(row[7]) + int(row[9]) + int(row[10]))
            
    allUsers = sorted(userDict, key=userDict.__getitem__, reverse = True) #sort by follower count
    print allUsers[0:5]

    allValues = []
    for user in allUsers:
    	allValues.append(userDict[user])




    return allUsers[0:25], allValues[0:25]


def treeMap():
	x = 0.
	y = 0.
	width = 100.
	height = 100.

	topUsers, topValues = getRealPopulars('users--2016-04-01_14-36-26-UTC.csv')


	values = topValues

	normed = squarify.normalize_sizes(values, width, height)
	rects = squarify.squarify(normed, x, y, width, height)

	# Choose colors from http://colorbrewer2.org/ under "Export"
	color_brewer = ['rgb(250,128,114)', 'rgb(127,255,212)', 'rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)','rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)','rgb(253,191,111)','rgb(255,127,0)','rgb(202,178,214)','rgb(106,61,154)','rgb(255,255,153)','rgb(177,89,40)', 'rgb(255,0,0)', 'rgb(0,255,0)', 'rgb(255,255,0)', 'rgb(0,255,255)', 'rgb(255,0,255)', 'rgb(128,128,128)', 'rgb(128,0,128)', 'rgb(0,128,128)', 'rgb(139,69,19)', 'rgb(112,128,144)', 'rgb(255,228,181)']
	
	shapes = []
	annotations = []
	counter = 0

	for r in rects:
	    shapes.append(
	        dict(
	            type = 'rect',
	            x0 = r['x'],
	            y0 = r['y'],
	            x1 = r['x']+r['dx'],
	            y1 = r['y']+r['dy'],
	            line = dict( width = 2 ),
	            fillcolor = color_brewer[counter]
	        )
	    )
	    annotations.append(
	        dict(
	            x = r['x']+(r['dx']/2),
	            y = r['y']+(r['dy']/2),
	            text = values[counter],
	            showarrow = False
	        )
	    )
	    counter = counter + 1
	    if counter >= len(color_brewer):
	        counter = 0

	# For hover text
	trace0 = go.Scatter(
	    x = [ r['x']+(r['dx']/2) for r in rects ],
	    y = [ r['y']+(r['dy']/2) for r in rects ],
	    text = [ str(v) for v in values ],
	    mode = 'text',
	)

	layout = dict(
		title = 'True Popularities',
	    height=700,
	    width=700,
	    xaxis=dict(showgrid=False,zeroline=False),
	    yaxis=dict(showgrid=False,zeroline=False),
	    shapes=shapes,
	    annotations=annotations,
	    hovermode='closest'
	)

	# With hovertext
	figure = dict(data=[trace0], layout=layout)

	# Without hovertext
	# figure = dict(data=[Scatter()], layout=layout)

	py.plot(figure, filename='squarify-treemap')


def main():
    ranks = [i for i in range(1,500)]
    posts = [0, 0, 0, 0, 0, 14, 0, 6, 0, 0, 0, 2, 9, 6, 0, 0, 30, 524, 0, 0, 2, 6, 26, 11, 0, 1, 31, 4, 0, 0, 1, 0, 6, 2, 0, 13, 0, 0, 0, 0, 0, 2, 0, 0, 0, 17, 0, 0, 0, 15, 0, 0, 18, 619, 22, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 259, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 11, 8, 4, 0, 0, 2, 17, 4, 0, 0, 0, 10, 0, 2, 0, 0, 0, 0, 0, 4, 277, 8, 1, 9, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 1, 10, 0, 14, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 0, 0, 0, 6, 22, 0, 110, 0, 0, 0, 0, 0, 0, 0, 1, 7, 1, 0, 0, 9, 3, 0, 0, 262, 0, 0, 2, 0, 7, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 767, 0, 16, 0, 0, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 6, 37, 2, 0, 0, 0, 4, 0, 0, 52, 0, 3, 0, 0, 0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 13, 0, 13, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 57, 0, 0, 0, 0, 0, 0, 71, 75, 0, 0, 0, 1, 0, 0, 6, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 12, 0, 0, 0, 0, 0, 5, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 5, 0, 15, 0, 1, 1, 7, 1, 31, 0, 0, 0, 0, 3, 0, 0, 0, 0, 50, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 56, 0, 0, 0, 0, 0, 3, 23, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 903, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 114, 0, 1, 20, 1, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 1, 1, 1, 3, 0, 0, 4, 0, 20, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 4, 0, 0, 0, 3, 0, 15, 0, 0, 0, 0, 0, 5, 0, 0, 30, 0, 8, 0, 0, 3, 0, 0, 0, 0, 0, 40, 0, 1, 0, 0, 1, 0, 0]
    votes = [0, 0, 0, 82, 1, 111, 0, 35, 43, 0, 6, 13, 16, 13, 0, 0, 42, 7574, 0, 2, 5, 7, 35, 12, 0, 9, 201, 65, 7, 51, 12, 0, 590, 3, 1, 65, 8, 0, 4, 2, 0, 11, 1, 1, 2, 74, 0, 0, 4, 156, 1, 0, 46, 2688, 166, 1, 22, 0, 2, 1, 3, 23, 12, 21, 2, 1, 812, 446, 2, 4, 26, 4, 0, 8, 24, 4, 1, 0, 111, 15, 4, 8, 0, 26, 213, 33, 0, 16, 0, 59, 42, 14, 8, 0, 9, 8, 2, 9, 4609, 125, 6, 237, 1, 1, 7, 3, 75, 1, 1, 2, 1, 0, 1, 31, 182, 1, 2545, 11, 1, 3, 65, 3, 2, 2, 5, 0, 3, 2, 0, 4, 0, 2, 1, 2, 1, 13, 6, 38, 1, 109, 5, 179, 117, 4, 1385, 2, 0, 1, 5, 712, 4, 19, 10, 72, 8, 0, 0, 60, 6, 1, 1, 1738, 1, 4, 7, 2, 10, 1, 62, 0, 13, 31, 0, 21, 549, 0, 0, 1, 1, 10, 2, 58, 16, 2, 2, 1, 0, 4, 1, 2, 6, 0, 3, 0, 1333, 2, 251, 1, 1, 10, 0, 1, 1, 4, 49, 2, 0, 0, 0, 3, 12, 4, 23, 0, 1, 3, 34, 66, 0, 208, 3, 1, 0, 5, 1, 8, 25, 13, 309, 20, 1, 29, 1, 44, 1, 1, 111, 1, 9, 1, 1, 0, 24, 1, 247, 1, 28, 1, 2, 2, 5, 91, 1, 342, 0, 0, 3, 1, 10, 63, 6, 0, 12, 22, 0, 7, 6, 1, 323, 47, 20, 5, 1, 10, 3, 429, 761, 3, 1, 1, 69, 1, 2, 208, 8, 1, 1, 4, 32, 0, 0, 0, 1, 11, 4, 0, 1, 24, 97, 14, 1, 7, 10, 2, 85, 0, 2, 40, 48, 1, 0, 9, 7, 473, 1, 2, 2, 10, 14, 38, 1, 270, 0, 302, 7, 7, 153, 49, 16, 1236, 1, 1, 21, 10, 11, 3, 1, 1, 1, 1632, 9, 3, 10, 4, 3, 8, 0, 3, 1, 0, 287, 1, 24, 7, 4, 0, 60, 47, 10, 27, 0, 2, 4, 1, 5, 4, 1, 10, 65, 1737, 7, 11, 2, 2, 6, 16, 1, 6, 4, 0, 2809, 27, 7, 352, 1, 1, 4, 2, 4, 6, 2, 221, 107, 2, 1, 6, 23, 4, 1, 1, 11, 4, 7, 81, 2, 7, 4, 1, 369, 4, 6, 3, 0, 13, 3, 122, 14, 0, 1, 1, 21, 2, 78, 0, 0, 1, 1, 2, 12, 24, 3, 17, 4, 0, 1, 8, 11, 1, 1, 3, 1, 4, 4, 0, 20, 413, 13, 6, 2, 18, 47, 8, 3, 3, 1, 0, 0, 4, 0, 1, 7, 0, 6, 34, 3, 42, 58, 2, 0, 1, 18, 1, 171, 3, 1, 20, 423, 70, 329, 2, 0, 167, 2, 146, 1, 0, 107, 0, 1, 0, 1, 1, 357, 0, 12, 2, 2, 6, 4, 1]
    #makePlotPost(ranks, posts)
    #makePlotVote(ranks, votes)
    #stackedBarPlot(ranks, posts, votes)
    treeMap()


if __name__=='__main__':
    main()