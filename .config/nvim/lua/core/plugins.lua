local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
    use 'wbthomason/packer.nvim'
    use 'nvim-treesitter/nvim-treesitter'
    use 'nvim-tree/nvim-web-devicons'
    use 'preservim/nerdtree'

    -- color themes
    use {
        'ayu-theme/ayu-vim',
        'blueshirts/darcula',
        'lifepillar/vim-solarized8',
        'NLKNguyen/papercolor-theme',
        'Abstract-IDE/Abstract-cs',
        'olimorris/onedarkpro.nvim',
    }

    -- lsp
    use {
        'williamboman/mason.nvim',
        'williamboman/mason-lspconfig.nvim',
        'neovim/nvim-lspconfig',
        'williamboman/nvim-lsp-installer',
        'mfussenegger/nvim-jdtls',
        'simrat39/rust-tools.nvim',
    }

    -- completion
    use {
        'hrsh7th/nvim-cmp',
        'hrsh7th/cmp-nvim-lsp',
        'hrsh7th/cmp-buffer',
        'hrsh7th/cmp-path',
        'hrsh7th/cmp-cmdline',
        'hrsh7th/cmp-vsnip',
        'hrsh7th/vim-vsnip',
        'L3MON4D3/LuaSnip',
        "saadparwaiz1/cmp_luasnip",
        "rafamadriz/friendly-snippets",
    }

  -- My plugins here
  -- use 'foo1/bar1.nvim'
  -- use 'foo2/bar2.nvim'

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end
end)
