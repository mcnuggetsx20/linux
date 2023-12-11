vim.g.mapleader = '<C-'
vim.keymap.set('n', '<leader>h', ':nohlsearch<CR>')

vim.api.nvim_set_keymap('n', 'x', '"_x', { noremap = true })
vim.api.nvim_set_keymap('v', 'x', '"_d', { noremap = true })
vim.api.nvim_set_keymap('n', 'dd', '"_dd', { noremap = true })
vim.api.nvim_set_keymap('n', 'c', '"_c', { noremap = true })
vim.api.nvim_set_keymap('n', 'cc', '"_cc', { noremap = true })
vim.api.nvim_set_keymap('n', 's', '"_ddko', { noremap = true })
vim.api.nvim_set_keymap('n', '<F2>', ':%y+<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', '<C-j>', ':tabprevious<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', '<C-k>', ':tabnext<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', '<C-x>', ':tabclose<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', '<F3>', [[:lua custom_action()<CR>]], { noremap = true, silent = true })

vim.api.nvim_set_keymap('i', '{', '{}<Left>', { noremap = true })
vim.api.nvim_set_keymap('i', '{<CR>', '{<CR>}<Esc>O', { noremap = true })
vim.api.nvim_set_keymap('i', '{{', '{{', { noremap = true })
vim.api.nvim_set_keymap('i', '{}<Space>', '{}<Space>', { noremap = true })

vim.api.nvim_set_keymap('t', '<Esc>', '<C-\\><C-n>', { noremap = true })

