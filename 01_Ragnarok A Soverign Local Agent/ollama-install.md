# Installing Ollama

Ollama lets you run large language models locally. Follow the section for your operating system.

## Windows (PowerShell)

**Option 1: Installer script (recommended)**

```powershell
irm https://ollama.com/install.ps1 | iex
```

**Option 2: winget**

```powershell
winget install Ollama.Ollama
```

**Option 3: Manual installer**

Download `OllamaSetup.exe` from https://ollama.com/download/windows and run it.

Verify:

```powershell
ollama --version
```

## Linux

**One-line install script**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify and start the service (if it isn't already running):

```bash
ollama --version
sudo systemctl enable --now ollama
```

**Manual install** (if you prefer not to pipe a script to your shell): see https://github.com/ollama/ollama/blob/main/docs/linux.md

## macOS

**Option 1: Homebrew**

```bash
brew install ollama
```

Then start the server:

```bash
ollama serve
```

**Option 2: Desktop app**

Download the app from https://ollama.com/download/mac, open the `.zip`, and move Ollama to your Applications folder. Launch it once to start the background service.

Verify:

```bash
ollama --version
```

## Quick Test (all platforms)

Pull and run a model:

```bash
ollama run llama3.2
```

Other useful commands:

```bash
ollama list          # show downloaded models
ollama pull <model>  # download a model without running it
ollama rm <model>    # remove a model
```

The local API is available at `http://localhost:11434`.

## Notes

- Check https://ollama.com/download for the latest installer links, as they can change.
- Larger models need plenty of RAM/VRAM; start with a small model (e.g. `llama3.2`) to confirm everything works.
