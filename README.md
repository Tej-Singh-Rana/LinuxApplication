# LinuxApplication
* Bash | Sh | Tsh |

# Few tips to How to use vim editor.

- `vim --version`
```bash
$ vim --version
VIM - Vi IMproved 8.1 (2018 May 18, compiled Oct  1 2019 05:31:13)
Included patches: 1-2104
Compiled by <alexpux@gmail.com>
Huge version without GUI.  Features included (+) or not (-):
+acl               -farsi             -mouse_sysmouse    -tag_any_white
+arabic            +file_in_path      +mouse_urxvt       -tcl
+autocmd           +find_in_path      +mouse_xterm       +termguicolors
+autochdir         +float             +multi_byte        +terminal
-autoservername    +folding           +multi_lang        +terminfo
-balloon_eval      -footer            -mzscheme          +termresponse
+balloon_eval_term +fork()            +netbeans_intg     +textobjects
-browse            +gettext           +num64             +textprop
++builtin_terms    -hangul_input      +packages          +timers
+byte_offset       +iconv             +path_extra        +title
+channel           +insert_expand     +perl/dyn          -toolbar
+cindent           +job               +persistent_undo   +user_commands
-clientserver      +jumplist          +postscript        +vartabs
+clipboard         +keymap            +printer           +vertsplit
+cmdline_compl     +lambda            +profile           +virtualedit
+cmdline_hist      +langmap           +python/dyn        +visual
+cmdline_info      +libcall           +python3/dyn       +visualextra
+comments          +linebreak         +quickfix          +viminfo
+conceal           +lispindent        +reltime           +vreplace
+cryptv            +listcmds          +rightleft         +wildignore
+cscope            +localmap          +ruby/dyn          +wildmenu
+cursorbind        -lua               +scrollbind        +windows
+cursorshape       +menu              +signs             +writebackup
+dialog_con        +mksession         +smartindent       -X11
+diff              +modify_fname      -sound             -xfontset
+digraphs          +mouse             +spell             -xim
-dnd               -mouseshape        +startuptime       -xpm
-ebcdic            +mouse_dec         +statusline        -xsmp
+emacs_tags        -mouse_gpm         -sun_workshop      -xterm_clipboard
+eval              -mouse_jsbterm     +syntax            -xterm_save
+ex_extra          +mouse_netterm     +tag_binary
+extra_search      +mouse_sgr         -tag_old_static
   system vimrc file: "/etc/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/etc"
 f-b for $VIMRUNTIME: "/usr/share/vim/vim81"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H   -I/usr/include/ncursesw  -march=x86-64 -mtune=generic -O2 -pipe -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1
Linking: gcc   -L. -pipe -fstack-protector-strong -pipe -Wl,--as-needed -o vim.exe        -lm -lelf    -lncursesw -liconv -lacl -lintl   -Wl,--enable-auto-import -Wl,--export-all-symbols -Wl,--enable-auto-image-base -fstack-protector-strong  -L/usr/lib/perl5/core_perl/CORE -lperl -lpthread -ldl -lcrypt
```
- In yum, to know details of vim packages.
  - `yum list vim*`
```console
$ yum list vim*
  
```
- To create a new file in linux and write script.
  - `vim file-name`
  
```console
$ vim script
```
- To insert or write in the file and to save the file without exit.
   * To insert in file `press i` . It will on insert mode.
   * To save and not exit from vim. We can do 'ESC' then 'shift + ;' 'w' like `:w`.
   * To save the file and exit then we use `:wq`.
   * To save and exit forcefully then we use `:wq!`. Sometimes permission issue.
   * To exit with forcefull then we use `:q!`. When you stuck and cannot save files.
```bash
#!/bin/bash
in vim editor


press i   ---> to insert in the file
:w        ---> to save the file
:wq       ---> to save and exit
:wq!      ---> to save and exit with forcefully
:q!       ---> to quit forcefully
```
- To write in the file, in the last edit where is cursor position. To add more data after that press lowercase 'a'.
```bash

this is your script

press a  ---> where is cursor, it will start after that 
a stands for append.
```
- To save and exit without write 'w' and 'q' . We will use 'x'. Many programmers do 'wq' but we can use only 'x' instead of that.
```bash

Keep going to write code...

:x         ---> save and exit
```
- It goes in error line which one we know. Enter line number and press G. For example, Error occured in line number 102, then in           editor type `102G`, without press any editor key. It will not shows. Sometimes, you can use double 'gg' instead of 'G'. For example,     Error occured in line number 150, in editor same things we have to do type `150gg`. Without press any editor key.
```bash

print("error occured in line number 102")


102G        ---> It goes in line number 102, We dont need to use down arrow
102gg       ---> similiar, who dont want to use uppercase
```
- To move into the next line without press i and then enter, to ignore this steps. We can do after last line, press lowercase 'o' to add   data.
```bash

print("to move into next line")

press o      ---> to move into next line
```
- To copy lines in vim, we use 'yy' and how many lines do you want to copy `numbers+yy` like '100yy' 100 lines will be copied.
- To paste those copied lines. We use lowercase 'p'. after the current line or where we want.
```bash

print("copying lines")
print("copying lines")
print("copying lines")

3yy       --->> this 3 lines will be copy 
press p   --->> to paste these 3 lines
```
- Uppercase 'A' is used to append insert data in end of the line.
- Uppercase 'I' is used to add data in begining of the line.
```bash

print("uses of Uppercase 'A'")
print("uses of Uppercase 'I'")

```
***Notice: Make sure this is all done in without insert mode. So press ESC before performing this tasks.***

- To undo recent changes in file we use lowercase 'u' and to get again that changes we use lowercase 'r' with ctrl key.
```bash

print("to undo changes we use lowercase 'u'")
print("to get changes we use lowercase 'r'")

press u     ---> to undo changes
ctrl + r    ---> to get that changes again
```
- To change case of any alphabets into the file (uppercase or lowercase), we use `~` with `shift`. If we dont use shift then it will give a    sign of '`'.
```bash

This is your code
~   ---> used on uppercase T
this is your code

shift + ~    ---> to make changes into uppercase and lowercase
```
- To copy of just previous word. We use '.' (dot). Overall dot perfomed just previous tasks.
```bash

export JAVA_HOME = /java            ---> press I and move into the starting of line and type export
export HADOOP_HOME = /hadoop        ---> then move into the 2nd line and press .(dot)
  (after press . (dot), export is copied in 2nd line) 
```  
- Whitespace and Indent levels in editor
  * To set in vim editor tabs and indents.
  * To see hidden character `:set list`.
  * To turn off the listing mode `:set nolist`.
  * To turn off the high lights `:set nohls`.
  * To set permanent basis we have to write in `.vimrc` file in user's home directory.
  * `.vimrc` ***----> set et ts=2 sw=2 ai***
  * To set tabs in editor et=expand tab -- translate enter tabs into the space, ts=translate space, sw=shift width, ai=auto indent.
  * After this settings tabs will not follow how many spaces you give in previous. It will give only 2 or 3 what you set it.
```bash
#!/bin/bash

........(tabs)code

  
:set et ts=2 sw=2 ai

after this settings 
.....code 'then enter'
         code
----------moving to starting line--------         
code..(only 2 spaces will follow not 5 spaces)
```
- To Search and Replace text in file 
   *
```console
# vim +/PermitRoot sshd_config

It will not move in that point what we are searching

# vim +/^PermitRoot sshd_config

It will be move to beginning of the lines to search 

# vim +22 sshd_config

It will be move to direct line number 22.
If it is high lights the words then use ":set nohls"
```



```
