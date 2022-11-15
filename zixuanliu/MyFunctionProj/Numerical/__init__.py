import logging
import math
import azure.functions as func

def BlackBoxFunction(x):
    return abs(math.sin(x))

def NumericalIntegration(lower, upper, N):
    integral = 0
    lower = float(lower)
    upper = float(upper)
    dx = (upper-lower)/N
    for i in range(N):
        xip12 = lower+(i+1/2)*dx
        dI = BlackBoxFunction(xip12)*dx
        integral += dI
    return "  "+str(integral)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        lower_upper = name.split("_")
        N = [10, 100, 1000, 10**4, 10**5, 10**6, 10**7]
        output = ""
        for n in N:
            output += NumericalIntegration(lower_upper[0],lower_upper[1], n)
        return func.HttpResponse(output)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
