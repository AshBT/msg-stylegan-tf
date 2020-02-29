import os

"""Global configuration."""

# ----------------------------------------------------------------------------
# Paths.'msg-stylegan-tf'
repo_name = "msg-stylegan-tf"
parent_repo_dir = os.path.abspath(os.curdir).split(repo_name)[0] + repo_name + "/"


result_dir = parent_repo_dir + "/results"
data_dir = "/mnt/batch/tasks/shared/LS_root/mounts/clusters/stylegan-nc24/code/data/CanadianaLandscapes/1_tfrecord"
cache_dir = parent_repo_dir + "/cache"
run_dir_ignore = ["results", "data", "cache"]

# ----------------------------------------------------------------------------
