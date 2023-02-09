if exists("g:custom")
  finish
endif
let g:custom = 1
highlight clear
if exists("syntax_on")
  syntax reset
endif

let g:colors_name='custom'

autocmd BufRead,BufNewFile * syn match parens /[(){}]/ | hi parens ctermfg=red

hi Normal ctermfg=Black ctermbg=White guifg=Black
hi SpecialKey term=bold ctermfg=1 guifg=Blue
hi link EndOfBuffer NonText
hi NonText term=bold ctermfg=9 gui=bold guifg=Blue
hi Directory term=bold ctermfg=1 guifg=Blue
hi ErrorMsg term=standout ctermfg=15 ctermbg=4 guifg=White guibg=Red
hi IncSearch term=reverse cterm=reverse gui=reverse
hi Search term=reverse ctermfg=0 ctermbg=14 guibg=Yellow
hi link CurSearch Search
hi MoreMsg term=bold ctermfg=2 gui=bold guifg=SeaGreen
hi ModeMsg term=bold cterm=bold gui=bold
hi LineNr term=underline ctermfg=6 guifg=Brown
hi CursorLineNr term=bold cterm=underline ctermfg=6 gui=bold guifg=Brown
hi link CursorLineSign SignColumn
hi link CursorLineFold FoldColumn
hi Question term=standout ctermfg=2 gui=bold guifg=SeaGreen
hi StatusLine term=bold,reverse cterm=bold,reverse gui=bold,reverse
hi StatusLineNC term=reverse cterm=reverse gui=reverse
hi VertSplit term=reverse cterm=reverse gui=reverse
hi Title term=bold ctermfg=5 gui=bold guifg=Magenta
hi Visual term=reverse cterm=reverse guibg=LightGrey
hi VisualNOS term=bold,underline cterm=bold,underline gui=bold,underline
hi WarningMsg term=standout ctermfg=4 guifg=Red
hi WildMenu term=standout ctermfg=0 ctermbg=14 guifg=Black guibg=Yellow
hi Folded term=standout ctermfg=1 ctermbg=7 guifg=DarkBlue guibg=LightGrey
hi FoldColumn term=standout ctermfg=1 ctermbg=7 guifg=DarkBlue guibg=Grey
hi DiffAdd term=bold ctermbg=9 guibg=LightBlue
hi DiffChange term=bold ctermbg=13 guibg=LightMagenta
hi DiffDelete term=bold ctermfg=9 ctermbg=11 gui=bold guifg=Blue guibg=LightCyan
hi DiffText term=reverse cterm=bold ctermbg=12 gui=bold guibg=Red
hi SignColumn term=standout ctermfg=1 ctermbg=7 guifg=DarkBlue guibg=Grey
hi Conceal ctermfg=7 ctermbg=8 guifg=LightGrey guibg=DarkGrey
hi SpellBad term=reverse ctermbg=12 gui=undercurl guisp=Red
hi SpellCap term=reverse ctermbg=9 gui=undercurl guisp=Blue
hi SpellRare term=reverse ctermbg=13 gui=undercurl guisp=Magenta
hi SpellLocal term=underline ctermbg=11 gui=undercurl guisp=DarkCyan
hi Pmenu ctermfg=0 ctermbg=13 guibg=LightMagenta
hi PmenuSel ctermfg=0 ctermbg=7 guibg=Grey
hi PmenuSbar ctermbg=7 guibg=Grey
hi PmenuThumb ctermbg=0 guibg=Black
hi TabLine term=underline cterm=underline ctermfg=0 ctermbg=7 gui=underline guibg=LightGrey
hi TabLineSel term=bold cterm=bold gui=bold
hi TabLineFill term=reverse cterm=reverse gui=reverse
hi CursorColumn term=reverse ctermbg=7 guibg=Grey90
hi CursorLine term=underline cterm=underline guibg=Grey90
hi ColorColumn term=reverse ctermbg=12 guibg=LightRed
hi link QuickFixLine Search
hi StatusLineTerm term=bold,reverse cterm=bold ctermfg=15 ctermbg=2 gui=bold guifg=bg guibg=DarkGreen
hi StatusLineTermNC term=reverse ctermfg=15 ctermbg=2 guifg=bg guibg=DarkGreen
hi Cursor guifg=red guibg=red
hi lCursor guifg=bg guibg=fg
hi MatchParen term=reverse ctermbg=11 guibg=Cyan
hi ToolbarLine term=underline ctermbg=7 guibg=LightGrey
hi ToolbarButton cterm=bold ctermfg=15 ctermbg=8 gui=bold guifg=White guibg=Grey40
hi Comment term=bold ctermfg=1 guifg=Blue
hi Constant term=underline ctermfg=4 guifg=Magenta
hi Special term=bold ctermfg=5 guifg=#6a5acd
hi Identifier term=underline ctermfg=3 guifg=DarkCyan
hi Statement term=bold ctermfg=6 gui=bold guifg=Brown
hi PreProc term=underline ctermfg=5 guifg=#6a0dad
hi Type term=underline ctermfg=2 gui=bold guifg=SeaGreen
hi Underlined term=underline cterm=underline ctermfg=5 gui=underline guifg=SlateBlue
hi Ignore ctermfg=15 guifg=bg
hi Error term=reverse ctermfg=15 ctermbg=12 guifg=White guibg=Red
hi Todo term=standout ctermfg=0 ctermbg=14 guifg=Blue guibg=Yellow
hi link String Constant
hi link Character Constant
hi link Number Constant
hi link Boolean Constant
hi link Float Number
hi link Function Identifier
hi link Conditional Statement
hi link Repeat Statement
hi link Label Statement
hi link Operator Statement
hi link Keyword Statement
hi link Exception Statement
hi link Include PreProc
hi link Define PreProc
hi link Macro PreProc
hi link PreCondit PreProc
hi link StorageClass Type
hi link Structure Type
hi link Typedef Type
hi link Tag Special
hi link SpecialChar Special
hi link Delimiter Special
hi link SpecialComment Special
hi link Debug Special
hi link helpHeadline Statement
hi link helpSectionDelim PreProc
hi link helpIgnore Ignore
hi link helpExample Comment
hi link helpBar Ignore
hi link helpStar Ignore
hi link helpHyperTextJump Identifier
hi link helpHyperTextEntry String
hi link helpBacktick Ignore
"hi helpNormal cleared hi link helpVim Identifier
hi link helpOption Type
hi link helpCommand Comment
hi link helpHeader PreProc
"hi helpGraphic cleared
hi link helpNote Todo
hi link helpWarning Todo
hi link helpDeprecated Todo
hi link helpSpecial Special
"hi helpLeadBlank cleared
hi link helpNotVi Special
hi link helpComment Comment
hi link helpConstant Constant
hi link helpString String
hi link helpCharacter Character
hi link helpNumber Number
hi link helpBoolean Boolean
hi link helpFloat Float
hi link helpIdentifier Identifier
hi link helpFunction Function
hi link helpStatement Statement
hi link helpConditional Conditional
hi link helpRepeat Repeat
hi link helpLabel Label
hi link helpOperator Operator
hi link helpKeyword Keyword
hi link helpException Exception
hi link helpPreProc PreProc
hi link helpInclude Include
hi link helpDefine Define
hi link helpMacro Macro
hi link helpPreCondit PreCondit
hi link helpType Type
hi link helpStorageClass StorageClass
hi link helpStructure Structure
hi link helpTypedef Typedef
hi link helpSpecialChar SpecialChar
hi link helpTag Tag
hi link helpDelimiter Delimiter
hi link helpSpecialComment SpecialComment
hi link helpDebug Debug
hi link helpUnderlined Underlined
hi link helpError Error
hi link helpTodo Todo
hi link helpURL String

