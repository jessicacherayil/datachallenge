import csvreader
import plotly.plotly as py
import plotly.graph_objs as go


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
	    barmode='stack'
	)

	fig = go.Figure(data=data, layout=layout)
	py.iplot(fig, filename='posts-votes-stacked')


def main():
    ranks = [i for i in range(1,25)]
    posts = [903, 767, 619, 524, 483, 457, 383, 369, 311, 277, 269, 262, 259, 255, 192, 185, 181, 180, 179, 165, 164, 160, 149, 146, 142]
    votes = [11634, 7574, 7539, 4609, 4307, 4067, 4028, 3695, 3523, 3241, 3044, 2990, 2809, 2694, 2688, 2547, 2545, 2346, 2255, 2252, 2250, 2242, 2230, 2122, 2080]
    #makePlotPost(ranks, posts)
    makePlotVote(ranks, votes)


if __name__=='__main__':
    main()