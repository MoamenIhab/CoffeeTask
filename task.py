from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pymongo as pm

myclient = pm.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
mydb = myclient["coffeedb"]
print(dblist)
collist = mydb.list_collection_names()
print(collist)

if "coffee_Machines" not in collist:
    CFM = mydb["coffee_Machines"]
    cf_Machines = [
    { "Product": "CM001", "Product_Type": "COFFEE_MACHINE_SMALL", "Water_line": "False", "Model": "Base"},
    { "Product": "CM002", "Product_Type": "COFFEE_MACHINE_SMALL", "Water_line": "False", "Model": "Premium"},
    { "Product": "CM003", "Product_Type": "COFFEE_MACHINE_SMALL", "Water_line": "True", "Model": "Deluxe"},
    { "Product": "CM101", "Product_Type": "COFFEE_MACHINE_LARGE", "Water_line": "False", "Model": "Base"},
    { "Product": "CM102", "Product_Type": "COFFEE_MACHINE_LARGE", "Water_line": "True", "Model": "Premium"},
    { "Product": "CM103", "Product_Type": "COFFEE_MACHINE_LARGE", "Water_line": "True", "Model": "Deluxe"},
    { "Product": "EM001", "Product_Type": "ESPRESSO_MACHINE", "Water_line": "False", "Model": "Base"},
    { "Product": "EM002", "Product_Type": "ESPRESSO_MACHINE", "Water_line": "False", "Model": "Premium"},
    { "Product": "EM003", "Product_Type": "ESPRESSO_MACHINE", "Water_line": "True", "Model": "Deluxe"}
    ]
    x = CFM.insert_many(cf_Machines)
    print("Collection coffee machine created")
else:
    print("Collection already exist, continuing..")

if "coffee_pods" not in collist:
    CFP = mydb["coffee_pods"]
    cf_pods = [
    { "Product": "CP001", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "1"},
    { "Product": "CP003", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "3"},
    { "Product": "CP011", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "1"},
    { "Product": "CP013", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "3"},
    { "Product": "CP021", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_PSL", "pack_size_dozen": "1"},
    { "Product": "CP023", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_PSL", "pack_size_dozen": "3"},
    { "Product": "CP031", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_MOCHA", "pack_size_dozen": "1"},
    { "Product": "CP033", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_MOCHA", "pack_size_dozen": "3"},
    { "Product": "CP041", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_HAZELNUT", "pack_size_dozen": "1"},
    { "Product": "CP043", "Product_Type": "COFFEE_POD_SMALL", "flavor": "COFFEE_FLAVOR_HAZELNUT", "pack_size_dozen": "3"},
    { "Product": "CP101", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "1"},
    { "Product": "CP103", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "3"},
    { "Product": "CP111", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "1"},
    { "Product": "CP113", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "3"},
    { "Product": "CP121", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_PSL", "pack_size_dozen": "1"},
    { "Product": "CP123", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_PSL", "pack_size_dozen": "3"},
    { "Product": "CP131", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_MOCHA", "pack_size_dozen": "1"},
    { "Product": "CP133", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_MOCHA", "pack_size_dozen": "3"},
    { "Product": "CP141", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_HAZELNUT", "pack_size_dozen": "1"},
    { "Product": "CP143", "Product_Type": "COFFEE_POD_LARGE", "flavor": "COFFEE_FLAVOR_HAZELNUT", "pack_size_dozen": "3"},
    { "Product": "EP003", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "3"},
    { "Product": "EP005", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "5"},
    { "Product": "EP007", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_VANILLA", "pack_size_dozen": "7"},
    { "Product": "EP013", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "3"},
    { "Product": "EP015", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "5"},
    { "Product": "EP017", "Product_Type": "ESPRESSO_POD", "flavor": "COFFEE_FLAVOR_CARAMEL", "pack_size_dozen": "7"}
    ]
    y = CFP.insert_many(cf_pods)
    print("Collection coffee pods created")
else:
    print("Collection already exist, continuing..")





app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'coffeedb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/coffeedb'

mongo = PyMongo(app)

@app.route('/machines', methods= ['GET'])
def get_all_machines():
    cm = mongo.db.coffee_Machines

    output = []

    for k in cm.find():
        output.append({'product': k["Product"]})
    return jsonify({'result': output})

@app.route('/machines/productType:<ptype>,waterLine:<tf>', methods= ['GET'])
def get_filterd_machines(ptype, tf):
    cm = mongo.db.coffee_Machines
    output= []
    for j in cm.find():
        if j['Product_Type'] == ptype and j['Water_line'] == tf:
            output.append({'Product': j['Product']})

    return jsonify({'result': output})    

@app.route('/pods', methods= ['GET'])
def get_all_pods():
    cp = mongo.db.coffee_pods

    output = []

    for l in cp.find():
        output.append({'product': l["Product"]})
    return jsonify({'result': output})

@app.route('/pods/productType:<ptype>,flavor:<fv>,size:<sz>', methods= ['GET'])
def get_filterd_pods(ptype, fv, sz):
    cp = mongo.db.coffee_pods
    output= []
    for m in cp.find():
        if m['Product_Type'] == ptype and m['flavor'] == fv and m['pack_size_dozen'] == sz:
            output.append({'Product': m['Product']})

    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug= True)