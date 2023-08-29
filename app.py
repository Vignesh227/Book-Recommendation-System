''' Python file to connect HTML using Flask '''

import os
from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd 

app=Flask(__name__)

# Read 'pivot' dataframe
pivot = pickle.load(open('pivot.pkl', 'rb'))

# Read 'similarity_scores' dataframe
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# Read 'books' dataframe
books = pickle.load(open('books.pkl', 'rb'))

# Convert the 'Book-Title' column values as a list
pivotcsv = pd.read_csv('Pivot.csv')
book_titles = pivotcsv['Book-Title'].tolist()


# Render Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Render recommendation page
@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html', titles=book_titles)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':

        bookName = request.form['bookName']
        
        # Returns the index os the book in pivot df
        index = np.where(pivot.index == bookName)[0][0]
        
        # Find similarity scores for each book
        # Sort the recommmended books in Desc order  
        recommended_books = sorted(list(enumerate(similarity_scores[index])),
                                key=lambda x:x[1], reverse=True)
        
        # Pick the top 5 recommended books
        recommended_books = recommended_books[1:6]
        
        # to store 5 records
        data = []
        
        for idx in recommended_books:
            item = []
            # print(pivot.index[idx[0]])
            temp_df = books[books['Book-Title'] == pivot.index[idx[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        
        print(data)
        return render_template('recommendation.html', movies = data, titles=book_titles)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
