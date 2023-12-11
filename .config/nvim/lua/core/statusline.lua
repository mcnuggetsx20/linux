vim.api.nvim_exec([[
    let g:currentmode={
           \ 'n'  : 'NORMAL ',
           \ 'v'  : 'VISUAL ',
           \ 'V'  : 'V·Line ',
           \ "\<C-V>" : 'V·Block ',
           \ 'i'  : 'INSERT ',
           \ 'R'  : 'R ',
           \ 'Rv' : 'V·Replace ',
           \ 'c'  : 'Command ',
           \ 't'  : 'TERMINAL ',
           \}
    set laststatus=2

    set statusline+=%#keyword#
    set statusline+=\ %{(g:currentmode[mode()])}

    set statusline+=%#statusline#
    set statusline+=\ %F\ %=\ 

    set statusline+=%#number#
    set statusline+=\ %L\ lines

    set statusline+=%#string#
    set statusline+=\ %{wordcount().words}\ words

    set statusline+=%#function#
    set statusline+=\ [NVIM]

]], false)
