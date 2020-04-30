source ./env/bin/activate
export $(grep -v '^#' .env | xargs)