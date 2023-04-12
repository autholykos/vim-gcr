function! GPTCommentReflow()
    if &filetype != 'python'
        echo "vim-gcr only supports Python files."
        return
    endif

    python3 import vim
    python3 from gpt_comment_reflow import main
    python3 main()
endfunction

command! GPTCommentReflow call GPTCommentReflow()
