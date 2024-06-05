#!/usr/bin/env bash
C1A=1
C1B=30
C2A=41
C2B=70

function ptab(){
	printf '\x1b[%sG\x1b[%sm%s\x1b[m' $1 $2 $3
}
VERSION=$(cat pyproject.toml|rg -i version|tr -d 'version = ')
PROJ=$(basename $PWD)
ptab $C1A 29 "Project:"
ptab $C1B 32 $PROJ
ptab $C2A 29 "Version:"
ptab $C2B 32 $VERSION
printf '\n'
ptab $C1A 29 "Upgrading tools:"
pip install --upgrade setuptools &>/dev/null
pip install --upgrade build &>/dev/null
pip install --upgrade twine &>/dev/null
ptab $C1B 32 "DONE"
printf '\n'
ptab $C1A 28 'Running Tests:'
python -m unittest &> .STATUS_TESTS
[[ -n $(cat .STATUS_TESTS|rg -i '^OK$') ]] && TESTSTATUS='OK' || TESTSTATUS='FAIL'
rm .STATUS_TESTS
ptab $C1B $DONE
ptab $C2A 'Result'
ptab $C2B "\x1b[32m$TESTSTATUS\x1b[32m"
printf '\n'
ptab  $C1A 'Building Project:'
python -m build &>/dev/null
ptab $C1B $DONE
ptab $C1A 'GIT'
ptab $C2A 'Staging:'
git add . &>/dev/null
ptab $C2B $DONE
printf '\n'
ptab $C2A 'Committing:'
echo "CURRENT VERSION: $VERSION :: TESTS: $TESTSTATUS :: CHANGED: " > .GITCOMMIT_MESSAGE
git status &>> .GITCOMMIT_MESSAGE &>/dev/null
git commit -m "$(cat .GITCOMMIT_MESSAGE)" &>/dev/null
ptab $C2B $DONE
ptab $C2A 'Pushing:'
git push &>/dev/null
ptab $C2B $DONE
printf '\n'
ptab $C1A "Pypi:"
ptab $C2A "Uploading:"

#twine upload  dist/* --verbose  --skip-existing  -u '__token__' -p "$(cat .PYPI_APIKEY)" &>/dev/null
ptab $C2B $DONE

printf '\n________________________________________________________________________________\n________________________________________________________________________________\n\n'
