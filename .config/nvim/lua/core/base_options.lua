--jakis wygladzik ni
vim.o.termguicolors = true
vim.cmd [[colorscheme gruvbox]]

--bazyczne ustawienia
LANG = 'en_US'
vim.o.hls = true
vim.o.is = true
vim.o.cb = 'unnamedplus'
vim.o.expandtab = true
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.ignorecase = true
vim.o.si = true
vim.o.showmode = false
vim.o.scrollback = 1000
vim.o.belloff = "all"

--te dziwne rozne foldery co se vim robi
vim.o.backup = true
vim.o.undofile = true
vim.o.undodir = "/mnt/hdd/vim_backups/undo"
vim.o.backupdir = "/mnt/hdd/vim_backups/backup"
vim.o.directory = "/mnt/hdd/vim_backups/swp"

--kursor
vim.o.guicursor="n:blinkon100,i:hor15-blinkon100"

--jakies luzne autocmd
vim.cmd [[autocmd BufEnter * silent! lcd %:p:h]]
vim.cmd [[autocmd BufNewFile *.cpp 0r /home/mcnuggetsx20/.config/ClassicTemplate.txt]]
vim.cmd [[autocmd VimEnter * :silent exec "!kill -s SIGWINCH $PPID"]]
vim.cmd [[autocmd VimEnter * NERDTree | wincmd p]]
vim.cmd [[autocmd TabNew * if getcmdwintype() == '' | silent NERDTree | endif | wincmd p]]
vim.cmd [[autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif]]

--numerki od williama lina
vim.o.number = true

vim.cmd([[
  augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
    autocmd BufLeave,FocusLost,InsertEnter * set norelativenumber
    autocmd BufLeave,FocusLost,InsertEnter * set number
  augroup END
]])
