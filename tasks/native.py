from invoke import task
from tasks.util import COVID_DIR, NATIVE_BUILD_DIR, DATA_DIR
from os import makedirs
from os.path import exists, join
from shutil import rmtree
from subprocess import run


@task(default=True)
def build(ctx, clean=False):
    """
    Build the native binary
    """
    if clean and exists(NATIVE_BUILD_DIR):
        rmtree(NATIVE_BUILD_DIR)

    makedirs(NATIVE_BUILD_DIR, exist_ok=True)

    cmake_cmd = [
        "cmake",
        "-G Ninja",
        "-DCMAKE_BUILD_TYPE=Release",
        COVID_DIR,
    ]

    run(
        " ".join(cmake_cmd),
        shell=True,
        check=True,
        cwd=NATIVE_BUILD_DIR,
    )

    run(
        "cmake --build . --target all",
        shell=True,
        check=True,
        cwd=NATIVE_BUILD_DIR,
    )


@task
def unzip(ctx):
    """
    Unzip compressed data from the Covid repo
    """
    files = [
        "wpop_eur.txt",
        "wpop_nga_adm1.txt",
        "wpop_us_terr.txt",
        "wpop_usacan.txt",
    ]

    pop_dir = join(DATA_DIR, "populations")

    for f in files:
        if exists(f):
            print("Skipping {}, already unzipped".format(f))
            continue

        run(
            "gunzip -c {}.gz > {}".format(f, f),
            shell=True,
            check=True,
            cwd=pop_dir,
        )
