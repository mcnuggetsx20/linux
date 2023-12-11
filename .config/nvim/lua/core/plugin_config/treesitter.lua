require'nvim-treesitter.configs'.setup {
    ensure_installed = {'c', 'cpp', 'lua', 'vim', 'java', 'python', 'css', 'html'},
    sync_install = false,
    auto_install = true,
    highlight = {
        enable = true,
    },
}