" C/C++
"call s:Hi('cMacroName', s:p.macroName)
hi! link cConstant cMacroName
hi! link cPreInclude String
hi! link cPreProcRegion NormalFg
hi! link cUserLabel NormalFg
hi! link cDataStructureKeyword Keyword
"call s:Hi('cDataStructure', s:p.cDataStructure)
hi! link cFunction Function
hi! link cppDestructor cFunction
hi! link cSemicolon Keyword
hi! link cComma Keyword
"call s:Hi('cppAfterColon', s:p.cStructField)
hi! link cppAfterColon Type
hi! link cppBeforeColon cDataStructure
"call s:Hi('cStructField', s:p.cStructField)
hi! link cppNullptr Keyword
hi! link cppTemplate Keyword
hi! link cTypedef Keyword
hi! link cppTypeName Keyword
hi! link cSpecial Keyword
hi! link cEnum Keyword
"call s:Hi('cSomeMacro', s:p.macroName)

" Rust
"call s:Hi('rustDeriveTrait', s:p.metaData)
hi! link rustQuestionMark Keyword
hi! link rustComma Keyword
hi! link rustSemicolon Keyword
hi! link rustOperator NormalFg
"call s:Hi('rustCommentLineDoc', s:p.docComment, s:p.null, 'italic')
"call s:Hi('rustMacro', s:p.rustMacro)
hi! link rustAssert rustMacro
hi! link rustPanic rustMacro
hi! link rustEscape Keyword
hi! link rustSigil NormalFg
hi! link rustSelf Keyword
"call s:Hi('rustLifetime', s:p.rustLifetime, s:p.null, 'italic')
"call s:Hi('rustTypeParameter', s:p.rustLifetime)
hi! link rustEnumVariant Constant
hi! link rustModPath NormalFg
hi! link rustModPathSep NormalFg
hi! link rustAs Keyword
hi! link rustConst Constant
hi! link rustVarField InstanceField

