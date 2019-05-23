from flask import Flask, render_template
from data import shoes_collection
from bson.objectid import ObjectId
app = Flask(__name__)


@app.route('/')
def index():
    allshoes = shoes_collection.find()
    return render_template('index.html',allshoes = allshoes)

@app.route('/products')
def products():
    allshoes = shoes_collection.find()
    return render_template('products.html',allshoes = allshoes)

@app.route('/products/single/<id>')
def single(id):
    detail_shoes = shoes_collection.find_one({"_id" : ObjectId(id)})
    
    print(detail_shoes)
    return render_template('single.html',detail_shoes=detail_shoes)

@app.route('/products/filter/<type>')
def detail8(type):
    shoes_list =[]
    filter_shoes = shoes_collection.find()
    for shoes in filter_shoes:
        if type in shoes['detail1']:
            shoes_list.append(shoes)
            print(shoes)
    return render_template('filter.html',shoes_list=shoes_list)

@app.route('/products/delete/<id>')
def delete (id):
    detail_shoes = shoes_collection.find_one({"_id":ObjectId(id)})
    detail_shoes= shoes_collection.delete_one(detail_shoes)
    return render_template('products.html',detail_shoes=detail_shoes)
    
if __name__ == '__main__':
 app.run(debug=True)
 