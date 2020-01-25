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
  
```bash
$ vim script
```
- To insert or write in the file and to save the file without exit.
   * To insert in file `Press i` . It will open write mode.
   * To save and not exit from vim. We can do 'ESC' then 'shift + ;' 'w' like `:w`.
   * To save the file and exit then we use `:wq`.
   * To save and exit forcefully then we use `:wq!`.
```console
#!/bin/bash
in vim editor


press i   ---> to insert in the file
:w        ---> to save the file
:wq       ---> to save and exit
:wq!      ---> to save and exit with forcefully
```
- To write in the file, in the last edit where is cursor position. To add more data after that press lowercase 'a'.
```bash

this is your script

press a  ---> where is cursor, it will start after that 
a stands for append.
```
- To save and exit without write 'w' and 'q' . We will use 'x'. Many programmers do 'wq' but we can use only 'x' instead of that.
```console

Keep going to write code...

:x         ---> save and exit
```
- To go in error line which one we know. Enter line number and press G. Error occured in line number 102, in editor `102G`. You can     use double 'gg' instead of 'G'. Error occured in line number 150, in editor `150gg`. Uppercase 'G' and Lowercase 'gg'.
```console

print("error occured in line number 102")


102G        ---> It goes in line number 102, We dont need to using down arrow
102gg       ---> similiar, who dont want to use uppercase. 
```
- To move into the next line without press i and enter after last line, we use lowercase 'o'.
```console

print("to move into next line")

press o      ---> to move into next line
```
- To copy lines in vim, we use 'yy' and how many lines do you want to copy `numbers+yy` like '100yy' 100 lines will be copy.
- To paste those copied lines. We use lowercase 'p'. after the current line or where we want.
```console

print("copying lines")
print("copying lines")
print("copying lines")

3yy       --->> this 3 lines will be copy 
press p   --->> to copy these 3 lines
```
- Uppercase 'A' is used to append insert data in end of the line.
- Uppercase 'I' is used to insert data in begining of the line.
```console

print("Uses of Uppercase 'A'")
print("Uses of Uppercase 'I'")
```
***Notice: Make sure this is all done in without insert mode. So press ESC before performing this tasks.***

- To undo recent changes in file we use lowercase 'u' and redo again that changes we use lowercase 'r'.
```bash

print("to undo changes we use lowercase 'u'")
print("to redo changes we use lowercase 'r'")
```



  
  
  
  
  
  
  
