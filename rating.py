from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store book ratings
book_ratings = {}

# Dictionary to store book comments
book_comments = {}


@app.route('/book/rating', methods=['POST'])
def create_book_rating():
    rating = float(request.json['rating']) / 2
    user_id = int(request.json['user_id'])
    book_id = int(request.json['book_id'])

    # Create a new rating entry for the book
    if book_id not in book_ratings:
        book_ratings[book_id] = []

    book_ratings[book_id].append({'user_id': user_id, 'rating': rating})

    return jsonify({'message': 'Rating added successfully'})


@app.route('/book/comment', methods=['POST'])
def create_book_comment():
    comment = request.json['comment']
    user_id = int(request.json['user_id'])
    book_id = int(request.json['book_id'])

    # Create a new comment entry for the book
    if book_id not in book_comments:
        book_comments[book_id] = []

    book_comments[book_id].append({'user_id': user_id, 'comment': comment})

    return jsonify({'message': 'Comment added successfully'})


@app.route('/book/comments', methods=['GET'])
def get_book_comments():
    book_id = int(request.args.get('book_id'))

    # Return the list of comments for the book
    if book_id in book_comments:
        return jsonify(book_comments[book_id])

    return jsonify([])


@app.route('/book/rating/average', methods=['GET'])
def get_book_rating_average():
    book_id = int(request.args.get('book_id'))

    # Calculate the average rating for the book
    if book_id in book_ratings:
        ratings = book_ratings[book_id]
        if len(ratings) > 0:
            average_rating = sum([rating['rating'] for rating in ratings]) / len(ratings)
            return jsonify({'average_rating': round(average_rating * 2, 2)})

    return jsonify({'average_rating': 0})


if __name__ == '__main__':
    app.run(debug=True)
