import pandas as pd
from flask import Flask, render_template, redirect, request, url_for

movieList = []

def getMoviesList(movies):
    moviesName = pd.read_csv('data/movies.csv')
    ratings_data = pd.read_csv('data/ratings.csv')
    df = pd.merge(ratings_data, moviesName, on='movieId')
    movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

    # 計算電影平均得分
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
    
    for i in ratings[ratings['number_of_ratings']>=70].index:
        movies.append(i)

def getSimliarMovie(movieName, num):
    print("User selected : " + movieName + ", num : " + str(num))
    # 最多只顯示30筆推薦結果
    if num > 30:
        num = 30

    # 匯入資料
    movies = pd.read_csv('data/movies.csv')
    ratings_data = pd.read_csv('data/ratings.csv')
    df = pd.merge(ratings_data, movies, on='movieId')
    movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
    # 計算電影相似度
    try:
        AFO_user_rating = movie_matrix[movieName]
    except KeyError:
        return []
    simliar_to_input = movie_matrix.corrwith(AFO_user_rating)

    # 計算電影平均得分
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['number_of_ratings'] = df.groupby('title')['rating'].count()

    # 製造新的df，以便接下來的判斷
    corr_AFO = pd.DataFrame(simliar_to_input, columns = ['Correlation'])
    corr_AFO.dropna(inplace = True)
    corr_AFO = corr_AFO.join(ratings['number_of_ratings'],how = 'left',lsuffix='_left', rsuffix='_right')
    corr_AFO = corr_AFO.join(ratings['rating'],how = 'left',lsuffix='_left', rsuffix='_right')
    sorted_movie = corr_AFO[corr_AFO['number_of_ratings']>=100].sort_values(by = 'Correlation',ascending = False).head(100) # 只取100筆評分超過100筆的電影

    avr = 0
    for row in sorted_movie['rating']:
        avr = avr + row
    avr = avr / 100

    # 刪去這100筆中評分較低的電影
    sorted_movie = sorted_movie[sorted_movie['rating']>=avr]
    count = 0
    movieList = []
    for index, row in sorted_movie.iterrows():
        if (count >= num): # 只顯示使用者要求的筆數
            break
        if (index != movieName):
            count = count + 1
            movieList.append({'index': index, 
                            'Correlation': round(row["Correlation"]*1000)/10, 
                            'number_of_ratings': int(row["number_of_ratings"]), 
                            'rating': round(row["rating"]*100)/100})
    return movieList

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", movieNames=movies)

@app.route('/getSimliarMovie', methods=['GET', 'POST'])
def getMovie():
    if request.method == 'POST':
        movieList = getSimliarMovie(request.values['movieName'], int(request.values['moviewNum']))
        if (movieList == []):
            return 'movie name error'
        else:
            return render_template("simliarMovie.html", movies=movieList, choose=request.values['movieName'], num=int(request.values['moviewNum']))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    getMoviesList(movieList)
    app.run(debug=True, host='0.0.0.0')