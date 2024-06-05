#!/usr/bin/env bash
C1A=1
C1B=30
C2A=41
C2B=70
DONE='\xb[1;32mDONE\x1b[m'
function ptab(){
	printf '\x1b[%sG%s' $1 $2
}
VERSION=$(cat pyproject.toml|rg -i version|tr -d 'version = ')
PROJ=$(basename $PWD)
ptab $C1A "Project:"
ptab $C1B $PROJ
ptab $C2A "Version:"
ptab $C2B $VERSION
printf '\n'
ptab $C1A "Upgrading tools:"
pip install --upgrade setuptools &>/dev/null
pip install --upgrade build &>/dev/null
pip install --upgrade twine &>/dev/null
ptab $C1B $DONE
printf '\n'
ptab $C1A'Running Tests:'
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
