# Practice: read values from nested messages and API-style data.

response = {
    "model": "example-model",
    "messages": [
        {"role": "user", "content": "Summarize this."},
        {"role": "assistant", "content": "Here is the summary."},
    ],
    "usage": {"prompt_tokens": 12, "completion_tokens": 8},
}


def assistant_message(api_response):
    messages = api_response["messages"]
    for message in messages:
        if message["role"] == "assistant":
            return message["content"]
    return None


def total_tokens(api_response):
    usage = api_response["usage"]
    return usage["prompt_tokens"] + usage["completion_tokens"]


print(assistant_message(response))
print(total_tokens(response))
