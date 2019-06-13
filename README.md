正则表达式：相同规律 特点的一个文本

findall：匹配 从html匹配符合正则的所有内容

页面元素：<i class="board-index board-index-2">2</i>

.*?   代表匹配任意字符（懒惰匹配）

/d    代表数字

()    括号里面的值代表要提取的值

正则：re.compile('<dd>.*?board-index.*?>(/d+)</i>')