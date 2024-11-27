# import tiktoken


def read(src:str):
    with open(src, "r") as file:
        content = file.read().strip()
    return content


# def partition(content:str, token_limit:int=400, enc:str="o200k_base"):
#     blocks = content.split("\n\n")
#     encoding = tiktoken.get_encoding(enc)

#     chunks = [[]]
#     curr_idx = 0
#     curr_token_count = 0

#     for block in blocks:
#         token_count = len(encoding.encode(block))
#         chunks[curr_idx].append(block)
#         curr_token_count += token_count

#         if curr_token_count > token_limit:
#             chunks.append([])
#             curr_idx += 1
#             curr_token_count = 0

#     return chunks
