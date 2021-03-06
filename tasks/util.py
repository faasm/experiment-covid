from os.path import dirname, realpath, expanduser, join, exists

HOME_DIR = expanduser("~")
PROJ_ROOT = dirname(dirname(realpath(__file__)))
COVID_DIR = join(PROJ_ROOT, "third-party", "covid-sim")
DATA_DIR = join(COVID_DIR, "data")
NATIVE_BUILD_DIR = join(PROJ_ROOT, "build", "native")
WASM_BUILD_DIR = join(PROJ_ROOT, "build", "wasm")

EXPERIMENTS_BASE_DIR = dirname(dirname(PROJ_ROOT))

FAASM_USER = "cov"
FAASM_FUNC = "sim"

IS_DOCKER = HOME_DIR.startswith("/root")

if IS_DOCKER:
    RESULTS_DIR = join(PROJ_ROOT, "results")
else:
    RESULTS_DIR = join(EXPERIMENTS_BASE_DIR, "results", "covid")


def get_experiments_base_version():
    ver_file = join(EXPERIMENTS_BASE_DIR, "VERSION")

    if not exists(ver_file):
        raise RuntimeError(
            "Expecting this to be a submodule experiments-base, but couldn't find {}",
            format(ver_file),
        )

    with open(ver_file, "r") as f:
        version = f.read()

    version = version.strip()
    return version
