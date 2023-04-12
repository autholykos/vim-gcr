function! GPTCommentReflow()
    if &filetype != 'python'
        echo "vim-gpt-comment-reflow only supports Python files."
        return
    endif

    let s:python_code = join([
        \ 'import sys',
        \ 'import os',
        \ 'import vim',
        \ '',
        \ 'plugin_dir = os.path.dirname(os.path.abspath(vim.eval(\'expand("<sfile>:p")\')))',
        \ 'parent_dir = os.path.dirname(plugin_dir)',
        \ 'if parent_dir not in sys.path:',
        \ '    sys.path.insert(0, parent_dir)',
        \ '',
        \ 'from gpt_comment_reflow import main',
        \ 'main()',
        \ ], "\n")

    exec 'python3 ' . s:python_code
endfunction

command! GPTCommentReflow call GPTCommentReflow()
