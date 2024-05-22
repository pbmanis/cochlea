ENVNAME="cochlea_venv"
if [ -d $ENVNAME ]
then
    echo "Removing previous environment: $ENVNAME"
    set +e
    # rm -rf $ENVNAME
    #rsync -aR --remove-source-files $ENVNAME ~/.Trash/ || exit 1
    rm -R $ENVNAME
    set -e
else
    echo "No previous environment - ok to proceed"
fi

# note code used scikits.audiolab, which has not been updatef for 3.11 or 3.12.
python3.12 -m venv $ENVNAME
source $ENVNAME/bin/activate
pip3 install --upgrade pip  # be sure pip is up to date in the new env.
pip3 install wheel  # seems to be missing (note singular)
python3.12 -m pip install Cython
#pip3 install h5py --no-build-isolation
# brew install hdf5
# pip3 install h5py --no-build-isolation
# # if requirements.txt is not present, create:
# # pip install pipreqs
# # pipreqs
#
# #Then:
#
pip3 install -r requirements.txt
source $ENVNAME/bin/activate
python3 --version
