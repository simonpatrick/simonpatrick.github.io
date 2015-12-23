" ==========================
" Author: Simon Patrick
" Version: 1.0
" Email: simonpatrick@163.com
" Sections:
"	-> initial plugin
"	-> General setting
"	-> Display setting
"	-> FielEncoding
"	-> Other
"	-> HotKeys
"============================
"============================
" init plugin
"============================
" 修改leader键
let mapleader =','
let g:mapleader=','

“开始语法高亮
syntax on

"install Vundle bundles
if filereadable(expand("~/.vimrc.bundles"))
	source ~/.vimrc.bundles
endif

"ensure ftdected
filetype plugin indent on

"============================
" general setting
"============================
"font and size
set guifont=Monaco:h20
"history 
set history=2000
"file type
filetype on
" 不同文件不同缩进
filetype indent on
" 允许插件
filetype plugin on
filetype plugin indent on

set autoread “ 文件自动载入
set shortmess=atI "启动时候不显示援助
” 备份到另外一个问题
" set backup
" set backext=.bak
" set backupdir=/tmp/vimbk
set nobackup
set noswapfile

"create undo files
if has('persistent_undo')
	set undolevels=1000
	set undoreload=10000
	set undofile
	set undodir=/tmp/vimundo/
endif

set wildignore=*.swp,*.bak,*.pyc,*.class,*.svn
“突出当前行
set cursorcolumn
set cursorline

” 退出vim后，内容显示终端
set t_ti= t_te=

set mouse-=a "不使用鼠标
