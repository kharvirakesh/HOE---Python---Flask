from flask import Flask
app = Flask(__name__)
 
stores = [
    {
        "name" : "My Store",
        "items" : [
            {
                "name" : "chair",
                "price" : 16
            }
        ]
    }
]
 
@app.get("/store")
def get_stores():
    return {"stores":stores}