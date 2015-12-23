#VIM

## VIM模式
- Insert
  * Cursor <i>
  * Append -<a>
  * On new line -<o>
- Normal
  * move
  * Word:w;End word:e;Back word:b;Find :f+<any>
  * Replace:r;Delete:d <motion>;Change:c <motion>; c w|e|h
- Visual
  * <v>
  * ctrl+v
  * shift+v
- Command
  * <c><i><"> delete all in ""
  * d t ) delete all till first )
  * i <text> . - write some text and repeat
  * F <(> 
  
### Vim 列操作
10.1.5.214
10.1.5.212
10.1.5.210

结果：
 ping -c 4 10.5.5.214 >> result0
 ping -c 4 10.5.5.212 >> result0
 ping -c 4 10.5.5.210 >> result0

步骤1:
* ctrl+v/ctrl+q(windows)开始列操作
* 选中所选的列，G 到最后
* i开始列操作
