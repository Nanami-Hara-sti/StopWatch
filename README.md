## プロジェクト概要

シンプルなストップウォッチを提供するデスクトップアプリです。各タイマーは独立して動作し、アプリ上で追加・削除やラベル編集ができます。個人利用のタイムトラッキングや、作業記録用途に向いています。

## 技術スタック

- Python 3.x
- tkinter（組み込みGUIライブラリ）
- PyInstaller（Windows向けにexe化する際に使用）

## 開発環境のセットアップ

### 前提条件

- Python 3.8 以上がインストールされていること
- 開発中に WSL やリモート環境で GUI を表示する場合は、Windows 側で X サーバ（例: VcXsrv）を起動し、DISPLAY 環境変数を設定する必要があります

### 起動方法（開発中）

1. ターミナルでリポジトリのルートに移動します。
2. 以下を実行してアプリを起動します:

```bash
python3 stopwatch.py
```

3. GUI が表示されない場合:
- Linux/WSL 上では Tkinter が別パッケージになっていることがあります。Ubuntu 系なら `sudo apt install python3-tk` でインストールしてください。

## Windows での配布（exe 化）

Windows 用に exe を作成する手順は `README_WINDOWS_BUILD.md` にまとめています。簡単な手順:

1. 仮想環境を作成して有効化
2. `pip install -r requirements.txt` を実行
3. `pyinstaller --onefile --noconsole --name StopWatch stopwatch.py` を実行
4. 出力 `dist\StopWatch.exe` を配布する

自動起動（ログオン時に起動）には、同リポジトリの `create_shortcut.ps1`（Startup フォルダへショートカットを作成）または Task Scheduler（`schtasks`）を使用する方法を記載しています。

## 開発上の注意点

- ビルド生成物（`dist/`, `build/`, `*.spec`）や仮想環境フォルダ（`.venv/`）はリポジトリに含めないでください。`.gitignore` に追加して管理してください。
- 実行ファイルを配布する際、Windows Defender やウイルス対策ソフトが警告することがあります。必要に応じて署名や例外登録を検討してください。

---

詳細な Windows 向け手順は `README_WINDOWS_BUILD.md` を参照してください。
