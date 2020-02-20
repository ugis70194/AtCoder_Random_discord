# AtCoder Random

## introduction
AtCoderの問題の中から指定された範囲のdifficultyの問題をランダムに1つ選んでリンクを貼ってくれるbotです.  
### Note
- difficultyの値はAtCoder ProblemsのAPIから取得しています
- リクエストごとにAPIを叩いているので無闇にリクエストを送りまくらないで下さい(負荷がかかります)
- 埋め込みリンクが表示されないときは問題へのリンクが繋がっていません.
    - もしそういった問題を見つけた場合は僕(<a href=https://twitter.com/ugis_prog>@ugis_prog</a>)まで知らせて下さい
- 指定された範囲のdifficultyの問題が無い場合は"問題がありません"と返ってきます
- レスポンスがあるまで2~3秒ほどかかるかもしれません 

## How to register a bot on Discord?
僕に登録用のリンクを聞いてください.ただし,基本的には身内にしか許可しません.  
リンクを開いた後,登録したいチャンネルにbotを登録してください.  

## Command
２つのコマンドがあります.
### \lower-upper
このコマンドはdifficultyが[lower, upper)の範囲の問題をランダムに1つ抽出します.  
例えば`\1200-1600`と入力するとdifficultyが1200~1599の問題から選ばれます.  

### \color
このコマンドはレートの色に対応するdifficultyの問題からランダムに1つ抽出します.  
例えば`\cyan`と入力するとdifficultyが1200~1599の問題から選ばれます.  

