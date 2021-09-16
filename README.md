# co2_visualize
CO2濃度及び室温表示アプリ。
動作イメージは以下。  
![image](https://user-images.githubusercontent.com/61326119/133564960-674c6861-c7bc-4da5-8c5d-5c7c987f1229.png)

co2_collect.pyで温度/co2濃度のログを取得し、  
ログから直近2日分のグラフを作成して表示する。  
co2.pyをブラウザから直接アクセスして使うことを想定しており、アクセス時に毎回グラフを生成し直す。

CO2測定器はCustom CO2miniを使用し、以下のライブラリ経由でアクセスする。  
https://github.com/heinemml/CO2Meter

# usage
1. co2_collect.pyを自動実行し、co2.logを作成
2. co2.pyをブラウザから実行。(apache2でpython cgiが使えるように設定する必要あり)

各ソースコードにはファイル名を固定で書き込んでいるが、  
以下の構成で使うことを想定している。

```
/var/www/
        html/
            co2.png         (tmp以下へのシンボリックリンク)
            temp.png        (tmp以下へのシンボリックリンク)
        cgi/
            co2.py          ※パーミッションを755に設定すること
            co2.log
            tmp/            ※ディレクトリのパーミッションを777に設定すること
                co2.png
                temp.png
```

# 動作環境
以下の確認で動作確認している。
- python3.7.3
- apache:2.4.38
- python3-matplotlib: 3.0.2-2
- pandas:1.3.3
