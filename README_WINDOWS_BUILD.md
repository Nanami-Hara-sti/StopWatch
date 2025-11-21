# StopWatch - Windows ビルドと自動起動手順

このドキュメントは、現在の `stopwatch.py` を Windows 上で exe 化し、PC 起動時に自動で起動する方法を説明します。

前提
- Windows 上で作業すること
- Python 3.8+ がインストールされていること
- `pyinstaller` をインストール可能であること

1) 仮想環境作成（推奨）
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) 依存関係のインストール
```powershell
pip install -r requirements.txt
# requirements.txt には pyinstaller が含まれる
```

3) PyInstaller で exe 化
- 単一ファイル exe（コンソールなし）を作る例:
```powershell
pyinstaller --onefile --noconsole --name StopWatch stopwatch.py
```
- 出力は `dist\StopWatch.exe` になります。

4) スタートアップにショートカットを置く（PowerShell スクリプト）
- `create_shortcut.ps1` を使うと、指定した exe のショートカットを現在のユーザーの Startup フォルダに作成します。

5) タスクスケジューラを使う方法（代替）
- 管理者権限不要でログオン時に起動するタスクを作成する例:
```powershell
schtasks /Create /SC ONLOGON /TN "StopWatch" /TR "C:\path\to\StopWatch.exe" /RL HIGHEST
```

トラブルシューティング
- tkinter の GUI が表示されない場合、`--noconsole` を外してビルドし、実行時のエラー出力を確認してください。
- Windows Defender が exe をブロックする場合は、例外登録が必要になることがあります。
