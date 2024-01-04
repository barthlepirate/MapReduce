
import logging
import json

import azure.functions as func
import azure.durable_functions as df

def custom_orchestrator(context: df.DurableOrchestrationContext):
    # Retrieve a list of N work items for parallel processing
    fetched_data = yield context.call_activity("fetcher", "")
    print(fetched_data)

    combined_results = {}
    for data_item in fetched_data.items():
        combined_mapped_lines = []
        map_tasks = []
        for line_item in data_item[1]:
            for line_number, line_content in line_item.items():
                map_tasks.append((line_number, line_content))
        for task in map_tasks:
            map_result = yield context.call_activity("Mapper", task)
            combined_mapped_lines.append(map_result)
        shuffled_data = yield context.call_activity("Shuffler", combined_mapped_lines)
        reducer_tasks = []
        for shuffled_item in shuffled_data.items():
            reducer_tasks.append(context.call_activity("Reducer", shuffled_item))
        reducer_results = yield context.task_all(reducer_tasks)
        combined_results[data_item[0]] = reducer_results
    
    return combined_results

main = df.Orchestrator.create(custom_orchestrator)
