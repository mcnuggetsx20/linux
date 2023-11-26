call plug#begin()
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-compe'
Plug 'doums/darcula'
Plug 'ayu-theme/ayu-vim'
Plug 'NLKNguyen/papercolor-theme'
Plug 'vim-python/python-syntax'
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
Plug 'nvim-tree/nvim-web-devicons' " optional, for file icons
Plug 'preservim/nerdtree'
Plug 'sainnhe/everforest'
Plug 'nvim-treesitter/nvim-treesitter'
Plug 'chriskempson/base16-vim'
call plug#end()

autocmd BufNewFile *.cpp 0r /mnt/hdd/Program-Files/Vim/ClassicTemplate.txt
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

if !has('nvim')
    set viminfo+=~/.config/nvim/viminfo
endif

let $LANG = 'en_US'
let g:python_highlight_all = 1
let g:python_highlight_indent_errors = 0
let g:NERDTreeShowHidden=1

source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

set viminfo='1000,\"100,:20,%,n~/.config/nvim/viminfo

set splitright

set langmenu=en_US
set hls
set is
set cb=unnamedplus
set gfn=8514oem
set expandtab
set tabstop=4
set shiftwidth=4
set si
set noshowmode
set belloff=all
set nu
set ignorecase

set undofile
set backup

set undodir=/mnt/hdd/vim_backups/undo
set backupdir=/mnt/hdd/vim_backups/backup
set directory=/mnt/hdd/vim_backups/swp

set laststatus=2

set statusline+=%#keyword#
set statusline+=\ %{(g:currentmode[mode()])}

set statusline+=%#Folded#
set statusline+=\ %F\ %=\ 

set statusline+=\%#number#\ 

set statusline+=\%#Folded#
set statusline+=\ [\%{&fileencoding?&fileencoding:&encoding}\]\ 

set statusline+=%#number#
set statusline+=\ %L\ lines\ 

set statusline+=%#string#
set statusline+=\ %{wordcount().words}\ words\ 

set statusline+=\%#TabLineSel#
set statusline+=\ %p%%\ 

set statusline+=\%#number#\ 

set statusline+=\%#Folded#
set statusline+=\ %l:%c\ 

set statusline+=%#function#
set statusline+=\ [NVIM]\ 

set guicursor=i:hor15-Cursor

set scrollback=10000

set numberwidth=5

"set guioptions -=m 
"set guioptions -=T
"set guioptions-=r

set termguicolors
colorscheme custom
"colorscheme ayu
"highlight Normal guibg=none

if (has('gui_running'))
    colorscheme darcula
    set guicursor=i:hor15-Cursor
    "set linespace=4
    set linespace=0
