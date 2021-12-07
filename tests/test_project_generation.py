from distutils.dir_util import copy_tree

import copier
from git import Repo


def copy_template_to_committed_git_repo(generator_path):
    """This function is necessary because copier works only with versioned files,
    so we have to copy the working directory to another directory and commit the untracked
    and changed files."""
    copy_tree(".", generator_path)
    repo = Repo(generator_path)
    repo.git.add(all=True)
    repo.git.commit("--message='Commit working dir'", "--allow-empty")
    assert not repo.git.status(
        "--short"
    ), "the git status should be empty after committing"


def test_project_generation(tmp_path):
    generator_path = (tmp_path / "generator").as_posix()
    generated_path = (tmp_path / "generated").as_posix()
    copy_template_to_committed_git_repo(generator_path)
    copier.copy(
        generator_path,
        generated_path,
        vcs_ref="HEAD",
        data={"project_description": "test"},
    )
