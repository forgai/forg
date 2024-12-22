import time
from typing import Dict, List

import pytest

import forgai

def teardown():
    # When an Agent is deleted, the following cascade: AgentBuilderJob, Build,
    # AgentExecutorJob, Execution. So we just have to delete
    # all the agents and the rest will be deleted automatically.
    _delete_all_agents()


def prepare() -> Dict:
    """
    Since it takes time for the agent to get built and for an execution to be created,
    we want to do these things once and then use the same data for all tests.

    This function was initially called `setup` but pytest kept running it twice,
    instead of once as it should. So, it got renamed to `prepare`.
    """

    agent = forg.Agent.create(
        name="testagent",
        script="def main():\n    print('hello world')\n",
        python_version="3.9",
    )

    agent_builder_job = forg.AgentBuilderJob.list(agent_id=agent.id).results[0]
    build_id = None
    # Wait for the build to finish and get its id
    while True:
        time.sleep(3)
        builds = forg.Build.list(agent_builder_job_id=agent_builder_job.id).results
        if len(builds) == 1:
            build = builds[0]
            if build.status == "success":
                build_id = build.id
                break
            elif build.status == "failure":
                raise Exception("Build failed.")

    execution = agent.execute()

    return {
        "agent_id": agent.id,
        "agent_builder_job_id": agent_builder_job.id,
        "build_id": build_id,
        "agent_executor_job_id": execution.agent_executor_job_id,  # type: ignore
        "execution_id": execution.id,
    }


@pytest.fixture(scope="session", autouse=True)
def prepare_and_teardown():
    """
    Run once at the beginning and once at the end of all tests.
    """

    data = prepare()
    yield data
    teardown()


def _get_every_page_paginated_resource(resource_class: type) -> List[object]:
    """
    Goes through all the pages of a paginated resource and returns a list of
    all the results.
    """
    ret = []
    resources = resource_class.list()  # type: ignore
    ret.extend(resources.results)
    while True:
        resources = resources.next()
        if resources is None:
            break
        ret.extend(resources.results)
    return ret


def _delete_all_agents():
    for agent in _get_every_page_paginated_resource(forg.Agent):
        forg.Agent.delete(agent.id)
