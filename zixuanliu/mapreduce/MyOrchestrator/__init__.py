# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    lines = yield context.call_activity("GetInputDataFn", "")
    
    map_task = []
    for line in lines:
        map_task.append(context.call_activity("Mapper", line))

    words  = yield context.task_all(map_task)
    
    words_count = yield context.call_activity("shuffler", words)

    reduce_task = []
    for word_count in words_count:
        reduce_task.append(context.call_activity("Reducer", word_count))
    
    result = yield context.task_all(reduce_task)
    print(result)

    return result

main = df.Orchestrator.create(orchestrator_function)