function! GPTCommentReflow()
    if &filetype != 'python'
        echo "vim-gcr only supports Python files."
        return
    endif

    python3 << EOF
    import vim
    from gpt_comment_reflow import main
    main()
    EOF
endfunction
