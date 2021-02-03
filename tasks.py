import configparser
import datetime as dt
import os
import sys
import tempfile
import time
from pathlib import Path

from invoke import task, Responder
from klaxon import klaxon

APP = "restful_api_gateway"
AWS_PROFILE = "default"
AWS_REGION = "us-east-2"

# Must separate these by spaces and indicate directories with trailing /
BLACK_FILEPATH_STR = f"{APP}/ api/"


@task
def clean(c):
    """Delete unused code."""

    c.run("find . -name \*.pyc -delete")

    c.run("rm shelves/*", warn=True)

    c.run("rm -rf cdk.out/*")


@task
def install_hooks(c):
    """Install git hooks."""

    c.run("pre-commit install")

    c.run("pre-commit install -t pre-push")

    # Optionally install commitizen CLI
    try:
        c.run("commitizen", hide=True)
    except:
        c.run("npm install -g commitizen")


@task
def uninstall_hooks(c):
    """Uninstall git hooks."""
    c.run("pre-commit uninstall")
    c.run("pre-commit uninstall -t pre-push")


@task(aliases=["black"])
def format(c):
    """Auto-format Python modules."""
    c.run(f"black *.py {BLACK_FILEPATH_STR}")


@task(aliases=["check-black"])
def check_formatting(c):
    """Check that files conform to black standards."""
    c.run(f"black --check *.py {BLACK_FILEPATH_STR}")


@task(optional=["stack"])
def deploy(c, profile=AWS_PROFILE, region=AWS_REGION, force=False, app=APP, stack=None):
    """Deploy CDK CloudFormation stack(s)."""

    if stack:
        c.run(
            f"cdk deploy --profile={profile} {stack}"
            + (" --require-approval never" if force else ""),
            pty=True,
            env={"AWS_DEFAULT_REGION": region},
        )
    else:
        c.run(
            f"cdk deploy --profile={profile} '*'"
            + (" --require-approval never" if force else ""),
            pty=True,
            env={"AWS_DEFAULT_REGION": region},
        )

    klaxon(title=app, subtitle="deployed CDK stack")


@task(optional=["stack"])
def destroy(
    c, profile=AWS_PROFILE, region=AWS_REGION, force=False, app=APP, stack=None
):
    """Tear-down CDK CloudFormation stack(s)."""

    responder = Responder(pattern="Are you sure you want to delete.*", response="y\n")

    if stack:
        c.run(
            f"cdk destroy --profile={profile} {stack}",
            pty=True,
            watchers=[responder] if force else [],
            env={"AWS_DEFAULT_REGION": region},
        )
    else:
        c.run(
            f"cdk destroy --profile={profile} '*'",
            pty=True,
            watchers=[responder] if force else [],
            env={"AWS_DEFAULT_REGION": region},
        )

    klaxon(title=app, subtitle="destroyed CDK stack")


@task
def diff(c, profile=AWS_PROFILE, region=AWS_REGION):
    """Compare current CDK stack to what was previously deployed."""

    c.run(
        f"cdk diff --profile={profile}",
        pty=True,
        env={"AWS_DEFAULT_REGION": region},
    )


@task
def ls(c, profile=AWS_PROFILE):
    """List of CDK stacks that are deployable"""

    c.run(f"cdk list --profile {profile}")


@task(optional=["stack"])
def synth(c, profile=AWS_PROFILE, region=AWS_REGION, stack=None):
    """Render cdk cloudformation template."""

    if stack:
        c.run(
            f"cdk synth --profile={profile} {stack}",
            pty=True,
            env={"AWS_DEFAULT_REGION": region},
        )
    else:
        c.run(
            f"cdk synth --profile={profile} -e",
            pty=True,
            env={"AWS_DEFAULT_REGION": region},
        )
