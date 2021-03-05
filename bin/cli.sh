#!/bin/bash

set -e

THIS_DIR=$(dirname $(readlink -f $0))
PROJ_ROOT=${THIS_DIR}/..

pushd ${PROJ_ROOT} > /dev/null

if [[ -z "${SYSROOT_CLI_IMAGE}" ]]; then
    VERSION=$(cat VERSION)
    SYSROOT_CLI_IMAGE=faasm/cpp-sysroot:${VERSION}
fi

INNER_SHELL=${SHELL:-"/bin/bash"}

docker-compose \
    up \
    --no-recreate \
    -d \
    cli 

docker-compose \
    exec \
    cli \
    ${INNER_SHELL}

popd > /dev/null
