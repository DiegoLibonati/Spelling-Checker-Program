# -*- mode: python ; coding: utf-8 -*-
# NOTE: The '.env' entry below bundles the repo-level .env into the binary.
# For production builds, create a separate .env.prod file with real values and
# replace '.env' here with '.env.prod' before running PyInstaller.
# Never commit production secrets to the repo-level .env.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('venv\\Lib\\site-packages\\spellchecker\\resources', 'spellchecker\\resources'), ('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
