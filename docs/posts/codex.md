# codex

[TOC]

## 安装 wget

[winget-cli](https://github.com/microsoft/winget-cli/releases/tag/v1.29.30-preview)
[DesktopAppInstaller_Dependencies.zip](https://github.com/microsoft/winget-cli/releases/download/v1.29.30-preview/DesktopAppInstaller_Dependencies.zip)
[Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle](https://github.com/microsoft/winget-cli/releases/download/v1.29.30-preview/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle)

~~~powershell
cd C:\Users\root\Desktop\DesktopAppInstaller_Dependencies\x64
Add-AppxPackage -Path .\Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
Add-AppxPackage -Path .\Microsoft.VCLibs.140.00_14.0.33519.0_x64.appx
# Add-AppxPackage -Path .\Microsoft.WindowsAppRuntime.1.8_8000.616.304.0_x64.appx

cd ../../

Add-AppxPackage -Path .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
~~~

## 安装 fnm

~~~powershell
winget install Schniz.fnm
~~~

## 安装 node

~~~powershell
fnm install 24

if (-not (Test-Path $PROFILE)) { New-Item $PROFILE -Force }

Invoke-Item $PROFILE

fnm env --use-on-cd --shell powershell | Out-String | Invoke-Expression

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

# 重启 powershell

fnm use 24

node -v
~~~

## 安装 codex cli

~~~powershell
npm i -g @openai/codex
~~~

1. Microsoft Edge 浏览器
2. 设置
3. 系统和性能
4. 代理服务器设置
5. 打开代理设置
6. 手动设置代理
    * `192.168.1.2` `7897`

~~~powershell
mkdir codex-project

cd codex-project

codex
~~~

## 安装 mcp

~~~powershell
winget install Git.Git
winget install Microsoft.VisualStudioCode

git clone https://github.com/NoOne-hub/JSReverser-MCP.git

cd JSReverser-MCP

fnm use 24

npm i

npm run build
~~~
