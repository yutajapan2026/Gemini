# Gemini Desktop(非公式)
[Gemini API](https://github.com/googleapis/python-genai)をwebui化したもの。

## For Windows
Releasesにインストーラ版を公開予定

## For Linux
Releasesのバージョン(以下$VERSIONとしますが臨機応変に変更してください)を参照して
```
wget -O Gemini.zip https://github.com/yutajapan2026/Bat-To-Exe-Converter-64-Bit/archive/refs/tags/$VERSION.zip
sudo apt install unzip
unzip Gemini.zip
cd Gemini-$VERSION
bash launch.sh
```
で実行したほうが安定します。

## 特徴
- python-genaiモジュール使用
- Interactions API使用

## 機能
- APIキー確認機能
- チャット:記憶機能付き
- 音声合成:自動再生機能付き
