#! python3
"""
# 将复制在剪切板中的多行内容每行前加上“   * ”（tab * 空格）。完成后示例：
	* 10.212.136.151
	* 10.212.136.153
	* 10.212.136.154
"""

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    #if i start with "["
    lines[i] = '\t* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
