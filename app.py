from flask import Flask,request
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

@app.post("/store")
def create_store():
    request_data = request.get_json()