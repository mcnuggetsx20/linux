function ExecuteInShell(command)
  local output = vim.fn.systemlist(command)

  local original_bufnr = vim.fn.bufnr('%')

  -- Sprawdź, czy bufor o nazwie "output" już istnieje
  local existing_bufnr = vim.fn.bufnr("output")
  if existing_bufnr ~= -1 and vim.fn.bufexists(existing_bufnr) == 1 then
    -- Bufor już istnieje, przełącz się do niego
    vim.api.nvim_buf_delete(existing_bufnr, { force = true })
    print('Buffer "output" already exists. Shell command ' .. command .. ' executed.')
  end

  --tworzenie nowego bufora
  local bufnr = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_set_current_buf(bufnr)

  --opcje tego nowego bufora
  vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, output) --tutaj wypelniamy go outputem
  vim.api.nvim_buf_set_option(bufnr, 'buftype', 'nofile')
  vim.api.nvim_buf_set_option(bufnr, 'bufhidden', 'wipe')
  vim.api.nvim_buf_set_option(bufnr, 'buflisted', false)
  vim.api.nvim_buf_set_option(bufnr, 'swapfile', false)
  vim.api.nvim_buf_set_option(bufnr, 'filetype', 'shelloutput')
  vim.api.nvim_buf_set_option(bufnr, 'readonly', true)
--------------
  vim.api.nvim_buf_set_name(bufnr, "output") --luzna nazwa bufora
  vim.cmd('topleft 120 vnew') -- tu sie cos jebi i jak bylo botright to sie odpalalo po lewej wiec dalem topleft i ema; rozmiar jest odwrotnie proporcjonalny
  vim.cmd('buffer ' .. original_bufnr) --powrot do pierwotengo bufora

  print('Shell command ' .. command .. ' executed.')
end

vim.cmd('command! -complete=shellcmd -nargs=+ Shell call v:lua.ExecuteInShell(<q-args>)')
vim.cmd [[command WW silent! :w !sudo tee %]]

function custom_action()
  local file_type = vim.bo.filetype --current filetype
  local current_file = vim.fn.expand('%:p')

  vim.cmd(":w")

  if file_type == 'python' then
      vim.cmd("silent Shell python -B " .. current_file)

  elseif file_type == 'java' then
      vim.cmd("silent Shell javac " .. current_file .. " && java " .. current_file)
    --nnoremap <F3> :w <bar> Shell javac % && java % <cr>

  else
      --default case
    ExecuteInShell('w | !echo "Default command"')
  end
end
