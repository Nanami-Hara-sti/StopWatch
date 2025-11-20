@echo off
REM PythonのEXE化ツール「PyInstaller」をインストールします
pip install pyinstaller

echo.
echo --- Building StopWatch.exe ---
echo.

REM PyInstallerを実行します
REM --onefile: 関連ファイルをすべて1つのEXEにまとめます
REM --noconsole: GUIアプリ実行時に後ろで黒いコンソール画面が出ないようにします
pyinstaller --onefile --noconsole --name StopWatch stopwatch.py

echo.
echo --- Build finished! ---
echo `dist` フォルダ内に `StopWatch.exe` が作成されました。
echo.
pause
