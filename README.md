# AtCoder

## 環境

- Pythonインストール
  - anyenv
    ```
    $ brew install anyenv
    $ anyenv init
    $ echo 'eval "$(anyenv init -)"' >> ~/.bash_profile
    ```
  - pyenv
    ```
    $ anyenv install pyenv
    $ exec $SHELL -l
    $ pyenv install 3.8.2
    ```
- 作業フォルダ作成
  ```
  $ mkdir ~/at-coder
  $ cd ~/at-coder
  $ pyenv local 3.8.2
  ```
- テスト環境構築
  - online-judge-toolsをインストール
    ```
    $ pip install --upgrade pip
    $ pip install online-judge-tools
    ```
  - AtCoderにログイン
    ```
    $ oj login -u <Username> -p <Password> "https://atcoder.jp/"
    $ oj login --check "https://atcoder.jp/"
    ```
  - テストスクリプトに実行権限付与
    ```
    $ chmod +x cptest.sh
    ```
- Visual Studio Code設定
  - テストしたい問題の名前を確認
    - 問題のURLで確認可能
    - `https://atcoder.jp/contests/abc189/tasks/abc189_a`の場合は`abc189_a`
    - 以下問題名を`taskName`と表記する
  - コンテストのコード作成
    - `/tasks/`に`<taskName>.py`を作成
  - AtCoderのサンプルケースでテスト
    - `<taskName>.py`を開く
    - `Cmd + Shift + B`でテスト実施
      - 初回は`.vscode/tasks.json`を作成
  - 手動入力でテスト
    - `/input.txt`にテストパターンを入力
    - `<taskName>.py`を開く
    - `F5`でテスト実施
      - 初回は`.vscode/launch.json`を作成