" Vim
hi! link vimOption Constant
hi! link vimFunction Function
hi! link vimContinue NonText
hi! link vimParenSep NormalFg
hi! link vimBracket PreProc
hi! link vimOper NormalFg
hi! link vimSep NormalFg
hi! link vimCommentString Comment

" JavaScript
hi! link jsNoise Keyword
hi! link JsImport Keyword
hi! link JsFrom Keyword
hi! link JsOperator NormalFg
hi! link jsArrowFunction NormalFg
hi! link jsFuncArgCommas Delimiter
hi! link jsObjectKey InstanceField
hi! link jsTernaryIfOperator NormalFg
hi! link jsObjectSeparator Keyword
hi! link jsSpreadOperator NormalFg
hi! link jsModuleComma Keyword
hi! link jsClassDefinition NormalFg
hi! link jsSuper Keyword
hi! link jsThis Keyword
hi! link jsObjectProp InstanceField
hi! link jsDestructuringNoise Keyword
hi! link jsClassProperty Function
hi! link jsBooleanTrue Keyword
hi! link jsBooleanFalse Keyword
hi! link jsObjectShorthandProp NormalFg
hi! link jsObjectColon NormalFg
hi! link jsExport Keyword
hi! link jsModuleAs Keyword

" TypeScript
hi! link typescriptBraces NormalFg
hi! link typescriptDocComment docComment
hi! link typescriptDocParam docComment
hi! link typescriptParens NormalFg
hi! link typescriptOpSymbols InstanceField
hi! link typescriptRegexpString Number
hi! link typescriptSpecial Keyword
hi! link typescriptLogicSymbols InstanceField
hi! link typescriptExceptions Keyword
"call s:Hi('typescriptDocTags', s:p.docComment, s:p.null, 'bold,italic,underline')
"call s:Hi('typescriptGlobalObjects', s:p.tsObject)

" JSON
hi! link jsonBraces NormalFg
hi! link jsonKeyword InstanceField
hi! link jsonNoise Keyword
hi! link jsonKeywordMatch Keyword
hi! link jsonBoolean Keyword
hi! link jsonNull Keyword
hi! link jsonEscape Keyword
hi! link jsonStringMatch String

" XML
"call s:Hi('xmlTagName', s:p.tag)
hi! link xmlEndTag xmlTagName
hi! link xmlAttrib NormalFg
hi! link xmlProcessingDelim xmlTagName
hi! link xmlDocTypeKeyword xmlTagName
hi! link xmlComment Comment
hi! link xmlCommentStart xmlComment
hi! link xmlCommentPart xmlComment
"call s:Hi('xmlEntity', s:p.entity)
hi! link xmlEntityPunct xmlEntity
hi! link xmlCdata NormalFg
hi! link xmlCdataCdata xmlCdata
hi! link xmlCdataStart xmlCdata
hi! link xmlCdataEnd xmlCdata
hi! link xmlNamespace InstanceField
hi! link xmlAttribPunct NormalFg
hi! link xmlEqual xmlString

" GraphQL
hi! link graphqlTaggedTemplate NormalFg

