#!/usr/bin/env bash
C1A="\x1b[1G"
C1B='\x1b[30G'
C2A='\x1b[41G'
C2B='\x1b[70G'
alias ptab="printf '%s%s:%s\x1b[32m%s\x1b[m\n'"
VERSION=$(cat pyproject.toml|rg -i version|tr -d 'version = ')
PROJ=$(basename $PWD)
ptab $C1A "Project" $C1B $PROJ
ptab $C2A "Version" $C2B $VERSION


printf "Upgrading tools..."
pip install --upgrade setuptools &>/dev/null
pip install --upgrade build &>/dev/null
pip install --upgrade twine &>/dev/null
printf '\t\t\x1b[32mDONE\x1b[m\n'
printf 'Running Tests... '
python -m unittest &> .STATUS_TESTS
[[ -n $(cat .STATUS_TESTS|rg -i '^OK$') ]] && TESTSTATUS='OK' || TESTSTATUS='FAIL'
rm .STATUS_TESTS
printf '\t\t\x1b[32mDONE\x1b[m\t\tRESULT: \x1b[32m%s\x1b[m\n' $TESTSTATUS
printf 'building %s v%s ...' $PROJ $VERSION
python -m build &>/dev/null
printf '\t\t\x1b[32mDONE\x1b[m\n'
printf 'GIT:'
printf '\x1b[41GStaging:'
git add . &>/dev/null
printf '\x1b[70G\x1b[32mDONE\x1b[m\n'
printf '\tCommitting:'
echo "CURRENT VERSION: $VERSION :: TESTS: $TESTSTATUS :: CHANGED: " > .GITCOMMIT_MESSAGE
git status &>> .GITCOMMIT_MESSAGE &>/dev/null
git commit -m "$(cat .GITCOMMIT_MESSAGE)" &>/dev/null
printf '\x1b[30G\x1b[32mDONE\x1b[m\n'
printf '\tPushing'
git push &>/dev/null
printf '\x1b[30G\x1b[32mDONE\x1b[m\n'
printf '\n----------------------------------------------------------------------\n'
printf "Uploading to Pypi..\x1b[30G"
#twine upload  dist/* --verbose  --skip-existing  -u '__token__' -p "$(cat .PYPI_APIKEY)" &>/dev/null
printf 't\x1b[1;32mDONE\x1b[m\n________________________________________________________________________________\n________________________________________________________________________________\n\n'

