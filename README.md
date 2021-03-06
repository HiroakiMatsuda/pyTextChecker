pytextcheck
======================
pytextcheckはテキスト中の特定の語句を検出するPython Scriptです．

あなたのテキスト形式で書かれた文書内の，特定の語句を検出します．  
例えば，あなたのTexで書かれた論文の語句チェックに使用することができます．  
  
論文や公開を前提とした文書では禁止語句が設定されています．  
誤植・誤字を防ぐため，禁止語句を検索欄に入力し，何度も検索を繰り返し確認するのは大変面倒です．  
pytextcheckは禁止語句リストとあなたの文書を比較し，その語句と行番号を教えてくれます．  
このモジュールは非生産的な作業からあなたを開放し，効率のよい文書作成を手助けします．

動作確認環境
------
Python:  
2.6.6  

OS:  
Windows 7 64bit / 32bit  
Ubuntu 12.04 LTS 32bit

現在対応している文字コード
------
・utf-8  
・shift-jis  
・enu-jp  
・iso2022-jp

使い方
------
###1. pytextcheckをDLする###
pytextcheckは標準モジュールのみで構成されていますので，スクリプトをDLすればすぐ使えます．  

###2. Python ShellからTexファイルをチェックしてみる###
Python ShellからTexファイルの中身をチェックします．

レポジトリ内にあるサンプルファイルをDLして使用して下さい．  
使用するファイルは以下のようになっています．  

 ・test.tex  
禁止語句が含まれていないか調べる，対象のファイルです．  
テクストで書かれているファイルであれば拡張子は問いません．

・basic.txt  
ファイル内に，「?」「、」「。」が禁止語句として設定されています．  

・sice.txt  
計測自動制御学会が定める禁止語句が設定されています．  

```python  
import pytextcheck  
t = Text()  
t.check_text('test.tex', 'basic.txt', 'sice.txt') 
```   
以上のように簡単に禁止語句を確認することができます．  
メソッドの詳しい使い方は以下を御覧ください．

###3. メソッドの使い方###
    check_text(self, text_path, *check_path)
文書内の禁止語句を検出します．  
 ・ `text_path` :  
    チェックを行う文書のパスを指定します．  
 ・   `*check_path` :  
    任意の数のチェックリストのパスを指定します．  
    複数のチェックリストを指定する場合は，例のように”,”で区切り指定して下さい．

###4. チェックリストの作成方法###
チェックリストはただのテキストファイルです．  
禁止語句を1行に１つずつ配置して下さい．  
サンプルファイルを参考にして下さい．  



ライセンス
----------
Copyright &copy; 2013 Hiroaki Matsuda  
Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and  [Apache License, Version 2.0][Apache].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php