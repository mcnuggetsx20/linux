call plug#begin()
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-compe'
Plug 'doums/darcula'
call plug#end()

autocmd BufNewFile *.cpp 0r /mnt/hdd/Program-Files/Vim/ClassicTemplate.txt
let g:currentmode={
       \ 'n'  : 'NORMAL  ',
       \ 'v'  : 'VISUAL  ',
       \ 'V'  : 'V·Line  ',
       \ "\<C-V>" : 'V·Block  ',
       \ 'i'  : 'INSERT  ',
       \ 'R'  : 'R  ',
       \ 'Rv' : 'V·Replace  ',
       \ 'c'  : 'Command  ',
       \}

let $LANG = 'en_US'
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim
:lcd %:p:h

set langmenu=en_US
set hls
set is
set cb=unnamedplus
set gfn=Fixedsys\ Excelsior\ 12
set expandtab
set tabstop=4
set shiftwidth=4
set si
set noshowmode
set nowrap
set belloff=all
set nu

set undodir=/mnt/hdd/vim_backups/undo
set backupdir=/mnt/hdd/vim_backups/backup
set directory=/mnt/hdd/vim_backups/swp

set laststatus=2
set statusline+=\ %{(g:currentmode[mode()])}
set statusline+=%F\ %=\ %L\ lines,
set statusline+=\ %{wordcount().words}\ words
set statusline+=\ [NVIM]

set guicursor=i:hor15-Cursor

"set guioptions -=m 
"set guioptions -=T
"set guioptions-=r

set termguicolors 
colorscheme darcula
"colorscheme desert

nnoremap x "_x
vmap x "_d
nnoremap dd "_dd
nnoremap c "_c
nnoremap cc "_cc
nnoremap s ddko
nnoremap <F2> :%y+ <cr>
nnoremap <C-j> :tabprevious <CR>
nnoremap<C-k> :tabnext <CR>
nnoremap <C-x> :tabclose <CR>

nnoremap <F4> :w <bar> :Shell python -B % <CR>
autocmd filetype cpp nnoremap <F3> :w <bar> :Shell g++ -std=c++17 -DLOCAL -Wall -Wextra -Wconversion -Wshadow -Wno-sign-conversion -D_GLIBCXX_DEBUG -fno-sanitize-recover=undefined -DAC % -o %< && ./a <CR>

function! s:ExecuteInShell(command)
  let command = join(map(split(a:command), 'expand(v:val)'))
  let winnr = bufwinnr('^' . command . '$')
  silent! execute  winnr < 0 ? 'botright vnew ' . fnameescape(command) : winnr . 'wincmd w'
  setlocal buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap number
  echo 'Execute ' . command . '...'
  silent! execute 'silent %!'. command
  silent! execute 'resize '
  silent! redraw
  silent! execute 'au BufUnload <buffer> execute bufwinnr(' . bufnr('#') . ') . ''wincmd w'''
  silent! execute 'nnoremap <silent> <buffer> <LocalLeader>r :call <SID>ExecuteInShell(''' . command . ''')<CR>'
  echo 'Shell command ' . command . ' executed.'
endfunction

command! -complete=shellcmd -nargs=+ Shell call s:ExecuteInShell(<q-args>)
command WW silent! :w !sudo tee % <CR>

augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set rnu
    autocmd BufLeave,FocusLost,InsertEnter * set nornu
	autocmd BufLeave,FocusLost,InsertEnter * set nu
augroup END
set numberwidth=5

lua << EOF
    local nvim_lsp = require'lspconfig'
    vim.lsp.handlers["textDocument/publishDiagnostics"] = function(...) end

    require('lspconfig').pyright.setup{
      settings = {
        python = {
          analysis = {
            autoSearchPaths = true,
            useLibraryCodeForTypes = true
          }
        }
      }
    }

    require'lspconfig'.clangd.setup{}
EOF

set completeopt=menuone,noselect
let g:compe = {}
let g:compe.enabled = v:true
let g:compe.autocomplete = v:true
let g:compe.debug = v:false
let g:compe.min_length = 1
let g:compe.preselect = 'enable'
let g:compe.throttle_time = 80
let g:compe.source_timeout = 200
let g:compe.incomplete_delay = 400
let g:compe.max_abbr_width = 100
let g:compe.max_kind_width = 100
let g:compe.max_menu_width = 100
let g:compe.documentation = v:true
let g:compe.source = {}
let g:compe.source.path = v:true
let g:compe.source.buffer = v:true
let g:compe.source.calc = v:true
let g:compe.source.nvim_lsp = v:true
let g:compe.source.nvim_lua = v:true
let g:compe.source.vsnip = v:true
let g:compe.source.ultisnips = v:true

