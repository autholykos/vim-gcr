try:
    import requests
except ImportError:
    raise ImportError(
        "The 'requests' library is required for vim-gpt-comment-reflow. "
        "Please install it using 'pip install requests'."
    )

import vim


def add_docstrings(api, api_key, text, max_line_length):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "prompt": f"""Generate docstrings for the following Python code:\n{text}\n
Make sure every line has maximum {max_line_length} characters.""",
        "max_tokens": 100,
        "n": 1,
        "temperature": 0.5,
    }
    response = requests.post(
        api,
        headers=headers,
        json=data,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()


def reflow_comment(api, api_key, text, max_line_length):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "prompt": f"""Rewrite the following comment to fit within {max_line_length}
 characters per line:\n{text}\n""",
        "max_tokens": 100,
        "n": 1,
        "temperature": 0.5,
    }
    response = requests.post(
        api,
        headers=headers,
        json=data,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()


def main():
    api_key = vim.eval("g:gpt_comment_reflow_api_key")
    llm_api = vim.eval("g:gpt_comment_reflow_api")
    if llm_api is None:
        llm_api = "https://api.openai.com/v1/engines/davinci-codex/completions"
    max_line_length = int(vim.eval("g:gpt_comment_reflow_max_line_length"))

    text = "\n".join(vim.current.buffer[:])
    text_with_docstrings = add_docstrings(llm_api, api_key, text, max_line_length)

    new_text = reflow_comment(llm_api, api_key, text_with_docstrings, max_line_length)

    if new_text:
        vim.current.buffer[:] = new_text.split("\n")


if __name__ == "__main__":
    main()
