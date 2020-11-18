# AtCoder

## 環境

- Python
  - anyenvをインストール
    ```
    $ brew install anyenv
    $ anyenv init
    $ echo 'eval "$(anyenv init -)"' >> ~/.bash_profile
    ```
  - pyenvをインストール
    ```
    $ anyenv install pyenv
    $ exec $SHELL -l
    $ pyenv install 3.8.2
    ```
  - 作業フォルダを作成
    ```
    $ mkdir ~/at-coder
    $ cd ~/AtCoder/
    $ pyenv local 3.8.2
    ```
- テスト
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
  - テストスクリプト
    ```
    $ chmod +x cptest.sh
    ```
- Visual Studio Code
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
