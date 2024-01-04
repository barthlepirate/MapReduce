# # This function is not intended to be invoked directly. Instead it will be
# # triggered by an orchestrator function.
# # Before running this sample, please:
# # - create a Durable orchestration function
# # - create a Durable HTTP starter function
# # - add azure-functions-durable to requirements.txt
# # - run pip install -r requirements.txt

# import logging


# # def main(name: str) -> str:
#     return f"Hello {name}!"
def main(mapperlist: list) -> dict:
    output_dict = {}
    
    for sub_list in mapperlist:
        for word, count in sub_list:
            output_dict.setdefault(word, []).append(count)
    
    return output_dict


