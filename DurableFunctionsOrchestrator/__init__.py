# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    tasks = []
    task_inputs = ["Tokio", "London", "Paris"]
    for task_input in task_inputs:
        tasks.append(context.call_activity("ActivityFunction", task_input))
    result = yield context.task_all(tasks)
    return result


main = df.Orchestrator.create(orchestrator_function)
