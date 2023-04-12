# vim-gpt-comment-reflow

A Vim/Neovim plugin that uses GPT-3.5 to rewrite documentation and comments to stay within a character limit and generate missing docstrings for Python functions.

## Installation

1. Install the plugin using a plugin manager, e.g., [vim-plug](https://github.com/junegunn/vim-plug). Add the following line to your `init.vim` or `.vimrc`:

```vim
Plug 'autholykos/vim-gpt-comment-reflow'
```

2. Run :PlugInstall in Vim or Neovim to install the plugin.
3. Install the required Python package:

```bash
pip install requests pynvim
```

## Configuration

1. Add your LLM API key and desired maximum line length to your init.vim or .vimrc. Use environment variables to avoid exposing sensitive information:
```vim
let $GPT_COMMENT_REFLOW_API_KEY = "your_api_key_here"
let g:gpt_comment_reflow_api = "your_api_url_here"
let g:gpt_comment_reflow_max_line_length = 80
```
2. Replace `your_api_key_here` with your actual API key and `your_api_url_here` with the url to the LLM APIs you intend to use (it defaults to [GPT-3.5](https://api.openai.com/v1/engines/davinci-codex/completions))

## Usage

To reflow comments and generate missing docstrings in a Python file, run the following command in Vim or Neovim:

```vim
:GPTCommentReflow
```
