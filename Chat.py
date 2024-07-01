from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    qu=data['queryResult']['queryText']
    num1=data['queryResult']['parameters']['number1']
    num2=data['queryResult']['parameters']['number2']
    op=data['queryResult']['parameters']['Operation']
    req=data['queryResult']['parameters']['Request']

    if len(op)!=1:
        res='Not trained yet for such op!'

    else:
        op = op[0]
        if op=='abort' or num1=='abort' or num2=='abort':
            res='Alright! Ping me if you need any further assistance.'
        else:
            try:
                if op=='addition':
                    res=num1+num2
                elif op=='substraction':
                    res=num1-num2
                elif op=='multiplication':
                    res=num1*num2
                elif op=='division':
                    res=num1/num2
                else:
                    res='Operation unknown to me.'
            except:
                res="Didn't understand! Please repeat your problem from the begining."

    if op not in ['addition','substraction','multiplication','division']:
        response = {
            'fulfillmentText': "{}".format(res)
        }
    else:
        if len(req)>0:
            response = {
                'fulfillmentText': "Sure. {} is your answer.".format(res)
            }
        else:
            response = {
                'fulfillmentText': "{}".format(res)
            }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)