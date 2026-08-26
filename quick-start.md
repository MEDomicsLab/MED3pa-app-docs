---
description: Installation of the app
---

# 👊 Quick start

## How to download and install the MED3pa application

Packaged builds are published on the [releases page](https://github.com/MEDomicsLab/MED3pa-app/releases). The most recent is **v0.1.0-alpha.5**.

{% hint style="warning" %}
These are **pre-releases**. They are complete enough to run the whole pipeline, and are what this documentation is written against, but they carry an alpha version number for a reason: interfaces and file formats may still change between builds. Check the releases page for anything newer than the version named here.
{% endhint %}

{% tabs %}
{% tab title="Windows" %}
Download [**MED3pa-0.1.0-alpha.5-win.exe**](https://github.com/MEDomicsLab/MED3pa-app/releases/download/v0.1.0-alpha.5/MED3pa-0.1.0-alpha.5-win.exe) (93 MB) and run it.

If SmartScreen warns about an unrecognised publisher, choose **More info**, then **Run anyway**.
{% endtab %}

{% tab title="MacOS" %}
Download [**MED3pa-0.1.0-alpha.5-mac.dmg**](https://github.com/MEDomicsLab/MED3pa-app/releases/download/v0.1.0-alpha.5/MED3pa-0.1.0-alpha.5-mac.dmg) (123 MB), open it, and drag MED3pa into Applications.

If macOS refuses to open it on the first double-click, open it once from the right-click menu with **Open**, and confirm.
{% endtab %}

{% tab title="Linux" %}
Download [**MED3pa-0.1.0-alpha.5-linux.deb**](https://github.com/MEDomicsLab/MED3pa-app/releases/download/v0.1.0-alpha.5/MED3pa-0.1.0-alpha.5-linux.deb) (102 MB) and install it:

```bash
sudo apt install ./MED3pa-0.1.0-alpha.5-linux.deb
```

Using `apt` rather than `dpkg -i` lets it pull any missing dependencies in the same step.
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
**MongoDB is still required.** The application starts and stops `mongod` itself, but it does not ship it: install MongoDB Community Edition first and make sure it is on your `PATH`. The instructions are in [section 1.1](#id-1.-prerequisites) below, and they are the only part of the contribution guide that also applies to a packaged install.
{% endhint %}

On first launch you are asked to pick a **workspace folder**. The application then sets up its own bundled Python, so there is nothing to install for it. After that, open **System** from the header and check that the Go server, MongoDB and the Python environment are all reported as running or set. If an analysis fails immediately, that page is where the reason will be. See [Interface overview](interface-overview.md#system-page).

{% hint style="info" %}
If the Python setup did not complete, each release also ships **MED3pa-PythonEnv.zip**, a repair kit holding the requirements file and a script that builds the environment. See [section 3](#id-3.-python-environment).
{% endhint %}

### The MED3pa application architecture <a href="#the-med3pa-application-architecture" id="the-med3pa-application-architecture"></a>

MED3pa follows the same architecture as its [mother application](https://medomics.app/): an Electron shell, a Next.js renderer, a Go dispatcher and Python scripts, with a local MongoDB for storage.

```
Electron main (main/)      window, MongoDB lifecycle, Go server lifecycle, python env
        │  ipc
Renderer (renderer/)       Next.js UI: the MED3pa pages + a thin app shell
        │  HTTP :54388
Go server (go_server/)     request dispatcher; spawns python scripts, streams progress
        │  stdin/stdout JSON
Python (pythonCode/)       MED3pa analysis, model application, external-model import
        │
MongoDB :54117             datasets, models (GridFS), sessions, deployments, patients
```

Nothing calls the MED3pa library directly from the UI: the renderer posts a JSON configuration to the Go server, which runs the matching Python script and pipes progress back. [This visual guide](https://medomicslab.gitbook.io/medomics-docs/contributing#the-medomics-platform-architecture) is designed to support new contributors in understanding the structure of MEDomics applications in general.

***

## Contribute to MED3pa-App 🌱 <a href="#contribute-to-med3pa" id="contribute-to-med3pa"></a>

Everything from here on installs the application **from source**, which is what you want in order to modify MED3pa rather than only use it. If you installed a packaged build above, the one section that still concerns you is [1.1, MongoDB](#id-1.-prerequisites).

### 1. Prerequisites <a href="#id-1.-prerequisites" id="id-1.-prerequisites"></a>

**1.1 Installation of MongoDB Community Edition**

{% tabs %}
{% tab title="Windows" %}
[Install MongoDB on Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/#install-mongodb-community-edition)

* Do not install MongoDB as a service.
* You do not have to install MongoDB Compass.
* You do not have to install mongosh.
* Do not forget to [add MongoDB binaries to the System PATH](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/#add-mongodb-binaries-to-the-system-path).
{% endtab %}

{% tab title="Linux" %}
[Install MongoDB on Linux (Ubuntu)](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition) - Install the latest version of MongoDB.
{% endtab %}

{% tab title="MacOS" %}
[Install MongoDB Database Tools on Mac](https://www.mongodb.com/docs/database-tools/installation/installation-macos/#installation) - Install with Homebrew.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The application starts and stops `mongod` itself, against a configuration file it writes into your workspace at `.medomics/mongod.conf`. MongoDB only has to be reachable on your `PATH`.
{% endhint %}

**1.2 Installation of MongoDB database tools**

{% tabs %}
{% tab title="Windows" %}
Install with the [MSI](https://www.mongodb.com/docs/database-tools/installation/?operating-system=windows\&package-type=msi) Installer.
{% endtab %}

{% tab title="Linux" %}
Install with the [DEB](https://www.mongodb.com/docs/database-tools/installation/?operating-system=linux\&package-type=deb) package.
{% endtab %}

{% tab title="MacOS" %}
Install with [Homebrew](https://www.mongodb.com/docs/database-tools/installation/?operating-system=macos\&package-type=homebrew).
{% endtab %}
{% endtabs %}

### 2. Node.js and NVM Setup <a href="#id-2.-node.js-and-nvm-setup" id="id-2.-node.js-and-nvm-setup"></a>

**2.1 Installation of Nvm**

* [NVM for Windows](https://github.com/coreybutler/nvm-windows)
* [NVM for Ubuntu/MacOS](https://github.com/nvm-sh/nvm#installing-and-updating)

**2.2 Installation of npm/node.js**

```bash
nvm install lts
nvm use lts
```

Node.js 18 or later is required.

### 3. Python environment <a href="#id-3.-python-environment" id="id-3.-python-environment"></a>

A packaged install normally needs nothing here. The application ships its own Python and installs the requirements into it on first run, which is why the System page reports **Python bundled: Yes**. This section matters when you are building from source, or when that automatic setup did not complete.

The bundled interpreter is **CPython 3.12 on every platform**, Windows, macOS and Linux alike, so an environment you build yourself matches what ships as long as you leave the version alone.

Everything the Python layer needs is declared in one file, `pythonEnv/requirements.txt`, which is what both the packaged app and the developer script install from:

```bash
pip install -r pythonEnv/requirements.txt
```

{% hint style="info" %}
MED3pa itself comes from PyPI, pinned to a pre-release: `MED3pa==1.1.0a3`. Because it is a pre-release, a plain `pip install MED3pa` resolves to the older stable 1.0.4 instead. Pin the version, or pass `--pre`.
{% endhint %}

The rest of the file exists to hold a working combination together. `numpy` is held at 1.26.4 because MED3pa requires `<2.1.0`, which in turn forces `scipy` back to 1.11.4, the newest release happy on that numpy. `onnxruntime` must stay at 1.18 or later, since earlier releases cap at ONNX IR version 9 and reject IR 10 models outright.

### Building the environment yourself

A helper script wraps the same requirements file in a conda environment:

```bash
bash pythonEnv/create_conda_env.sh med3pa_app 3.12
```

The two arguments are the environment name and the Python version, both optional, defaulting to `med3pa_app` and 3.12. Leave the version at the default: it is what every platform bundles. The script also pins `openssl` to 3.0.20, because conda ships OpenSSL 3.5 by default and that combination breaks pip's certificate loading on some interpreters. When it finishes it prints the interpreter path.

Once the environment exists, point the application at that interpreter from the [System page](interface-overview.md#system-page).

### If the automatic setup failed

Every release ships [**MED3pa-PythonEnv.zip**](https://github.com/MEDomicsLab/MED3pa-app/releases/download/v0.1.0-alpha.5/MED3pa-PythonEnv.zip) for exactly this case. It is small, because it does **not** contain an environment: it holds `requirements.txt` and `create_conda_env.sh`, the two files above, so a packaged install can be repaired without cloning the repository.

Unzip it, run the script, and set the resulting interpreter on the System page.

***

{% hint style="warning" %}
Be careful, the next steps are different depending on the user's privilege.
{% endhint %}

***

<details>

<summary>For members of the <a href="https://github.com/MEDomicsLab">MEDomicsLab GitHub Organization</a>.</summary>

#### 4. Clone the Repository <a href="#id-4.-clone-the-repository" id="id-4.-clone-the-repository"></a>

Using HTTPS:

```zsh
git clone https://github.com/MEDomicsLab/MED3pa-app.git
```

Using SSH:

```zsh
git clone git@github.com:MEDomicsLab/MED3pa-app.git
```

#### 5. Backend Setup (Go) <a href="#id-5.-backend-setup-go" id="id-5.-backend-setup-go"></a>

**5.1 Install Go**

1. Download the latest stable release of Go (1.21+) from the official website: [https://golang.org/dl/](https://golang.org/dl/)
2. Follow the [installation instructions](https://go.dev/doc/install) for your operating system.

**5.2 Setup of environment**

Execute these commands in the terminal:

_**Windows:**_

```bash
setx GOPATH %USERPROFILE%\go
setx PATH "%PATH%;C:\Go\bin"
```

_**Linux/MacOS:**_

```bash
echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.bashrc
echo 'export GOPATH=$HOME/go' >> $HOME/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> $HOME/.bashrc
```

After, **close all your terminals** because these commands will take effect on the initialization of any terminal.

**5.3 Verify installation**

In a new terminal, run:

```bash
go version
```

If Go is installed correctly, you should see the version number printed to the console.

**5.4 Setup for the application**

```bash
cd <repo-path>/go_server
go run main.go   # initial run installs dependencies
```

Next, build the executable:

```bash
go build main.go
```

{% hint style="warning" %}
Rebuild after any `.go` file modification. `npm run dev` runs `npm run build:go` first, so in normal development this is done for you.
{% endhint %}

#### 6. Create Your Own Branch <a href="#id-6.-create-your-own-branch" id="id-6.-create-your-own-branch"></a>

Always branch from `master`, and ensure you have the latest changes:

```zsh
git checkout master
git pull origin master
git checkout -b your-branch-name
git push --set-upstream origin your-branch-name
```

#### 7. Make Changes <a href="#id-7.-make-changes" id="id-7.-make-changes"></a>

* Follow the project structure
* Keep commits **small and descriptive**

```zsh
git add .
git commit -m "feat: add new feature X"
```

Commit naming conventions:

* `feat:` new feature
* `fix:` bug fix
* `docs:` documentation changes
* `refactor:` code restructuring
* `test:` tests added/updated

***

#### 8. Push Changes <a href="#id-8.-push-changes" id="id-8.-push-changes"></a>

```zsh
git push
```

***

#### 9. Create a Pull Request <a href="#id-9.-create-a-pull-request" id="id-9.-create-a-pull-request"></a>

1. Go to the MED3pa-app GitHub [Pull Requests page](https://github.com/MEDomicsLab/MED3pa-app/pulls)
2. Click **New Pull Request**
3. Target branch: `master`
4. Compare branch: `your-branch-name`

***

#### 10. Pull Request Guidelines <a href="#id-10.-pull-request-guidelines" id="id-10.-pull-request-guidelines"></a>

Ensure:

* ✅ Code compiles and runs
* ✅ No console errors
* ✅ Proper formatting
* ✅ Tests pass (if applicable)
* ✅ Clear PR description:
  * What was done
  * Why was it done
  * Screenshots (if UI changes)

***

#### 11. Code Review Process <a href="#id-11.-code-review-process" id="id-11.-code-review-process"></a>

* Address reviewer comments
* Push updates to the same branch
* Keep discussion professional and concise

#### 12. After Merge <a href="#id-12.-after-merge" id="id-12.-after-merge"></a>

```zsh
git checkout master
git pull
git branch -d feature/your-feature-name # Time for a new feature
```

</details>

<details>

<summary>For external users</summary>

#### 🌱 Contributing via Fork (Common Practice) <a href="#contributing-via-fork-common-practice" id="contributing-via-fork-common-practice"></a>

This workflow is recommended for external contributors.

***

#### 4. Fork the Repository <a href="#id-4.-fork-the-repository" id="id-4.-fork-the-repository"></a>

1. Go to the [official repo](https://github.com/MEDomicsLab/MED3pa-app)
2. Click **Fork**
3. Clone your fork:

```zsh
git clone https://github.com/<your-username>/MED3pa-app.git
cd MED3pa-app
```

***

#### 5. Add Upstream Remote <a href="#id-5.-add-upstream-remote" id="id-5.-add-upstream-remote"></a>

```zsh
git remote add upstream https://github.com/MEDomicsLab/MED3pa-app.git
```

Verify:

```zsh
git remote -v
```

***

#### 6. Create a Feature Branch <a href="#id-6.-create-a-feature-branch" id="id-6.-create-a-feature-branch"></a>

Always branch from `master`:

```zsh
git fetch upstream
git checkout master
git pull upstream master

git checkout -b feature/your-feature-name
```

***

#### 7. Backend Setup (Go) <a href="#id-7.-backend-setup-go" id="id-7.-backend-setup-go"></a>

**7.1 Install Go**

1. Download the latest stable release of Go from the official website: [https://golang.org/dl/](https://golang.org/dl/)
2. Follow the [installation instructions](https://go.dev/doc/install) for your operating system.

**7.2 Setup of environment**

Execute these commands in the terminal:

_**Windows**_

```zsh
setx GOPATH %USERPROFILE%\go
setx PATH "%PATH%;C:\Go\bin"
```

_**Linux/MacOS**_

```zsh
echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.bashrc
echo 'export GOPATH=$HOME/go' >> $HOME/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> $HOME/.bashrc
```

After, **close all your terminals** because these commands will take effect on the initialization of any terminal.

**7.3 Verify installation**

In a new terminal, run:

```zsh
go version
```

**7.4 Setup for the application**

```zsh
cd <repo-path>/go_server
go run main.go   # initial run installs dependencies
go build main.go
```

***

#### 8. Make Changes <a href="#id-8.-make-changes" id="id-8.-make-changes"></a>

* Follow the project structure
* Keep commits **small and descriptive**

```zsh
git add .
git commit -m "feat: add new feature X"
```

***

#### 9. Sync with Upstream <a href="#id-9.-sync-with-upstream" id="id-9.-sync-with-upstream"></a>

Before pushing:

```zsh
git fetch upstream
git rebase upstream/master
```

***

#### 10. Push Changes <a href="#id-10.-push-changes" id="id-10.-push-changes"></a>

```zsh
git push origin feature/your-feature-name
```

***

#### 11. Create a Pull Request <a href="#id-11.-create-a-pull-request" id="id-11.-create-a-pull-request"></a>

1. Go to your fork on GitHub
2. Click **Compare & Pull Request**
3. Target branch: `master` (base repo)

***

#### 12. After Merge <a href="#id-12.-after-merge-1" id="id-12.-after-merge-1"></a>

```zsh
git checkout master
git pull upstream master
git branch -d feature/your-feature-name
```

</details>

***

#### Running the Electron App <a href="#run-the-electron-app" id="run-the-electron-app"></a>

Launch the Electron application (desktop app window) and start the required development servers (frontend/backend):

```shellscript
cd <repo_path/MED3pa-app>
npm install
npm run dev
```

`nextron` builds the renderer and launches Electron. On first launch you are asked to pick a **workspace folder**; this is where `DATA/` lives and where MongoDB stores its files.

#### Worth noting

{% hint style="info" %}
**MongoDB configuration**

MED3pa-app uses **port 54117** as the default MongoDB connection port. For database visualization and management, we recommend using [MongoDB Compass](https://www.mongodb.com/products/compass), the official GUI client from MongoDB.

**Key Details**:

* Default Port: `54117`
* Recommended Client: MongoDB Compass
* Connection String Format: `mongodb://localhost:54117/`
{% endhint %}

{% hint style="info" %}
**Modify startup settings**

1. Go to file `medomics.dev.js`
2. Here is a description of the object:

<pre class="language-javascript"><code class="lang-javascript"><strong>export const PORT_FINDING_METHOD = {
</strong>  FIX: 0,
  AVAILABLE: 1
};

const config = {
  // Automatically starts the backend server when the app launches
  runServerAutomatically: true,

  // Enables React Developer Tools (useful for debugging UI)
  useReactDevTools: false,

  // Default port used by the Electron/Go server
  defaultPort: 54388,

  // MongoDB connection port
  mongoPort: 54117,

  // Port allocation strategy:
  // FIX        -> Forces use of defaultPort (terminates conflicting processes if needed)
  // AVAILABLE  -> Finds the next available port if defaultPort is occupied
  portFindingMethod: PORT_FINDING_METHOD.FIX
};

export default config;
</code></pre>
{% endhint %}

### Testing Production Builds <a href="#testing-production-builds" id="testing-production-builds"></a>

#### Build & Run <a href="#build-and-run" id="build-and-run"></a>

This compiles the application code and packages the Electron app into an executable format:

{% tabs %}
{% tab title="Windows" %}
```bash
npm run build:win                       # build and package the application
.\build\dist\win-unpacked\MED3pa.exe    # run the executable of the built version
```
{% endtab %}

{% tab title="Linux" %}
```bash
npm run build:linux                     # build and package the application
bash build/dist/linux-unpacked/med3pa   # run the executable of the built version
```
{% endtab %}

{% tab title="MacOS" %}
```bash
npm run build:mac                                              # build and package the application
bash build/dist/mac-arm64/MED3pa.app/Contents/MacOS/med3pa     # run the executable of the built version
```
{% endtab %}
{% endtabs %}

The built app will be located in the `build/dist` folder.

**Now that the app is live and running, it is time to learn how to use the interface. See you on the next page.** :wink:
