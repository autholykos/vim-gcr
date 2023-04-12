ifunction! GPTCommentReflow()
    if &filetype != 'python'
        echo "vim-gpt-comment-reflow only supports Python files."
        return
    endif
    python3 << EOF
    import sys
    import os

    sys.path.append(os.path.dirname(__file__))
    import gpt_comment_reflow

    gpt_comment_reflow.main()
EOF
endfunction

command! GPTCommentReflow call GPTCommentReflow()