" YAML
hi! link yamlDocumentStart NormalFg
hi! link yamlDocumentEnd NormalFg
hi! link yamlComment docComment
hi! link yamlBlockMappingKey Keyword
hi! link yamlKeyValueDelimiter NormalFg
hi! link yamlInteger NormalFg
hi! link yamlFloat NormalFg
hi! link yamlBlockCollectionItemStart NormalFg
"call s:Hi('yamlAnchor', s:p.tag)
hi! link yamlAlias yamlAnchor
hi! link yamlBool NormalFg
hi! link yamlNodeTag NormalFg
hi! link yamlNull NormalFg

" Markdown
hi! link markdownH1 Constant
hi! link markdownH2 markdownH1
hi! link markdownH3 markdownH1
hi! link markdownH4 markdownH1
hi! link markdownH5 markdownH1
hi! link markdownH6 markdownH1
hi! link markdownHeadingRule markdownH1
hi! link markdownHeadingDelimiter markdownH1
"call s:Hi('markdownAutomaticLink', s:p.link, s:p.null, 'underline')
hi! link markdownBlockquote String
hi! link markdownBoldDelimiter Keyword
hi! link markdownBold NormalFg
hi! link markdownItalicDelimiter Keyword
hi! link markdownItalic NormalFg
hi! link markdownCode Comment
hi! link markdownCodeDelimiter markdownCode
hi! link markdownCodeBlock markdownCode
"call s:Hi('markdownLinkText', s:p.link, s:p.null, 'underline')
hi! link markdownLinkTextDelimiter markdownLinkText
hi! link markdownUrlDelimiter markdownLinkText
"call s:Hi('markdownUrl', s:p.function, s:p.null, 'italic')
hi! link markdownIdDelimiter Keyword
hi! link markdownLinkDelimiter Keyword
hi! link markdownIdDeclaration Keyword
hi! link markdownLinkDelimiter NormalFg
hi! link markdownUrlTitleDelimiter Comment
hi! link markdownRule Comment

" HTML
let html_no_rendering=1
"call s:Hi('htmlTag', s:p.tag)
hi! link htmlTagName htmlTag
hi! link htmlEndTag htmlTag
"call s:Hi('htmlArg', s:p.htmlAttribute)
"call s:Hi('htmlString', s:p.htmlString)
hi! link htmlValue htmlString
hi! link htmlComment Comment
hi! link htmlCommentError Comment
hi! link htmlCommentPart Comment
"call s:Hi('htmlSpecialChar', s:p.entity)
hi! link htmlSpecialTagName htmlTag

" CSS
hi! link cssAtKeyword Keyword
hi! link cssBraces NormalFg
hi! link cssAttributeSelector htmlTag
hi! link cssSelectorOp NormalFg
hi! link cssClassName htmlTag
hi! link cssNoise Keyword
hi! link cssAttrComma Keyword
hi! link cssFunctionComma Keyword
hi! link cssMediaComma Keyword
hi! link cssComment Comment
hi! link cssClassNameDot NormalFg
"call s:Hi('cssFunctionName', s:p.tag)
"call s:Hi('cssColor', s:p.number)
"call s:Hi('cssIdentifier', s:p.tag)
"call s:Hi('cssPseudoClassId', s:p.tag)
"call s:Hi('cssImportant', s:p.keyword, s:p.null, 'bold')
"call s:Hi('cssProp', s:p.htmlAttribute)
"call s:Hi('cssAttr', s:p.htmlString)
"call s:Hi('cssAttrRegion', s:p.htmlString)
"call s:Hi('cssURL', s:p.link)

" Shell Script
"call s:Hi('sheBang', s:p.fg, s:p.null, 'bold')
hi! link shRange NormalFg
hi! link shFunctionKey Keyword
"call s:Hi('shStatement', s:p.shCommand)
hi! link bashStatement shStatement
hi! link shDerefVar NormalFg
hi! link shQuote String
"call s:Hi('shHereDoc', s:p.null, s:p.templateLanguage)
"call s:Hi('shRedir', s:p.fg, s:p.null, 'bold')
hi! link shDerefSimple NormalFg
hi! link shCommandSubBQ InstanceField
hi! link shOption NormalFg
hi! link shCmdSubRegion shStatement
hi! link shCommandSub NormalFg
hi! link shLoop Keyword
hi! link shCommandSub Keyword
hi! link shSet shStatement
hi! link shFunctionTwo shStatement
hi! link shCtrlSeq String
hi! link shSpecial String
hi! link shCommandSub NormalFg
hi! link shDerefSpecial NormalFg
hi! link shOperator NormalFg
