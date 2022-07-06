import json


def hello(event, context):
   body = {
       "message": "Go Serverless v1.0!",
       "input": event
   }

   response = {
       "statusCode": 200,
       "body": json.dumps(body)
   }

   return response

def __prod(ls):
    result = 1
    for n in ls:
        result *= n
    return result

def __calculate(calc):
    plus = calc.split("+")
    if(len(plus)>1):
        return sum([int(n) for n in plus])
    minus = calc.split("-")
    if(len(minus)>1):
        return int(minus[0])-sum(int(n) for n in minus[1:])
    div = calc.split("/")
    if(len(div)>1):
        return int(div[0])/__prod(int(n) for n in div[1:])
    mult = calc.split("*")
    if(len(mult)>1):
        return __prod(int(n) for n in mult)
    raise Exception("Could not recognize calculation")

def calculator(event, context):
    # TODO implement
    calc = json.loads(event["body"])["calculation"]
    calc = calc.replace(" ","")
    
    
    try:
        result = __calculate(calc)
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except:
        return {
            'statusCode': 400,
            'body': json.dumps("Calculation bad formatted")
        }
    

