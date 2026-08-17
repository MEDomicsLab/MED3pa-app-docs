---
description: Installation of the app
---

# 👊 Quick start

## How to download and install the MED3pa application

{% hint style="warning" %}
There is no packaged installer yet. Until the first release is published, the application is installed from source by following the steps below. The same steps are also the contribution guide.
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

{% hint style="danger" %}
**Python 3.12 is required, not merely recommended.** MED3pa pins `checkpointer==2.1.0`, and every `checkpointer` 2.x release declares `Requires-Python >=3.12`. On 3.11 the install fails outright with _No matching distribution found_.
{% endhint %}

The MED3pa library is **not on PyPI**. `pythonEnv/requirements.txt` installs it from GitHub at a pinned commit:

```bash
pip install -r pythonEnv/requirements.txt
```

A helper script builds the whole conda environment in the right order; `numpy` has to be pinned before MED3pa is installed, otherwise pip pulls `numpy` 2.x and a `scipy` that conflicts with MED3pa's own `numpy<2.1.0` requirement:

```bash
bash pythonEnv/create_conda_env.sh med3pa_app
```

If you are developing against a local checkout of the MED3pa library, pass it as a second argument to get an editable install instead:

```bash
bash pythonEnv/create_conda_env.sh med3pa_app ../packages/MED3pa
```

Once the environment exists, point the application at its interpreter from the [Settings page](interface-overview.md#settings-page).

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

Always branch from the development branch, and ensure you have the latest changes:

```zsh
git checkout develop
git pull origin develop
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

1. Go to the MED3paApp GitHub [Pull Requests page](https://github.com/Thedetektive/MED3paApp/pulls)
2. Click **New Pull Request**
3. Target branch: `develop`
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
git checkout develop
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

1. Go to the [official repo](https://github.com/Thedetektive/MED3paApp)
2. Click **Fork**
3. Clone your fork:

```zsh
git clone https://github.com/<your-username>/MED3paApp.git
cd MED3paApp
```

***

#### 5. Add Upstream Remote <a href="#id-5.-add-upstream-remote" id="id-5.-add-upstream-remote"></a>

```zsh
git remote add upstream https://github.com/Thedetektive/MED3paApp.git
```

Verify:

```zsh
git remote -v
```

***

#### 6. Create a Feature Branch <a href="#id-6.-create-a-feature-branch" id="id-6.-create-a-feature-branch"></a>

Always branch from `develop`:

```zsh
git fetch upstream
git checkout develop
git pull upstream develop

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
git rebase upstream/develop
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
3. Target branch: `develop` (base repo)

***

#### 12. After Merge <a href="#id-12.-after-merge-1" id="id-12.-after-merge-1"></a>

```zsh
git checkout develop
git pull upstream develop
git branch -d feature/your-feature-name
```

</details>

***

#### Running the Electron App <a href="#run-the-electron-app" id="run-the-electron-app"></a>

Launch the Electron application (desktop app window) and start the required development servers (frontend/backend):

```shellscript
cd <repo_path/MED3paApp>
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
