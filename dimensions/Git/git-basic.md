### History of Version Control Systems
> Local VCSs --> Centralized VCSs --> Distributed VCSs

### The way Git thinks about its data

- A set of files and changes made to each file over time
<img src="images/data_store_vcs.jpg" width="60%" height="60%"/>

- A stream of snapshots
<img src="images/data_store_git.jpg" width="60%" height="60%"/>


### The three states
- modified
- staged
- committed

### The three main sections
- Working directory
  - tracked: files that were in the last snapshot
  - untracked: any files in your working directory that were not in the last snapshot
- Staging area
- Git directory

### The basic workflow

<img src="images/git_states.jpg" width="60%" height="60%"/>

### Git has integrity
> Everything in Git is check-summed by SHA-1 hash, a 40-character string composed of hexadecimal characters.

### Common-used commands

#### git config
There are three different places to store git settings:
```
1. /etc/gitconfig: for every users on the system, `--system`
2. ~/.gitconfig or ~/.config/git/config: specific to your user, `--global`
3. <working_dir>/.git/config: specific to the single repository
```

#### git diff
```
- git diff
- git diff --staged/--cached
- git difftool, run `git difftool --tool-help` to see what is available on your system.
```

#### git mv

#### git rm (-f)

#### git log (-p) (-2) (--stat) (--pretty=oneline) (--pretty=format:"%h %s" --graph)

#### git commit --amend
Undoing Things: the second commit replaces the results of the first.
```
git commit -m "initial commit"
git add forgotten_file
git commit --amend
```

#### git reset HEAD \<file\>
Unstaging a Staged file: 

#### git checkout -- \<file\>
Unmodifying a Modified file: git copys another file over it.
  
#### git remote
Working with remotes:
```
git remote
git remote -v
git remote add <shortname> <url>
git fetch <remote-name/shortname>, i.e., git fetch origin

# git fetch vs. git pull
# fetch: downloads the data to local repository, does't merge it
# pull: fetch and merge

# To see more information about a particular remote
git remote show [remote-name]
git remote show origin

git remote rename current-name tobe-name
git remote rm [remote-name]
```

#### git tag

```
# Annotated Tags
git tag -a v1.4 -m "my version 1.4"
git tag
git show v1.4

# Lightweight Tags
git tag v1.4-lw
git show v1.4-lw

git push origin v1.4
git push origin --tags

# Checking out tags
git checkout -b version1.4 v1.4
```

#### Git aliases

```
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
$ git config --global alias.unstage 'reset HEAD --'
$ git config --global alias.last 'log -1 HEAD'

# run an external command, rather than a Git subcommand
# you start the command with a ! character
$ git config --global alias.visual '!gitk'
```
