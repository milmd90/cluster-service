from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask("cluster-service")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def hello():
    return "Hello world!"

@app.route("/recommend/<saleCode>")
@cross_origin()
def recommend(saleCode):
    return jsonify({
      "products": [
        {
          "id": "1",
          "name": "this product",
          "img": "https://images-na.ssl-images-amazon.com/images/I/61OLLS-CDoL._UX679_.jpg",
          "brand": "nike",
          "price": 200
        }, {
          "id": "2",
          "name": "that product",
          "img": "https://res.cloudinary.com/teepublic/image/private/s---eJtvOOE--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_470/c_crop,g_north_west,h_626,w_470,x_0,y_-72/g_north_west,u_upload:v1462829015:production:blanks:mtl53ofohwq5goqjo9ke,x_-395,y_-397/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1507413937/production/designs/1955718_1.jpg",
          "brand": "bike",
          "price": 300
        }, {
          "id": "1",
          "name": "this product",
          "img": "https://images-na.ssl-images-amazon.com/images/I/61OLLS-CDoL._UX679_.jpg",
          "brand": "nike",
          "price": 200
        }, {
          "id": "2",
          "name": "that product",
          "img": "https://res.cloudinary.com/teepublic/image/private/s---eJtvOOE--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_470/c_crop,g_north_west,h_626,w_470,x_0,y_-72/g_north_west,u_upload:v1462829015:production:blanks:mtl53ofohwq5goqjo9ke,x_-395,y_-397/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1507413937/production/designs/1955718_1.jpg",
          "brand": "bike",
          "price": 300
        }, {
          "id": "1",
          "name": "this product",
          "img": "https://images-na.ssl-images-amazon.com/images/I/61OLLS-CDoL._UX679_.jpg",
          "brand": "nike",
          "price": 200
        }, {
          "id": "2",
          "name": "that product",
          "img": "https://res.cloudinary.com/teepublic/image/private/s---eJtvOOE--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_470/c_crop,g_north_west,h_626,w_470,x_0,y_-72/g_north_west,u_upload:v1462829015:production:blanks:mtl53ofohwq5goqjo9ke,x_-395,y_-397/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1507413937/production/designs/1955718_1.jpg",
          "brand": "bike",
          "price": 300
        }, {
          "id": "1",
          "name": "this product",
          "img": "https://images-na.ssl-images-amazon.com/images/I/61OLLS-CDoL._UX679_.jpg",
          "brand": "nike",
          "price": 200
        }, {
          "id": "2",
          "name": "that product",
          "img": "https://res.cloudinary.com/teepublic/image/private/s---eJtvOOE--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,w_470/c_crop,g_north_west,h_626,w_470,x_0,y_-72/g_north_west,u_upload:v1462829015:production:blanks:mtl53ofohwq5goqjo9ke,x_-395,y_-397/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1507413937/production/designs/1955718_1.jpg",
          "brand": "bike",
          "price": 300
        }
      ]
    })
