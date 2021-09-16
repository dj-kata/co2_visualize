# co2_visualize
CO2濃度及び室温表示アプリ

# usage
1. co2_collect.pyを自動実行し、co2.logを作成
2. co2.pyをブラウザから実行。(apache2でpython cgiが使えるように設定する必要あり)

各ソースコードにはファイル名を固定で書き込んでいるが、  
以下の構成で使うことを想定している。

```
/var/www/
        html/
            co2.png  (tmp以下へのシンボリックリンク)
            temp.png (tmp以下へのシンボリックリンク)
        cgi-bin/
            co2.py         ※パーミッションを755に設定すること
            co2.log
            tmp/           ※ディレクトリのパーミッションを777に設定すること
                co2.png
                temp.png
```
