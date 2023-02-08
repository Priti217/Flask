from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index1.html")

@app.route("/demo",methods=['POST'])
def items():
    if (request.method=='POST'):
        itemname=request.json['itemname']
        #itemcost=int(request.json['itemcost'])
        quantity=int(request.json['quantity'])
        result = itemcost*quantity
        if result<=1000:
            total= result*0.1
            Total=result-total
        elif 1000<result<=2000:
            total= result*0.2
            Total=result-total
        elif result>2000:
            total= result*0.3
            Total=result-total

    return f"The total price {Total}"

@app.route("/abc",methods=['POST'])
def abcd():
    if (request.method=='POST'):
        itemname=request.form['itemname']
        #itemcost=int(request.form['itemcost'])
        quantity=request.form['quantity']
        l={"Phonecover":200,"T-shirt":500,"schoolbag":1000,"Radio":2000,"Headphone":2000,
           "Laptopbag":1500,"Table and chair":2000,"Mobilestand":500,"sunglasses":500,"Blanket":1000}
        l1 = {"1":1,"2":2,"3":3,"4":4,"5":5}
        if (itemname in l) and (quantity in l1):
            result = l.get(itemname) * l1.get(quantity)
            if result<=1000:
                total= result * 0.1
                Total=result-total
            elif 1000<result<=2000:
                total= result *0.2
                Total=result-total
            elif result>2000:
                total= result * 0.3
                Total=result-total

            return render_template("result1.html" ,result=Total)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