endif

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
tnoremap <Esc> <C-\><C-n>
nnoremap <C-t> :100vs term://bash <CR>
inoremap { {}<left>

nnoremap <F4> :w <bar> :Shell python -B %.txt <CR>
autocmd filetype cpp nnoremap <F3> :w <bar> :80vs term://bash -c 'g++ -std=c++17 -DLOCAL -Wall -Wextra -Wconversion -Wshadow -Wno-sign-conversion -D_GLIBCXX_DEBUG -fno-sanitize-recover=undefined -DAC % -o %:r && ./%:r' <bar> 0 <bar> start <CR><CR>
autocmd filetype c nnoremap <F3> :w <bar> :80vs term://bash -c 'gcc % -o %:r && ./%:r' <bar> 0 <bar> start <CR><CR>
autocmd filetype javascript nnoremap <F3> :w <bar> :Shell node % <CR>
autocmd filetype java nnoremap <F3> :w <bar> Shell javac % && java % <cr>
autocmd VimEnter * :silent exec "!kill -s SIGWINCH $PPID"
autocmd BufEnter * silent! lcd %:p:h
autocmd VimEnter * NERDTree | wincmd p
autocmd TabNew * if getcmdwintype() == '' | silent NERDTree | endif | wincmd p
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

autocmd BufReadPost *
  \ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'
  \ |   exe "normal! g`\""
  \ | endif

function! s:ExecuteInShell(command)
  let command = join(map(split(a:command), 'expand(v:val)'))
  let winnr = bufwinnr('^' . command . '$')
  silent! execute  winnr < 0 ? 'botright 80 vnew ' . fnameescape(command) : winnr . 'wincmd w'
  setlocal buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap number
  echo 'Execute ' . command . '...'
  silent! execute 'silent %!'. command
  silent! execute 'resize '
  silent! redraw
  silent! execute 'au BufUnload <buffer> execute bufwinnr(' . bufnr('#') . ') . ''wincmd w'''
  silent! execute 'nnoremap <silent> <buffer> <LocalLeader>r :call <SID>ExecuteInShell(''' . command . ''')<CR>'
  normal Go
  echo 'Shell command ' . command . ' executed.'

endfunction

command! -complete=shellcmd -nargs=+ Shell call s:ExecuteInShell(<q-args>)
command WW silent! :w !sudo tee % 

augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set rnu
    autocmd BufLeave,FocusLost,InsertEnter * set nornu
	autocmd BufLeave,FocusLost,InsertEnter * set nu
augroup END

lua << EOF
    vim.g.loaded_netrw = 1
    vim.g.loaded_netrwPlugin = 1
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
    require'lspconfig'.tsserver.setup{}

    require("catppuccin").setup({
        flavour = "mocha", -- latte, frappe, macchiato, mocha
        background = { -- :h background
            light = "latte",
            dark = "mocha",
        },
        transparent_background = true,
        show_end_of_buffer = false, -- show the '~' characters after the end of buffers
        term_colors = false,
        dim_inactive = {
            enabled = false,
            shade = "dark",
            percentage = 0.15,
        },
        no_italic = false, -- Force no italic
        no_bold = false, -- Force no bold
        styles = {
            comments = { "italic" },
            conditionals = { "italic" },
            loops = {},
            functions = {},
            keywords = {},
            strings = {},
            variables = {},
            numbers = {},
            booleans = {},
            properties = {},
            types = {},
            operators = {},
        },
        color_overrides = {
            latte = {
                text = "#cdd6f4",
            },
        },

        highlight_overrides = {
            frappe = function(frappe)
                return {
                    LineNr = { fg = "#656c88" },
                }
            end,
        },

        custom_highlights = function(colors)
            return {
                cppAfterColon = { fg = "#ef9f76" },
            }
        end,

        integrations = {
            cmp = true,
            gitsigns = true,
            nvimtree = true,
            telescope = true,
            notify = false,
            mini = false,
            -- For more plugins integrations please scroll down (https://github.com/catppuccin/nvim#integrations)
        },

        require'nvim-treesitter.configs'.setup {
          -- A list of parser names, or "all" (the four listed parsers should always be installed)
          ensure_installed = { "c", "vim", "python"},

          -- Install parsers synchronously (only applied to `ensure_installed`)
          sync_install = false,

          -- Automatically install missing parsers when entering buffer
          -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
          auto_install = false,

          disable = {"vim"},

          -- List of parsers to ignore installing (for "all")
          ignore_install = { "javascript" },

          ---- If you need to change the installation directory of the parsers (see -> Advanced Setup)
          -- parser_install_dir = "/some/path/to/store/parsers", -- Remember to run vim.opt.runtimepath:append("/some/path/to/store/parsers")!

          highlight = {
            enable = true,

            -- NOTE: these are the names of the parsers and not the filetype. (for example if you want to
            -- disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is
            -- the name of the parser)
            -- list of language that will be disabled

            -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
            -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
            -- Using this option may slow down your editor, and you may see some duplicate highlights.
            -- Instead of true it can also be a list of languages
            additional_vim_regex_highlighting = false,
          },
        }
    })

EOF

autocmd BufRead,BufNewFile * syn match parens /[()]/ | hi parens guifg=red
"colorscheme catppuccin-frappe

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
